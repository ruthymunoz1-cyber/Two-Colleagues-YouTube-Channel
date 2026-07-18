#!/usr/bin/env python3
"""Build downloadable, paste-ready Character Sheet and Voice Casting docs
for Maria & James from restaurant-track/characters/character-lab-entries.md.

Character Sheet fields match the RAMP studio's ACTUAL Character Lab form,
verified against the studio's own source (js/app.js), not guessed:
Name, Age, Gender/identity, Ethnicity/ancestry, Skin tone (Monk swatch),
Undertone (single-select dropdown), Hair texture (single-select dropdown),
Hair style (dropdown - its "custom (type below)" option is a studio bug,
no text box appears), Hair color, Eyes, Face details, Build, Signature
wardrobe, Vibe/personality, Reference photo. There is no free-text "paste
one big description" field anywhere in the form.
"""
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor

OUT_DIR = Path("/home/user/Two-Colleagues-YouTube-Channel/restaurant-track/characters")


def base_doc(title):
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    doc.add_heading(title, level=1)
    return doc


def field(doc, label, value, note=None):
    p = doc.add_paragraph()
    r = p.add_run(f"{label}: ")
    r.bold = True
    p.add_run(value)
    if note:
        p2 = doc.add_paragraph()
        r2 = p2.add_run(note)
        r2.italic = True
        r2.font.size = Pt(9)
        r2.font.color.rgb = RGBColor(0x66, 0x66, 0x66)


def warning_block(doc, heading, text):
    doc.add_heading(heading, level=3)
    p = doc.add_paragraph(text)
    for run in p.runs:
        run.font.color.rgb = RGBColor(0xB0, 0x3A, 0x2E)
    return p


# ---------------- Character Sheet doc ----------------
doc = base_doc("Character Sheet — Maria & James")
doc.add_paragraph(
    "Field values for the RAMP studio's actual Character Lab form (verified against the "
    "studio's source code, not guessed). Enter one value per field, in the order shown."
)

warning_block(
    doc,
    "Before you start — two things about the real form",
    "1) Undertone and Hair texture are single-select dropdowns — pick exactly ONE value from "
    "each, not a combination. 2) The Hair Style dropdown's \"custom (type below)\" option is a "
    "studio bug: no text box actually appears. None of its presets (all natural/textured "
    "Black hairstyling terms — afro, braids, locs, twists, bantu knots, silk press) fit a low "
    "bun or a short professional cut anyway. Workaround used below: pick any preset for that "
    "dropdown (it won't matter) and the REAL hairstyle instruction is written into the Face "
    "details field instead, which is free text."
)

doc.add_heading("Maria — Restaurant Server (learner proxy)", level=2)
for label, value, note in [
    ("Name", "Maria", None),
    ("Age", "Late 20s (27)", None),
    ("Gender / identity", "woman", None),
    ("Ethnicity / ancestry", "Latina — Mexican heritage", None),
    ("Skin tone", "Click swatch 5 on the Monk Skin Tone row", None),
    ("Undertone (dropdown)", "olive", "Pick this one value only — do not also type \"warm-neutral.\""),
    ("Hair texture (dropdown)", "Loose curls (3A)",
     "Closest literal match to \"defined waves / loose curls.\" If a render looks too tightly "
     "curled, switch this one dropdown value to \"Wavy (2A–2C)\" and regenerate."),
    ("Hair style (dropdown)", "protective updo",
     "CORRECTED from an earlier \"long layers\" pick: confirmed live in Maria's first compiled "
     "token that \"long layers\" produces a literal contradiction against the Face details bun "
     "instruction (the compiler stitches both into one sentence, so they visibly fight). "
     "\"Protective updo\" is the only preset whose literal meaning (hair pulled up) agrees with "
     "\"low bun\" instead of fighting it."),
    ("Hair color", "dark brown", None),
    ("Eyes", "dark brown, alert, warm", None),
    ("Face details", "Round-oval face, soft features, expressive brows, smile lines. Hair worn in "
                      "a practical low bun with a few loose strands at the temples (work-day "
                      "realism).",
     "This field is carrying the real hairstyle instruction — see bug note above."),
    ("Build", "Average height, average build — on-her-feet-all-shift posture", None),
    ("Signature wardrobe",
     "Fitted black polo, black bistro server apron (waist-length) with order pad and pen in the "
     "pocket, small name tag reading MARIA on the right chest, black slacks, comfortable black "
     "work shoes, small stud earrings only", None),
    ("Vibe / personality",
     "Warm, hardworking, quietly determined — confidence visibly grows across episodes", None),
    ("Reference photo", "None yet — leave blank. Generate from these fields, then the approved "
                         "portrait becomes the reference for future uploads.", None),
]:
    field(doc, label, value, note)

warning_block(
    doc,
    "Lighting note",
    "At Monk 5, the Lab's deep-skin exposure guidance will NOT auto-apply (it only triggers at "
    "deeper tones). Watch for the opposite drift: AI models tend to wash olive skin toward "
    "generic pale pink. If a portrait comes out lighter or pinker than intended, add this to the "
    "Face details field and regenerate before approving: \"medium olive skin tone, olive "
    "undertone, no pink shift.\""
)

doc.add_heading("James — Restaurant Manager (mentor)", level=2)
for label, value, note in [
    ("Name", "James", None),
    ("Age", "Mid 40s (45)", None),
    ("Gender / identity", "man", None),
    ("Ethnicity / ancestry", "White (US)", None),
    ("Skin tone", "Click swatch 3 on the Monk Skin Tone row", None),
    ("Undertone (dropdown)", "neutral", None),
    ("Hair texture (dropdown)", "Straight (1A–1C)",
     "Closest literal match to \"straight, slight body.\""),
    ("Hair style (dropdown)", "long layers",
     "Try this first; if the length reads wrong against \"short, neat, professional\" in Face "
     "details, switch to \"short natural afro\" instead — see Maria's confirmed contradiction "
     "bug above. No preset actually fits a short professional cut; check his Master portrait "
     "carefully before locking."),
    ("Hair color", "dark brown with graying at the temples", None),
    ("Eyes", "gray-blue, steady, crow's feet when he smiles", None),
    ("Face details",
     "Rectangular, lightly lined face (forehead and smile lines), friendly lived-in look, "
     "clean-shaven. Hair short, neat, professional, with graying temples — this is a locked "
     "identity feature; do not let generations \"youthen\" him or remove the gray.",
     "This field is carrying the real hairstyle instruction — see bug note above."),
    ("Build", "Tall (around 6'0\"), broad-shouldered, average build", None),
    ("Signature wardrobe",
     "Dark charcoal button-down with sleeves rolled to the forearm, manager badge on a black "
     "lanyard, dark jeans-cut slacks, brown leather belt, wristwatch", None),
    ("Vibe / personality", "Steady, encouraging, dry humor — the calmest person in every room",
     None),
    ("Reference photo", "None yet — leave blank. Generate from these fields, then the approved "
                         "portrait becomes the reference for future uploads.", None),
]:
    field(doc, label, value, note)

doc.add_heading("Confirmed Workflow Order (from the live app)", level=2)
doc.add_paragraph(
    "1) Create character. 2) Hit \"Master portrait\" first — one image, cheap to redo. Check "
    "the skin tone (watch for pink drift on Maria) and confirm the hairstyle reads correctly "
    "before spending on the full sheet. 3) Only once that looks right, hit \"Generate character "
    "sheet (all angles)\" — that's the real multi-angle turnaround reference everything else "
    "anchors to. 4) Approve and store. Skip \"Create a language/culture variant\" for now — "
    "that's the Spanish/French track for Month 3+."
)

doc.add_heading("Combined Two-Character Scene String", level=2)
doc.add_paragraph(
    "For scene prompts featuring both characters together (outside the Lab, e.g. in the Image "
    "or Video Studio's scene prompt field), paste this:"
)
p = doc.add_paragraph(
    "Maria: adult woman, late 20s, medium olive skin, dark hair in a low bun, brown eyes, black "
    "server apron over black polo, name tag. James: adult man, 40s, light-medium skin, short dark "
    "hair graying at the temples, dark button-down shirt with rolled sleeves, manager badge on "
    "lanyard."
)
p.paragraph_format.space_after = Pt(12)

doc.add_heading("Entry Checklist", level=2)
for item in [
    "Enter Maria in Character Lab (all fields above) -> Create character",
    "Enter James in Character Lab (all fields above) -> Create character",
    "Generate + approve each portrait; regenerate with the pink-shift fix if Maria's tone drifts",
    "Generate both turnaround sheets -> approve -> store",
    "Pin each character's seed once approved",
    "Run the test clip (menu hand-off) using both sheets -> score against the brief",
    "Save \"restaurant\" location set in Location Scout",
]:
    doc.add_paragraph(item, style="List Bullet")

doc.save(OUT_DIR / "RAMP_CharacterSheet_MariaJames.docx")
print("wrote RAMP_CharacterSheet_MariaJames.docx")


# ---------------- Voice Casting doc (unchanged structure - no reported issues) ----------------
doc2 = base_doc("Voice Casting — Maria & James")
doc2.add_paragraph(
    "Voice direction for the RAMP studio Voice Studio. James needs one voice actor covering "
    "three directed registers — never cast a third voice."
)

doc2.add_heading("Maria — Server", level=2)
for label, value in [
    ("Register", "Warm, medium pitch. Slightly careful pacing early in the series, more fluid "
                  "and confident by Video 5"),
    ("Delivery style", "Warm teacher"),
    ("Special variant needed", "A believable \"sick voice\" for Video 4 — hoarse but fully "
                                "intelligible, not mumbled"),
    ("Optional accent note", "A light, authentic Spanish-accent inflection is welcome — never "
                              "played for comedy"),
    ("Voice ID (fill in once cast)", "____________________"),
]:
    field(doc2, label, value)

doc2.add_heading("Casting search prompt", level=3)
doc2.add_paragraph(
    "Search for: a warm, natural female voice in her late 20s with a light, authentic Spanish "
    "accent, medium pitch, capable of a careful/thoughtful early-series delivery that grows more "
    "fluid and confident, plus a hoarse-but-intelligible \"sick\" variant for one episode."
)

doc2.add_heading("James — Manager", level=2)
for label, value in [
    ("Base register", "Lower-medium pitch, unhurried, warm authority"),
    ("Delivery style", "Warm teacher (mentor mode is the default)"),
    ("Register 1 — Mentor (default)", "Steady, encouraging"),
    ("Register 2 — Role-play (fast customer / angry customer / chef)",
     "Natural fast native speaking speed, real heat and urgency without becoming cartoonish"),
    ("Register 3 — Manager-on-the-phone (Video 4)", "Calm, brief, morning-quiet"),
    ("Casting rule", "ONE voice actor covers all three registers via pace/pitch direction — the "
                      "running joke across the series is that it's always James"),
    ("Voice ID (fill in once cast)", "____________________"),
]:
    field(doc2, label, value)

doc2.add_heading("Casting search prompt", level=3)
doc2.add_paragraph(
    "Search for: a male voice in his mid 40s, lower-medium pitch, warm and unhurried authority as "
    "a default mentor register, with demonstrated range to also deliver a fast, heated (but not "
    "cartoonish) customer/chef role-play register and a calm, brief, early-morning phone register."
)

doc2.save(OUT_DIR / "RAMP_VoiceCasting_MariaJames.docx")
print("wrote RAMP_VoiceCasting_MariaJames.docx")
