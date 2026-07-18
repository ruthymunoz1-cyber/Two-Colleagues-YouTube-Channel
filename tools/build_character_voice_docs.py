#!/usr/bin/env python3
"""Build downloadable, paste-ready Character Sheet and Voice Casting docs
for Maria & James from restaurant-track/characters/character-lab-entries.md.
Each field is its own short paragraph so it's easy to copy one line at a
time into the RAMP studio's Character Lab / Voice Studio fields.
"""
from pathlib import Path

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT_DIR = Path("/home/user/Two-Colleagues-YouTube-Channel/restaurant-track/characters")


def base_doc(title):
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    h = doc.add_heading(title, level=1)
    return doc


def field(doc, label, value):
    p = doc.add_paragraph()
    r = p.add_run(f"{label}: ")
    r.bold = True
    p.add_run(value)


def block_quote(doc, heading, text):
    doc.add_heading(heading, level=3)
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(12)


# ---------------- Character Sheet doc ----------------
doc = base_doc("Character Sheet — Maria & James")
doc.add_paragraph(
    "Paste-ready field values for the RAMP studio Character Lab. "
    "Copy each field into its matching Lab input, or use the single "
    "consolidated paragraph at the end of each character's section if "
    "the Lab takes one free-text description instead."
)

doc.add_heading("Maria — Restaurant Server (learner proxy)", level=2)
for label, value in [
    ("Name", "Maria"),
    ("Age", "Late 20s (27)"),
    ("Race / ethnicity", "Latina — Mexican heritage"),
    ("Skin tone (Monk scale 1-10)", "5 — medium olive (typical Latina tone)"),
    ("Undertone", "Olive / warm-neutral"),
    ("Hair texture", "2C-3A (defined waves / loose curls), dark brown"),
    ("Hair style", "Practical low bun, a few loose strands at the temples (work-day realism)"),
    ("Eyes", "Dark brown, alert, warm"),
    ("Face", "Round-oval, soft features, expressive brows, smile lines"),
    ("Wardrobe (locked, every scene)",
     "Fitted black polo, black bistro server apron (waist-length) with order pad and pen in "
     "pocket, small name tag reading MARIA on the right chest, black slacks, comfortable black "
     "work shoes, small stud earrings only"),
    ("Vibe", "Warm, hardworking, quietly determined — confidence visibly grows across episodes"),
]:
    field(doc, label, value)

block_quote(
    doc,
    "Consolidated description (single paste)",
    "Maria: an adult Latina woman in her late 20s, medium olive skin tone (Monk scale 5) with a "
    "warm-neutral undertone, dark brown hair with a 2C-3A wave/curl texture worn in a practical "
    "low bun with a few loose strands at the temples, dark brown alert warm eyes, a round-oval "
    "face with soft features and smile lines. Wardrobe: fitted black polo, black waist-length "
    "bistro server apron with an order pad and pen in the pocket, a small name tag reading MARIA "
    "on the right chest, black slacks, black work shoes, small stud earrings only. Vibe: warm, "
    "hardworking, quietly determined."
)

block_quote(
    doc,
    "Lighting note",
    "At Monk 5, the Lab's deep-skin exposure guidance will NOT auto-apply (it only triggers at "
    "deeper tones). Watch for the opposite drift: AI models tend to wash olive skin toward "
    "generic pale pink. If a portrait comes out lighter or pinker than intended, add this to the "
    "prompt and regenerate before approving: \"medium olive skin tone, warm-neutral undertone, "
    "no pink shift.\""
)

doc.add_heading("James — Restaurant Manager (mentor)", level=2)
for label, value in [
    ("Name", "James"),
    ("Age", "Mid 40s (45)"),
    ("Race / ethnicity", "White (US)"),
    ("Skin tone (Monk scale 1-10)", "3 — light-medium"),
    ("Undertone", "Neutral"),
    ("Hair texture", "1B (straight, slight body), dark brown with clear graying at the temples"),
    ("Hair style",
     "Short, neat, professional. Graying temples are a locked identity feature — do not let "
     "generations \"youthen\" him"),
    ("Eyes", "Gray-blue, steady, crow's feet when he smiles"),
    ("Face",
     "Rectangular, lightly lined (forehead and smile lines), friendly lived-in face. Clean-shaven "
     "or light stubble — pick ONE at turnaround time and lock it"),
    ("Wardrobe (locked, every scene)",
     "Dark charcoal button-down shirt with sleeves rolled to the forearm, manager badge on a "
     "black lanyard, dark jeans-cut slacks, brown leather belt, wristwatch"),
    ("Vibe", "Steady, encouraging, dry humor — the calmest person in every room"),
]:
    field(doc, label, value)

block_quote(
    doc,
    "Consolidated description (single paste)",
    "James: an adult white man in his mid 40s, light-medium skin tone (Monk scale 3) with a "
    "neutral undertone, straight dark brown hair (1B texture) with clear graying at the temples, "
    "worn short and neat and professional — the graying temples must never be youthened away. "
    "Gray-blue steady eyes with crow's feet when he smiles. A rectangular, lightly lined face "
    "(forehead and smile lines), friendly and lived-in, clean-shaven. Wardrobe: dark charcoal "
    "button-down shirt with sleeves rolled to the forearm, a manager badge on a black lanyard, "
    "dark jeans-cut slacks, a brown leather belt, a wristwatch. Vibe: steady, encouraging, dry "
    "humor, the calmest person in every room."
)

doc.add_heading("Turnaround Sheet Prompt (both characters)", level=2)
doc.add_paragraph(
    "Use the Lab's standard turnaround-sheet template with each character's consolidated "
    "description above substituted in for [CHARACTER DESCRIPTION]:"
)
block_quote(
    doc,
    "Template",
    "Character reference turnaround sheet on a single image: the EXACT same character shown "
    "full-body from five angles side by side — front view, three-quarter left view, left profile, "
    "back view, three-quarter right view — plus a chest-up front close-up and a side-face "
    "close-up. [CHARACTER DESCRIPTION]. Identical face, identical hairstyle, identical outfit and "
    "colors in every view. Neutral relaxed standing pose, arms at sides, plain light-grey "
    "seamless studio background, soft even professional lighting, photorealistic, highly "
    "detailed, no text, no labels, no props."
)

doc.add_heading("Combined Two-Character Scene String", level=2)
doc.add_paragraph("Paste this into any scene prompt that features both characters together:")
block_quote(
    doc,
    "Scene string",
    "Maria: adult woman, late 20s, medium olive skin, dark hair in a low bun, brown eyes, black "
    "server apron over black polo, name tag. James: adult man, 40s, light-medium skin, short dark "
    "hair graying at the temples, dark button-down shirt with rolled sleeves, manager badge on "
    "lanyard."
)

doc.add_heading("Entry Checklist", level=2)
for item in [
    "Enter Maria in Character Lab -> generate portrait -> approve -> pin seed",
    "Enter James in Character Lab -> generate portrait -> approve -> pin seed",
    "Generate both turnaround sheets -> approve -> store",
    "Run the test clip (menu hand-off) using both sheets -> score against the brief",
    "Save \"restaurant\" location set in Location Scout",
]:
    doc.add_paragraph(item, style="List Bullet")

doc.save(OUT_DIR / "RAMP_CharacterSheet_MariaJames.docx")
print("wrote RAMP_CharacterSheet_MariaJames.docx")


# ---------------- Voice Casting doc ----------------
doc2 = base_doc("Voice Casting — Maria & James")
doc2.add_paragraph(
    "Paste-ready voice direction for the RAMP studio Voice Studio. James needs one voice "
    "actor covering three directed registers — never cast a third voice."
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

block_quote(
    doc2,
    "Casting search prompt",
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

block_quote(
    doc2,
    "Casting search prompt",
    "Search for: a male voice in his mid 40s, lower-medium pitch, warm and unhurried authority as "
    "a default mentor register, with demonstrated range to also deliver a fast, heated (but not "
    "cartoonish) customer/chef role-play register and a calm, brief, early-morning phone register."
)

doc2.save(OUT_DIR / "RAMP_VoiceCasting_MariaJames.docx")
print("wrote RAMP_VoiceCasting_MariaJames.docx")
