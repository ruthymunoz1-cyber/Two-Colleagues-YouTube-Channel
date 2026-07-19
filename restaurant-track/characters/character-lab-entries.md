# Character Lab Entries — Maria & James

Field-by-field values matched to the **actual RAMP studio Character Lab form** (verified against the studio's source, `js/app.js`, July 2026 — not guessed). Enter these once, generate each character's **turnaround sheet**, and the Lab's consistency token + pinned seed will anchor them across every episode.

**Status:** Ready to enter. Names locked (Ruthy, July 2026). Final look still subject to the test-clip verdict (cinematic-realistic vs. illustrated fallback) — these entries work for both; only the Lab's style setting changes.

## ⚠️ Two things about the real form (corrected from an earlier draft of this doc)

1. **Undertone and Hair texture are single-select dropdowns, not free text.** You must pick exactly ONE value from each list — you can't combine two (e.g., "olive" alone, not "olive / warm-neutral"). The full option lists are below so you're not guessing.
2. **"Hair style" → "custom (type below)" is a studio bug — there is no text box that appears.** It's a dropdown (`<select>`) with that literal string as one of its options; the studio never wired up a text field for it. None of the preset options (they're all natural/textured Black hairstyling terms — afro, braids, locs, twists, bantu knots, silk press) fit either Maria's low bun or James's short professional cut anyway. **Workaround:** pick any preset (it barely matters, since it's not the real instruction) and put the actual hairstyle description in the **Face details** field instead, which is free text. Each character's entry below shows exactly what to type there.
3. **There is no single "paste one big paragraph" field anywhere in the form.** Every field is separate. (An earlier version of this doc offered a "consolidated description" block — that doesn't apply to this form and has been removed below.)

Confirmed exact field list, in order, from the live app: Name · Age · Gender/identity · Ethnicity/ancestry (optional) · Skin tone (Monk scale, click a swatch) · Undertone (dropdown) · Hair texture (dropdown) · Hair style (dropdown, buggy) · Hair color (free text) · Eyes (free text) · Face details (free text) · Build (free text) · Signature wardrobe (free text) · Vibe/personality (free text) · Reference photo (optional upload).

---

## Character 1 — Maria (Restaurant Server, learner proxy)

| Character Lab field | Exact value to enter |
|---|---|
| Name | Maria |
| Age | Late 20s (27) |
| Gender / identity | woman |
| Ethnicity / ancestry | Latina — Mexican heritage |
| Skin tone (Monk scale, click swatch) | **5** |
| Undertone (dropdown — pick ONE) | **olive** |
| Hair texture (dropdown — pick ONE) | **Loose curls (3A)** — closest literal match to "defined waves/loose curls." If the render looks too curly, fall back to "Wavy (2A–2C)." |
| Hair style (dropdown) | **protective updo** — CORRECTED from an earlier "long layers" pick. Confirmed live in Maria's first compiled token: "long layers" produced a literal contradiction against the Face details bun instruction ("...hair styled as long layers... Hair worn in a practical low bun...") — the compiler stitches both into one sentence, so they visibly fight. "Protective updo" is the only preset whose literal meaning (hair pulled up) agrees with "low bun" instead. |
| Hair color (free text) | dark brown |
| Eyes (free text) | dark brown, alert, warm |
| Face details (free text) | **Round-oval face, soft features, expressive brows, smile lines. Hair worn in a practical low bun with a few loose strands at the temples (work-day realism).** *(the actual hairstyle instruction lives here, per the bug workaround)* |
| Build (free text) | Average height, average build — on-her-feet-all-shift posture |
| Signature wardrobe (free text) | Fitted black polo, black bistro server apron (waist-length) with order pad and pen in the pocket, small name tag reading MARIA on the right chest, black slacks, comfortable black work shoes, small stud earrings only |
| Vibe / personality (free text) | Warm, hardworking, quietly determined — confidence visibly grows across episodes |
| Reference photo | None yet — generate from this entry, then the approved portrait becomes the reference |

**Lighting note:** at Monk 5 the Lab's deep-skin exposure guidance won't auto-apply (it triggers at deeper tones only). Watch generations for the opposite drift instead: AI models tend to wash olive tones toward generic pale-pink — if the portrait comes out lighter or pinker than intended, add "medium olive skin tone, olive undertone, no pink shift" to the Face details field and regenerate before approving/pinning the seed.

### Voice (Voice Studio)

- Register: warm, medium pitch; slightly careful pacing early in the series, more fluid by Video 5
- Delivery style picker: **warm teacher**
- Needs a believable "sick voice" variant for Video 4 (hoarse but intelligible)
- Optional: a light Spanish-accent inflection — authentic to the audience, never comedic
- Once chosen, record the voice ID here: `____________`

---

## Character 2 — James (Restaurant Manager, mentor)

| Character Lab field | Exact value to enter |
|---|---|
| Name | James |
| Age | Mid 40s (45) |
| Gender / identity | man |
| Ethnicity / ancestry | White (US) |
| Skin tone (Monk scale, click swatch) | **3** |
| Undertone (dropdown — pick ONE) | **neutral** |
| Hair texture (dropdown — pick ONE) | **Straight (1A–1C)** — closest literal match to "straight, slight body" |
| Hair style (dropdown) | try "long layers" first; if the length reads wrong against "short, neat, professional" in Face details, switch to "short natural afro" instead — see Maria's confirmed contradiction bug above. No preset actually fits a short professional cut; watch his Master portrait carefully before locking. |
| Hair color (free text) | dark brown with graying at the temples |
| Eyes (free text) | gray-blue, steady, crow's feet when he smiles |
| Face details (free text) | **Rectangular, lightly lined face (forehead and smile lines), friendly lived-in look, clean-shaven. Hair short, neat, professional, with graying temples — this is a locked identity feature; do not let generations "youthen" him or remove the gray.** *(the actual hairstyle instruction lives here, per the bug workaround)* |
| Build (free text) | Tall (around 6'0"), broad-shouldered, average build |
| Signature wardrobe (free text) | Dark charcoal button-down with sleeves rolled to the forearm, manager badge on a black lanyard, dark jeans-cut slacks, brown leather belt, wristwatch |
| Vibe / personality (free text) | Steady, encouraging, dry humor — the calmest person in every room |
| Reference photo | None yet — generate from this entry, then the approved portrait becomes the reference |

### Voice (Voice Studio)

- Register: lower-medium pitch, unhurried, warm authority
- Delivery style picker: **warm teacher** (mentor mode) — but he needs THREE registers:
  1. **Mentor** (default) — steady, encouraging
  2. **Fast customer / angry customer / chef** (role-play in Videos 1–3) — natural fast native speed, heat without cartoonishness
  3. **Manager-on-the-phone** (Video 4) — calm, brief, morning-quiet
- Casting rule: ONE voice that can do all three (slight pace/pitch treatment for role-play mode is acceptable) — never a third voice actor; the joke is that it's always James
- Once chosen, record the voice ID here: `____________`

---

## Shared production settings

- **Seeds:** auto-assigned by the Lab on character creation (no separate "pin" button observed — creation itself appears to lock it). Record here — Maria: `482784` (assigned 2026-07-18) · James: `______`
- **Workflow order confirmed from the live app:** create character → generate **Master portrait** (single image, cheap to redo) → check skin tone + hairstyle → only then **Generate character sheet (all angles)** (the real turnaround reference) → approve/store. Don't jump straight to the full sheet — the master portrait is the cheap checkpoint.
- **Maria's Master portrait, reviewed 2026-07-18: APPROVED.** Skin tone holds true olive (no pink drift). "Protective updo" fix confirmed working visually — hair reads as an actual bun, not loose layers. Proceeding to full turnaround sheet.
- **✅ MARIA FINAL LOCK — 2026-07-19:** Turnaround sheet #3 (regenerated with Master Portrait as reference) + standalone face-closeup reference BOTH APPROVED. Complete 5-angle body set + 2 face closeups verified clean. Hands: 5 digits each angle, no warping/merging. Face/ear anatomy consistent across all views. Skin tone (olive/Monk 5) locked. Hair (low bun) and wardrobe (black polo, apron, MARIA name tag, shoes) consistent throughout. Ready for production. **Noted:** back-view panel crops at knee (missing full feet) — cosmetic framing issue, lower priority than anatomy; acceptable for composition reference.
- **Hard rule — hands:** the Master portrait does NOT show hands (by design — it's a face/skin/hair check only) and must never be used alone as the reference for object-interaction scenes (menu hand-offs, holding pad/pen). Only the full turnaround sheet (5 full-body angles, arms at sides) actually establishes hand appearance. **Before approving/pinning any character's turnaround sheet, check hands specifically in every full-body angle** — correct finger count, no merging/warping — this is the exact failure mode the original risk flag warns about.
- **⚠️ Confirmed tool limitation — Master Portrait ≠ Turnaround Sheet by default.** Verified in the studio's own source (`js/app.js`): the two are separate generations that share a seed and description but use different prompts/compositions (chest-up single portrait vs. 5-panel full-body grid) — a matching seed alone does NOT guarantee the same face across such different shots. The Master Portrait flow does not save its result onto the character; it only alerts you to manually download it from the Gallery and re-upload it as the character's Reference Photo. **If you skip that manual step (easy to miss), the Turnaround Sheet will render a different-looking face than the portrait you approved.** Live example: Maria's approved master portrait and her generated turnaround sheet showed different faces (2026-07-18) for exactly this reason.
  - **To make them match:** download the approved master portrait from the Gallery, recreate the character with that image attached to "Reference photo" at creation (no re-upload option exists on an already-created character), then regenerate the sheet.
  - **Simpler alternative:** skip matching the discarded portrait — once a turnaround sheet exists, it automatically becomes the reference for everything generated after it. Approve the sheet's own face (checking self-consistency across its 5 angles + hands) and treat that as the character's official locked look.
- **Turnaround sheet #1 hands check, 2026-07-18: REJECTED.** Close crop of the profile-view hand showed an ambiguous extra shape near the finger base (possible 6th digit) and an oddly bent/wide finger next to the body — classic AI hand artifact. Also: Ruthy preferred the Master Portrait's face over this sheet's face.
- **Decision (2026-07-18): recreating Maria with the approved Master Portrait attached as Reference Photo.** Steps: (1) save the approved master portrait from the Gallery, (2) delete the current Maria (seed 162852, mismatched sheet), (3) recreate with identical fields — age 27, woman, Latina/Mexican heritage, skin tone 5, undertone olive, hair texture Loose curls (3A), hair style protective updo, hair color dark brown, eyes dark brown/alert/warm, Face details with the low-bun instruction, Build, Signature wardrobe, Vibe — but this time attach the saved portrait via "Choose File" under Reference photo before creating, (4) go straight to "Generate character sheet (all angles)" — refImage present switches this to the anchored edit model automatically, (5) re-check hands on the result before approving.
- **⚠️ Standing rule (2026-07-18): face/ear closeups are REQUIRED production material, not cosmetic.** Every episode's whiteboard recap segment is a face-forward, close-in shot of both characters delivering Q&A — this is one of the most-used framings in the series, not an edge case. Face closeups must be checked with the same rigor as hands (see hard rule above) before being treated as good — for every character, including James and any future cast. A flawed face/ear closeup is NOT low-risk just because it's not a full-body shot.
- **Turnaround sheet #2 (with reference photo) check, 2026-07-18:**
  - ✅ Face now consistent across all views, matches the approved Master Portrait — the reference-photo fix worked.
  - ✅ Hands: checked 3 tight crops (front-view hand, two profile/side-area hands) — all show correct 5-digit anatomy, no repeat of the 6th-finger artifact from sheet #1.
  - ❌ **NEW issue — panel compositing bleed.** The back-view panel and one face-closeup panel overlap/bleed into each other: the back view's head is obscured by an intruding face closeup, and that same closeup has a stray leg/hand fragment cut into its top. Neither panel is cleanly extractable as-is. This is also what read as "her head is a little off" — same root cause, not a separate defect.
  - ❔ Earrings: both closeups show small stud earrings, no obvious style mismatch spotted, but not confirmed with full certainty from the available crops.
  - **REJECTED — regenerating again** (same character, same reference photo, re-click "Generate character sheet"). Re-check on the next attempt: clean panel separation (no bleed) + hands fresh, since each regeneration is a new roll.
- **Sheet #3 individual closeups review, 2026-07-18:** panel-bleed issue resolved (no overlap this time); one framing inconsistency found (back-view panel cropped shorter than the other 4, missing feet — cosmetic, low priority); hands re-checked clean across 3 tight crops; earring style inconsistent in one extreme close-up vs. 6 other consistent views (simple stud everywhere else); **that same closeup also shows incomplete/ambiguous ear anatomy on both sides — no clear helix visible, reads as under-rendered rather than hair-covered.** This closeup rejected as a locked reference.
- **Extra face close-up attempt, 2026-07-18: ear anatomy excellent (best yet — full helix + lobe correctly formed), but earring shows TWO studs instead of the spec's single stud.** Not used to replace the already-approved reference below — logged for awareness only. If chasing a "best of both" version later, try adding "single stud earring only, not double" explicitly to the Face details field before regenerating.
- **✅ Standalone "Face close-up" single-angle shot, 2026-07-18: APPROVED as Maria's face-closeup reference.** Visible earlobe curve on the clearer ear (anatomically real, not floating); other ear appropriately covered by loose hair strands per the styling spec, nothing wrong where visible; both earrings consistent simple studs — no repeat of the two-part anomaly. Face/skin/hair all still consistent with the locked look. Minor incidental note: name tag now shows a small logo icon above "MARIA" (previous versions were plain text) — harmless drift, Ruthy's call whether to keep it. **Action:** save this image and keep it on hand to manually feed as a reference when composing recap segments later (per the standing rule — not part of the automatic reference chain).
- **Turnaround sheets (the consistency anchor):** generate for BOTH characters before any scene generation — full body ×5 angles + face close-ups, identical wardrobe. Every scene generation must reference the sheet, not just the text token. This is the direct mitigation for the detached-limbs failure in the risk flag.
- **Two-shot rule:** scenes with both characters use BOTH turnaround sheets as references, and physical-object interactions (menu/plate hand-offs) go through the test-clip gate first (`../test-clip/test-clip-brief.md`).
- **Setting (Location Scout):** build one reusable "warm casual American restaurant" location set — dining floor, service counter/pass, bar corner, back-of-house station, and Maria's small apartment (Video 4). Save as Settings so every episode pulls identical environments.
- **Language variants (Month 3+):** use the Lab's language/culture variant generator off these two masters — Spanish: Yesenia (server) + Señor López (manager); French: Amina/Karim + Monsieur Dubois — per the handoff naming table. Variants are new characters with their own sheets, not re-skins mid-series.

## Entry checklist

- [ ] Enter Maria in Character Lab → generate portrait → approve → pin seed
- [ ] Enter James in Character Lab → generate portrait → approve → pin seed
- [ ] Generate both turnaround sheets → approve → store
- [ ] Run the test clip (menu hand-off) using both sheets → score against the brief
- [ ] Cast both voices in Voice Studio → record voice IDs above
- [ ] Save "restaurant" location set in Location Scout
