#!/usr/bin/env bash
# run_pipeline.sh — launch the blog pipeline with secrets in env.
#
# The Ahrefs MCP authenticates with a plain API key
# (`Authorization: Bearer $AHREFS_MCP_KEY`, expanded by .mcp.json) — no OAuth,
# no refresh tokens, no token minting.
#
# Usage:
#   ./scripts/run_pipeline.sh "/keyword-research-pipeline --regen"
#   ./scripts/run_pipeline.sh "/blog-pipeline ai chatbot nsfw --context '...'"
#
# Requires:
#   * doppler CLI on PATH (DOPPLER_TOKEN in env, or interactive login)
#   * AHREFS_MCP_KEY, AHREFS_API_KEY, FIRECRAWL_API_KEY, OPENROUTER_API_KEY_BLOG_AGENT in
#     Doppler project `pleasurai`, config `dev`
#
# Headless-safe: no browser, no prompts, no terminal interaction. Claude is used
# only when explicit noninteractive API/token auth is available; otherwise the
# same prompt is run through Codex exec, which is the Paperclip runner's native
# unattended adapter.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 \"<claude prompt>\"" >&2
  exit 64
fi
PROMPT="$*"

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Resolve doppler: prefer PATH, fall back to known Paperclip install location.
if command -v doppler >/dev/null 2>&1; then
  DOPPLER_BIN="doppler"
elif [[ -x "/paperclip/.local/bin/doppler" ]]; then
  DOPPLER_BIN="/paperclip/.local/bin/doppler"
else
  echo "ERROR: doppler CLI not found on PATH or at /paperclip/.local/bin/doppler." >&2
  exit 1
fi

# Allow DOPPLER_KEY as a fallback token name (Paperclip runner injects DOPPLER_KEY).
export DOPPLER_TOKEN="${DOPPLER_TOKEN:-${DOPPLER_KEY:-}}"
if [[ -z "$DOPPLER_TOKEN" ]]; then
  echo "ERROR: neither DOPPLER_TOKEN nor DOPPLER_KEY is set." >&2
  exit 1
fi

case "$PROMPT" in
  *"/blog-pipeline"*|*"/auto-blog-loop"*)
    export BLOG_AGENT_AUTONOMOUS="${BLOG_AGENT_AUTONOMOUS:-1}"
    export UNATTENDED="${UNATTENDED:-1}"
    export BLOG_AGENT_AUTO_PUBLISH="${BLOG_AGENT_AUTO_PUBLISH:-1}"
    export BLOG_AGENT_REVISION_BUDGET="${BLOG_AGENT_REVISION_BUDGET:-2}"
    ;;
esac

claude_is_headless_ready() {
  command -v claude >/dev/null 2>&1 || return 1

  # API-key/token auth is the only default unattended-safe Claude path.
  if [[ -n "${ANTHROPIC_API_KEY:-}" || -n "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]]; then
    return 0
  fi

  if "$DOPPLER_BIN" secrets --only-names --project pleasurai --config dev 2>/dev/null \
    | grep -Eq '^(ANTHROPIC_API_KEY|CLAUDE_CODE_OAUTH_TOKEN)$'; then
    return 0
  fi

  # Cached Claude.ai OAuth can pass `claude auth status` while still failing in
  # headless org policy checks. Keep it opt-in for standalone VPS operators.
  if [[ "${BLOG_AGENT_ALLOW_CLAUDE_OAUTH:-0}" == "1" ]]; then
    timeout 20 claude auth status >/dev/null 2>&1
    return $?
  fi

  return 1
}

codex_is_ready() {
  command -v codex >/dev/null 2>&1
}

run_with_claude() {
  exec "$DOPPLER_BIN" run --project pleasurai --config dev -- \
    claude -p \
      --no-session-persistence \
      --dangerously-skip-permissions \
      --mcp-config "$REPO_ROOT/.mcp.json" \
      -- \
      "$PROMPT"
}

run_with_codex() {
  local codex_prompt
  codex_prompt="$(cat <<EOF
You are running the Pleasur.AI blog-engine pipeline unattended from Paperclip.

Project root: $REPO_ROOT
Original operator prompt:
$PROMPT

Read CLAUDE.md first, then the relevant .claude/skills/*/SKILL.md file for the slash command in the operator prompt. Treat the .claude skill instructions as the source of truth even though this is Codex rather than Claude Code.

Run noninteractively. Do not ask the user for choices. Use the environment variables already loaded by Doppler. If the prompt is /blog-pipeline or /auto-blog-loop, keep BLOG_AGENT_AUTONOMOUS=1, UNATTENDED=1, BLOG_AGENT_AUTO_PUBLISH=1, and BLOG_AGENT_REVISION_BUDGET=2 unless the environment explicitly overrides them.

Use the deterministic gates exactly as the skill requires, especially scripts/pipeline_gate.py. If Ahrefs MCP tools are unavailable in this Codex process, use the Ahrefs REST API with AHREFS_API_KEY as allowed by CLAUDE.md. Save every stage output to content-pipeline/ before reporting completion.
EOF
)"

  exec "$DOPPLER_BIN" run --project pleasurai --config dev -- \
    codex -a never exec \
      --ephemeral \
      -C "$REPO_ROOT" \
      -s danger-full-access \
      "$codex_prompt"
}

RUNNER="${BLOG_AGENT_RUNNER:-auto}"
case "$RUNNER" in
  claude)
    if ! claude_is_headless_ready; then
      echo "ERROR: BLOG_AGENT_RUNNER=claude but Claude is not authenticated for noninteractive use." >&2
      exit 1
    fi
    run_with_claude
    ;;
  codex)
    if ! codex_is_ready; then
      echo "ERROR: BLOG_AGENT_RUNNER=codex but codex CLI is not available." >&2
      exit 1
    fi
    run_with_codex
    ;;
  auto)
    if claude_is_headless_ready; then
      run_with_claude
    elif codex_is_ready; then
      run_with_codex
    else
      echo "ERROR: neither noninteractive Claude nor Codex is available." >&2
      exit 1
    fi
    ;;
  *)
    echo "ERROR: BLOG_AGENT_RUNNER must be one of: auto, claude, codex." >&2
    exit 64
    ;;
esac
