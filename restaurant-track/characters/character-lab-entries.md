# Character Lab Entries — Maria & James

Field-by-field values to enter into the **RAMP studio → Character Lab**, matched to the Lab's actual fields (ethnicity, Monk Skin Tone scale, undertone, hair texture 1A–4C, wardrobe, vibe). Enter these once, generate each character's **turnaround sheet**, and the Lab's consistency token + pinned seed will anchor them across every episode.

**Status:** Ready to enter. Names locked (Ruthy, July 2026). Final look still subject to the test-clip verdict (cinematic-realistic vs. illustrated fallback) — these entries work for both; only the Lab's style setting changes.

---

## Character 1 — Maria (Restaurant Server, learner proxy)

| Character Lab field | Value |
|---|---|
| Name | Maria |
| Age | Late 20s (27) |
| Race / ethnicity | Latina — Mexican heritage |
| Skin tone (Monk scale 1–10) | **5** — medium olive (typical Latina tone) |
| Undertone | Olive / warm-neutral |
| Hair texture | **2C–3A** (defined waves/loose curls), dark brown |
| Hair style | Practical low bun, a few loose strands at the temples (work-day realism) |
| Eyes | Dark brown, alert, warm |
| Face | Round-oval, soft features, expressive brows; smile lines |
| Wardrobe (locked, every scene) | Fitted black polo, black bistro server apron (waist-length) with order pad + pen in pocket, small name tag "MARIA" on right chest, black slacks, comfortable black work shoes; small stud earrings only |
| Vibe | Warm, hardworking, quietly determined — confidence visibly grows across episodes |
| Reference photos | None yet — generate from this entry, then the approved portrait becomes the reference |

**Lighting note:** at Monk 5 the Lab's deep-skin exposure guidance won't auto-apply (it triggers at deeper tones only). Watch generations for the opposite drift instead: AI models tend to wash olive tones toward generic pale-pink — if the portrait comes out lighter or pinker than intended, add "medium olive skin tone, warm-neutral undertone, no pink shift" to the prompt and regenerate before approving/pinning the seed.

### Voice (Voice Studio)

- Register: warm, medium pitch; slightly careful pacing early in the series, more fluid by Video 5
- Delivery style picker: **warm teacher**
- Needs a believable "sick voice" variant for Video 4 (hoarse but intelligible)
- Optional: a light Spanish-accent inflection — authentic to the audience, never comedic
- Once chosen, record the voice ID here: `____________`

---

## Character 2 — James (Restaurant Manager, mentor)

| Character Lab field | Value |
|---|---|
| Name | James |
| Age | Mid 40s (45) |
| Race / ethnicity | White (US) |
| Skin tone (Monk scale 1–10) | **3** — light-medium |
| Undertone | Neutral |
| Hair texture | **1B** (straight, slight body), dark brown with clear graying at the temples |
| Hair style | Short, neat, professional; graying temples are a locked identity feature — do not let generations "youthen" him |
| Eyes | Gray-blue, steady; crow's feet when he smiles |
| Face | Rectangular, lightly lined (forehead + smile lines), friendly lived-in face; clean-shaven or light stubble — pick ONE at turnaround time and lock it |
| Wardrobe (locked, every scene) | Dark charcoal button-down with sleeves rolled to the forearm, manager badge on a black lanyard, dark jeans-cut slacks, brown leather belt, wristwatch |
| Vibe | Steady, encouraging, dry humor; the calmest person in every room |
| Reference photos | None yet — generate from this entry, then the approved portrait becomes the reference |

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

- **Seeds:** pin each character's seed in the Lab the moment a portrait is approved; record here — Maria: `______` · James: `______`
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
