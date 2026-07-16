# Sound Design Spec — Restaurant Track

**Principle:** this is a B1–B2 *listening comprehension* channel — ambience creates realism, but **voice clarity always wins**. Ambience sits low under dialogue, and disappears entirely wherever the viewer is supposed to repeat or answer.

## Ambient bed library (generate once, reuse across all episodes)

Generate in the RAMP studio **Sound Library** (Stable Audio, ~$0.03/track, seamless loops — same engine as the built-in "Coffee shop" preset). Custom prompts:

| Loop | Prompt | Used in |
|------|--------|---------|
| Dining floor (service) | "busy casual restaurant dining room ambience, distant murmuring conversations, cutlery and plate clinks, seamless loop, no music, no voices distinguishable" | V1, V2, V5 cold opens/payoffs |
| Dining floor (quiet/pre-shift) | "empty restaurant at morning, quiet room tone, occasional chair movement, distant kitchen hum, seamless loop, no music, no voices" | V1–V3, V5 training scenes |
| Kitchen rush | "professional restaurant kitchen ambience, sizzling, ticket printer, pans, extractor fan hum, seamless loop, no music, no voices" | V3 cold open/payoff |
| Kitchen calm | "restaurant kitchen at prep time, low extractor hum, occasional chopping, seamless loop, no music, no voices" | V3 training scenes |
| Quiet apartment (morning) | "quiet small apartment at early morning, soft room tone, distant city hum through window, seamless loop, no music, no voices" | V4 Maria's side |
| Restaurant (pre-open, office side) | "quiet restaurant back office room tone, distant refrigeration hum, seamless loop, no music, no voices" | V4 James's side, V2 back-of-house |

## Mixing rules (Audio Mixer, per episode)

1. **Dialogue:** always the top layer, full level.
2. **Ambience:** ducked well under voice (~20–25 dB below dialogue). Present enough to feel real; never competing with a phrase a learner is trying to parse.
3. **Ambience OUT completely during:** (a) every KEY PHRASE repetition beat, (b) the entire whiteboard recap quiz — the 3-second answer pauses must be clean silence so viewers hear themselves think, (c) protected emotional lines flagged in the scripts (James's "not angry at YOU" in V2, "that call RAISED my opinion of her" in V4).
4. **Diegetic one-shots stay scripted** (already in the scripts): ticket printer chatter and "Behind!" pan pass (V3), phone ring (V4), door chime and ticking clock (V5). Source from the free libraries linked in Sound Library (Pixabay/Freesound/YouTube Audio Library) rather than generating.
5. **Music:** intro/outro sting only (Music Studio, one reusable channel sting) — no music beds under teaching dialogue, ever. Optional soft bed under the cold-open freeze-frame VO and the outro CTA.
6. **Replace generated-clip audio:** Kling v3 outputs native audio with its clips — **mute it and use our mix** (VO + ambient beds) so sound is consistent across every scene regardless of which clip generated it. Exception: a native clip sound may be kept as a one-shot if it happens to be good (e.g., a plate set-down).
7. **Loudness target:** normalize final mix to YouTube's −14 LUFS; dialogue-driven content should not be limited/crushed — learners use the pause button constantly and clipped consonants hurt comprehension.

## Per-episode cost

6 ambient loops × ~$0.03 = **~$0.18 one-time** for the whole track's bed library; mixing is the browser Audio Mixer ($0). This is effectively free realism.
