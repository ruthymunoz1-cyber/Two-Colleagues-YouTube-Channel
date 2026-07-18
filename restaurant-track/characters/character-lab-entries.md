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
| Hair style (dropdown — doesn't matter, see bug note above) | pick "long layers" (least likely to visually fight the real style below) |
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
| Hair style (dropdown — doesn't matter, see bug note above) | pick "long layers" (least likely to visually fight the real style below) |
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
