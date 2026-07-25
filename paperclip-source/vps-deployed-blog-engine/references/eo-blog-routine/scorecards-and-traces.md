# Scorecards And Traces

This file defines the debugging contract for each article or relaunch. A run is not complete until
the scorecard and skill trace exist, even when the final disposition is no-publish or no-op.

Portfolio-review and measurement runs use the compact artifacts in
`portfolio-improvement-system.md`. A focused relaunch/update child also uses the article manifest
below. Technical or leave/no-op decisions do not need fake article artifacts.

## Required Artifacts

Save these for every run:

- `content-pipeline/run-manifests/{slug}.json`
- `content-pipeline/scorecards/{slug}.md`
- `content-pipeline/traces/{slug}-skill-trace.md`

Create the directories first if they do not exist. Missing directories are not a blocker.

If the slug changes, keep the original keyword in the file frontmatter and use the final slug for
the path.

## Run Manifest Shape

The JSON manifest should be readable by humans and by a future Whiteboard/debug UI.

```json
{
  "slug": "example-slug",
  "keyword": "example keyword",
  "lane": "publish",
  "status": "published | no_publish | blocked | relaunch_shipped | no_op",
  "url": null,
  "author": {
    "name": null,
    "cmsId": null,
    "profileUrl": null,
    "stylePacket": "content-pipeline/2-reference/example-slug-author.md",
    "verifiedLive": false
  },
  "scores": {
    "courseOpportunity": null,
    "businessValue": null,
    "estimatedLinksNeeded": null,
    "contentQuality": null,
    "contagion": null,
    "authorFit": null,
    "visualProof": null,
    "publishReadiness": "fail"
  },
  "visuals": {
    "manifest": "content-pipeline/images/example-slug/manifest.json",
    "coverCandidate": null,
    "ogCandidate": null,
    "roleMix": [],
    "productProof": false,
    "tableOnly": false
  },
  "productMentions": {
    "featureFitMatrix": null,
    "pricingLinksJustified": false,
    "materialMentionsProofLed": false
  },
  "workPackets": {
    "folder": "content-pipeline/task-packets/example-slug",
    "created": [],
    "childIssues": []
  },
  "stages": [
    {
      "id": "0-context",
      "name": "Candidate Selection",
      "status": "pass | fail | skipped | blocked",
      "inputs": [],
      "outputs": [],
      "skillsUsed": [],
      "gateFailures": [],
      "notes": ""
    }
  ],
  "followUps": []
}
```

For existing-content children also record `priorityClass`, raw `businessValue`, `impact`,
`confidence`, `urgency`, `effort`, `evidenceArtifacts`, `baseline`, `measureOn`, and
`measurementWindowDays`.

## Scorecard

Use scores diagnostically. Hard gates still control publish/no-publish.

### Stage Packets

Use `stage-task-map.md`. Record the packet folder and every packet created. If a stage was handled
inside a fresh `blog-pipeline` agent context without a separate packet file, record the agent stage
output path in the stage row and explain why no packet was needed.

If a Paperclip child/follow-up issue is created, add its ID to `workPackets.childIssues` and explain
which stage it unblocked. Do not create multiple child tasks for the same stage at once.

### Course Opportunity

Use the course formula from `course-formula.md`:

```text
Business Value x Traffic Potential / max(1, Estimated Links Needed)
```

This selects candidates. It does not excuse thin content.

### Content Quality

Use `quality-check` and `scales-and-rubrics.md`. Record:

- mechanical score;
- judgment score;
- final score;
- pass/borderline/fail;
- the competitor the article was judged against.

### Contagion Score, 0-10

Use `contagious-why-things-catch-on` when the article needs shares, links, citations, memorable
framing, or a public hook.

```text
Contagion Score =
STEPPS count (0-6)
+ Share/link asset strength (0-2)
+ Story integration (0-1)
+ Headline trigger strength (0-1)
```

STEPPS count:

- Social Currency
- Triggers
- Emotion
- Public
- Practical Value
- Stories

Share/link asset strength:

- 0 = no concrete asset;
- 1 = useful but ordinary checklist/table/framework;
- 2 = original test, data, visual proof, comparison, named framework, or proprietary observation.

Story integration:

- 0 = story can be removed without changing the article;
- 1 = the story carries the point and the product/brand is integral.

Headline trigger strength:

- 0 = keyword-only or generic;
- 1 = honest search fit plus a clear reason to click, save, or share.

Interpretation:

- 0-3: ordinary SEO support asset. Do not promote as linkable.
- 4-6: solid article with one or two shareable hooks.
- 7-10: strong linkable/promotable candidate.

If any Contagious improvement creates a false, unsafe, clickbait, or off-intent claim, force the
Contagion Score to 0 and reject the change.

### Author Fit, 0-5

Use `author-style-and-byline.md`.

- 0: no real author, missing byline, or no author examples.
- 1-2: author exists but voice/sample alignment is weak.
- 3: acceptable house/author fit.
- 4: strong author mimicry without copying.
- 5: excellent author fit plus clear Pleasur.AI point of view.

Publish requires at least 3 and no byline gate failure.

### Visual Proof, 0-5

Use the visual/header/cover checklist.

- 0: missing/broken visuals or text-only post.
- 1-2: decorative visuals only or weak relevance.
- 3: minimum useful visuals pass.
- 4: strong role mix with product proof.
- 5: visuals materially improve comprehension, trust, and conversion.

Publish requires at least 3, unless a documented route exception applies.

### Publish Readiness

Binary result only:

- `pass`: all hard gates pass and live verification passes.
- `fail`: any hard gate fails.

Do not average away a failed live check, missing author, broken cover, unsupported claim, or missing
visual.

## Skill Trace Template

Use this markdown format in `content-pipeline/traces/{slug}-skill-trace.md`.

```markdown
# Skill Trace: {slug}

| Stage | Skill | Mode | Input | Output | Decision Changed | Conflict | Result |
|---|---|---|---|---|---|---|---|
| 0-context | keyword-vet-bid | required | keyword-ideas.csv | 0-context/{slug}.md | yes/no | none | pass/fail |

## Skill Gaps

- None.

## Conflict Resolutions

- None.
```

Mode must be one of:

- required;
- conditional;
- advisory;
- manual_fallback;
- skill_gap.

Never claim a skill was used unless its instructions or output were actually applied.

The markdown trace is a human-readable summary only. The authoritative evidence is the stage JSON
receipt at `content-pipeline/stage-receipts/{run-key}/{stage}.json`, using the schema in
`execution-contract.md`. A publish gate fails when a required receipt is missing, a skill instruction
hash is absent, an artifact path/hash does not verify, or the claimed skill did not change a decision
and lacks a concrete `NOT_APPLICABLE` result.
