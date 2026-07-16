# Test Clip Brief — Production Gate

**Purpose:** Validate the realistic-cinematic approach on a 15–30 second clip **before** committing a full episode. This is the #1 next step in the handoff and the gate for everything downstream.

**Why:** A prior full-AI character video attempt produced detached body parts and missing furniture/environment. Realistic + cinematic + two characters + physical object interaction is the highest-risk combination for that failure. This clip deliberately reproduces that combination at minimal cost.

## The Test

One 15–30 second clip: **the manager hands the server a menu across the counter, the server takes it and opens it.** A single simple hand-off of a single object — the minimal version of exactly what full episodes will require constantly.

### Draft Generation Prompt

```
Realistic cinematic video, warm restaurant interior during pre-shift prep, soft natural
window light. Two people at the service counter. Maria: adult woman, late 20s, warm
brown skin, dark hair in a low bun, brown eyes, black server apron over black polo,
name tag. James: adult man, 40s, light-medium skin, short dark hair graying at the
temples, dark button-down shirt with rolled sleeves, manager badge on lanyard.
James picks up a menu from the counter and hands it to Maria. Maria takes the menu
with both hands and opens it, looking down at it. Static camera, medium two-shot,
no camera movement. Natural body mechanics, both characters fully in frame.
```

(Character descriptions are the DRAFT proposals from `../characters/duo-proposals.md` — fine for the test; lock before full production.)

## Pass / Fail Checklist

Watch frame-by-frame at the hand-off moment. **Any one failure = FAIL.**

- [ ] Both characters have correct, attached anatomy for the full clip (hands, arms, faces)
- [ ] The menu exists continuously — it doesn't appear, vanish, duplicate, or morph
- [ ] The hand-off reads as one object passing between two people's hands
- [ ] The counter and background furniture remain present and stable
- [ ] Both characters remain visually consistent start-to-finish (clothing, hair, face)
- [ ] No extra limbs, phantom hands, or merged bodies at the interaction moment

## Outcomes

**PASS →** Lock the cinematic approach. Proceed to reference-image lock and Video 1 production per the script in `../video-01-taking-orders/`.

**FAIL →** Fall back to the still-image format (the handoff's designated fallback, which vidIQ flagged as the more reliable standard for faceless channels):

- Illustrated character cards (consistent still images per character/pose)
- Gentle pan/zoom animation over the cards
- Dual AI voiceover carries the dialogue (unchanged from the cinematic plan)
- Real B-roll for restaurant environment shots
- Animated whiteboard vocabulary + captions (unchanged)

Note: the Video 1 script is written to be **format-agnostic** — dialogue, whiteboard cues, and recap segment work identically in either format; only the scene-direction lines change.

## Result Log

| Date | Tool/model | Result | Notes |
|------|-----------|--------|-------|
| _pending_ | | | |
