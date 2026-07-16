# Two Colleagues English — Channel HQ

Production repository for the YouTube channel **Two Colleagues English** (`@TwoColleaguesEnglish`).

> **Channel promise:** "I help working professionals speak English confidently at work by showing realistic office/workplace conversations between two colleagues — not textbook drills."

- **Audience:** Immigrant workers, intermediate English (B1–B2), who can read English but lack speaking confidence in professional settings
- **Format:** Dialogue-based workplace English between two colleagues
- **Current focus:** Restaurant / Hospitality worker-side English (vidIQ breakout score 171x — see handoff)

## Current Status (July 2026)

| Track | Status | Notes |
|-------|--------|-------|
| 🍽️ Restaurant track | **ACTIVE — current priority** | Duo to be designed; test clip required before full production |
| 🏢 Office track (Marcia & Dave) | SHELVED | Resumes on a separate timeline. Do NOT use Marcia & Dave for restaurant content. |
| 🏥 Healthcare track | Planned (Month 2) | Alternating weeks with restaurant |
| 🛒 Retail track | Planned (Month 3+) | Plus Spanish-language variant launch |

## ⚠️ Standing Production Risk

Realistic cinematic AI video with **two characters + physical objects** (menus, plates, trays) is the highest-risk combination for AI generation failures (detached body parts, missing environment — observed in a prior test). **Every new production approach must be piloted with a 15–30 second test clip before a full episode is committed.** Fallback format: still-image character cards + dual voiceover + captions + real B-roll. See [`docs/handoff-2026-07/handoff-v2.md`](docs/handoff-2026-07/handoff-v2.md) — **v2 is current** (v1 kept for history).

**Locked production rules (v2):** whiteboard element appears only in the end-recap segment · no captions burned into visuals (YouTube native toggle only) · vendor is substitutable, constraints are not.

## Repository Map

```
docs/handoff-2026-07/        Source-of-truth handoffs (v2 current; v1 superseded)
skills/two-colleagues-english/  Channel production skill (office track, v2 — current)
skills/archive/              Superseded skill versions
office-track/                Shelved office track (Marcia & Dave) — status + asset pointers
restaurant-track/            ACTIVE: restaurant pivot workspace
  characters/                Restaurant duo — Maria & James (names LOCKED)
  test-clip/                 Test-clip brief (gate before full production)
  video-01-taking-orders/    Full script draft v2
  video-02-angry-customer/   Outline (launch batch)
  video-03-kitchen-english/  Outline (launch batch)
  video-04-calling-in-sick/  Outline (launch batch, new in handoff v2)
  video-05-shift-handover/   Outline (launch batch, new in handoff v2)
```

## Roadmap (from handoff v2 — launch = all 5 videos together, then 3/week)

1. ☐ Generate 15–30s cinematic test clip (duo + single object) — **production gate**
2. 🟡 Design the restaurant duo — names LOCKED (Maria + James); visuals pending test clip
3. ☐ Lock reference images for the new duo
4. 🟡 Full scripts for all 5 launch videos — all 5 drafted, awaiting review
5. ☐ Produce dual voiceovers for the launch batch
6. ☐ Compose all 5 episodes; evaluate against risk flag before launch and 3-videos/week cadence

**Tooling (per v2 caveat):** vidIQ for research/titles/thumbnails scoring; the [RAMP "Ramping It Up" studio](https://github.com/ruthymunoz1-cyber/Ramping-it-up-video-and-content-studio) for character design, video generation, lip sync, voiceover dialogue, whiteboard recap, and assembly.
