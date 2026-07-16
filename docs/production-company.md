# The Production Company — How the Agent Team Works

Nine roles, defined as Claude Code agents in [`.claude/agents/`](../.claude/agents/). Any Claude session opened on this repo can dispatch them. One rule above all others: **nothing is published without Ruthy's explicit approval — ever.** The agents' job is to make sure there is always finished, approved-ready work waiting for that approval, never to skip it.

## The roster

| Agent | Role | Runs when |
|-------|------|-----------|
| `showrunner` | Coordinates the cycle, maintains the board, assembles Ruthy's approval packets | Weekly cycle + on demand |
| `scriptwriter` | Drafts full episode scripts in the channel format | Board needs scripts |
| `script-editor` | Rule compliance, B1–B2 level, runtime, continuity, AI-tell removal | After every draft/revision |
| `scene-director` | Approved script → shot list + Kling prompts + cost estimate | After Gate 1 |
| `location-scout` | Reusable setting library + continuity | With scene-director |
| `sound-designer` | Per-episode mix sheet (beds, silence windows, voice direction) | With scene-director |
| `seo-packager` | Title/description/tags/thumbnail brief/chapters/`.srt` check | Episode composed |
| `social-producer` | Cuts Shorts/Reels/TikToks/Stories WITH baked captions + weekly social calendar | After Gate 2 |
| `community-manager` | Weekly digest: comment triage, drafted replies, community-post drafts, topic mining | Weekly (post-launch) |

## The pipeline (per episode)

```
topic backlog
   → scriptwriter drafts → script-editor passes
   → ═══ GATE 1: RUTHY APPROVES SCRIPT ═══  (scripts always delivered as files to read)
   → scene-director + location-scout + sound-designer (parallel)
   → generation & composition in the RAMP studio (cost estimate approved first if >$60)
   → seo-packager builds the publish package
   → ═══ GATE 2: RUTHY APPROVES FINAL CUT + PACKAGE ═══
   → Ruthy uploads & publishes on YouTube (manual, always)
   → social-producer cuts the vertical clip set (captions baked in) + calendar
   → Ruthy posts/schedules social from the prepared set
   → community-manager mines the response into next episodes (weekly)
```

**Caption rule, both directions:** main episodes = never burned in (`.srt` upload only) · social clips = ALWAYS burned in (muted autoplay). Both are locked.

**What social/community agents can and can't automate (honest boundary):** they prepare everything — rendered clips, captions, post copy, reply drafts, community-post drafts — but no tool here can post to YouTube/TikTok/Instagram or send replies. Ruthy (or a scheduler like YouTube Studio's built-in scheduling / Meta Business Suite, fed with the prepared set) does the actual posting. In practice this is ~15 minutes of pasting per week, and it doubles as the final human check.

Two gates, both Ruthy's. Everything between the gates is autonomous. Agents record gate decisions on the production board; an unrecorded approval doesn't exist.

## The production board

Lives at `restaurant-track/production/production-board.md`. One row per episode:

```
| Ep | Title | State | Cost est. | Gate 1 (script) | Gate 2 (final) | Publish date |
```

States: `idea → drafted → editor-passed → SCRIPT APPROVED → assets-in-progress → composed → PACKAGE READY → published`

## Release calendar & buffer policy

- **Launch week:** all 5 launch episodes released across the week (e.g., Mon/Tue/Wed/Thu/Fri or Mon/Wed/Fri + 2) — the binge-ready shelf is the point; Video 5's callbacks reward watching in order.
- **Ongoing: Mon / Wed / Fri, one episode each** (3/week per the handoff).
- **Buffer rule (what makes 3/week sustainable):** the queue of episodes past Gate 2 must never drop below **6 (two weeks of cadence)**. The showrunner counts the buffer at every cycle and starts new scripts when it thins.
- **Degrade gracefully, never rush:** if the buffer falls below 3, the calendar drops to Mon/Fri (2/week) until it recovers. A weaker episode hurts the channel more than a slower week.
- **Ruthy's weekly touch:** one review session per week is enough at steady state — approve scripts (Gate 1) and finished packages (Gate 2) in a single sitting. The agents batch everything to make that session short.

## Scheduling (to activate AFTER the test clip passes)

A weekly Routine fires a session on this repo: *"Run the showrunner's weekly cycle: check the board, refill the buffer, prepare Ruthy's approval packet."* Output lands as commits + files delivered to Ruthy; nothing external happens. Not yet armed — the pipeline needs its physical assets first (turnaround sheets, test-clip verdict, voice IDs). Arming it is a one-line ask once those exist.

## Cost picture at steady state (studio registry prices)

| Item | Per episode | 3/week |
|------|------------|--------|
| Video generation (Kling v3 Pro, ~3–5 min unique footage + retries) | ~$30–55 | ~$90–165 |
| Lip sync ($0.06/s on talking closeups) | ~$5–10 | ~$15–30 |
| Voiceover (ElevenLabs creator tier) | — | ~$5–22/mo flat |
| Ambient beds, whiteboard recap, mixing, sequencing, captions | ~$0 (client-side / one-time) | ~$0 |
| **Total** | **~$35–65** | **~$105–195/week** |

Scripts, scene plans, mix sheets, SEO packages: $0 marginal cost — which is why the buffer is kept in *approved scripts* generously and in *composed video* frugally.
