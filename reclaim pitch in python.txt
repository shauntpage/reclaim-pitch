from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_zen_deck():
    # 1. Create Presentation
    prs = Presentation()

    # Helper to add a slide with Title, Text, and an Image Placeholder
    def add_zen_slide(title_text, bullet_points, image_instruction=None):
        # Use a blank layout to control everything
        slide = prs.slides.add_slide(prs.slide_layouts[6])

        # A. Title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(1))
        title = title_box.text_frame
        title.text = title_text
        title.paragraphs[0].font.size = Pt(40)
        title.paragraphs[0].font.bold = True
        title.paragraphs[0].font.name = 'Arial'

        # B. Content (Left Side)
        content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.5), Inches(5))
        tf = content_box.text_frame
        tf.word_wrap = True
        
        for point in bullet_points:
            p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(20)
            p.space_after = Pt(14)
            p.level = 0

        # C. Image Placeholder (Right Side)
        if image_instruction:
            # Draw a red rectangle where the image goes
            shape = slide.shapes.add_shape(
                1, # MSO_SHAPE.RECTANGLE
                Inches(5.2), Inches(1.5), Inches(4.5), Inches(5)
            )
            shape.fill.solid()
            shape.fill.fore_color.rgb = RGBColor(255, 200, 200) # Light Red
            shape.line.color.rgb = RGBColor(255, 0, 0)
            
            # Add instruction text inside
            p = shape.text_frame.paragraphs[0]
            p.text = f"INSERT IMAGE HERE:\n\n{image_instruction}"
            p.alignment = PP_ALIGN.CENTER
            p.font.color.rgb = RGBColor(100, 0, 0)

    # --- SLIDE 1: TITLE ---
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = slide.shapes.title
    title.text = "Reclaim"
    subtitle = slide.placeholders[1]
    subtitle.text = "The Operating System for Ownership\n\nShaun Page"

    # --- SLIDE 2: THE CRISIS ---
    add_zen_slide(
        "The Context: Crisis of Control",
        [
            "Stress is up. Trust is down.",
            "Homeowners feel resigned because they feel powerless.",
            "The world is messy, and they lack the tools to manage it."
        ],
        "Use your chaotic crowd/stress image here."
    )

    # --- SLIDE 3: THE VILLAIN (Old Way) ---
    add_zen_slide(
        "The False Solution: Homework",
        [
            "We started by building a Dashboard.",
            "We thought people wanted to organize their chaos.",
            "We were wrong.",
            "Nobody wants to be a data entry clerk for their own life."
        ],
        "SCREENSHOT: 'thjtj.png' (The old web dashboard). This shows the contrast."
    )

    # --- SLIDE 4: THE HERO (Zen Mode) ---
    add_zen_slide(
        "The Pivot: Instant Action",
        [
            "We scrapped the dashboard.",
            "We built a weapon.",
            "No data entry. No forms.",
            "Just point, shoot, and solve."
        ],
        "IMAGE: '93952B50...' (Scanning the Water Heater). Make this Full Bleed if possible."
    )

    # --- SLIDE 5: RECLAIM HOME (The Wedge) ---
    add_zen_slide(
        "The Audit: One Second Value",
        [
            "Identity: AI instantly recognizes Make/Model.",
            "Health: A 'Check Engine Light' for the home.",
            "Action: One-tap Fix or Buy.",
            "Powered by the FIGJAM Protocol."
        ],
        "IMAGE: 'home 2.jpg' (Scanning the Fridge). This is your slickest UI shot."
    )

    # --- SLIDE 6: RECLAIM MONEY (Retention) ---
    add_zen_slide(
        "The Pulse: Stop the Bleeding",
        [
            "We turn hidden drains into visible alerts.",
            "Energy vampires. Forgotten subscriptions.",
            "It's not a spreadsheet; it's a fuel gauge."
        ],
        "IMAGE: 'B8200FFF...' (The Energy/Money Graph)."
    )

    # --- SLIDE 7: COMMUNITY (The Moat) ---
    add_zen_slide(
        "Coordination, Not Surveillance",
        [
            "Replacing 'Nextdoor Anxiety' with asset-based help.",
            "'Who has a generator?'",
            "'Is the power out for you too?'",
            "Privacy-first. Opt-in only."
        ],
        "IMAGE: 'F3CE5CEC...' (The Map View)."
    )

    # --- SLIDE 8: THE ECOSYSTEM ---
    add_zen_slide(
        "Four Modules. One OS.",
        [
            "HOME: The Wedge (Free)",
            "MONEY: The Retention (Sub)",
            "RIGHTS: The Shield (Sub)",
            "COMMUNITY: The Moat (Network Effect)"
        ],
        "IMAGE: 'CC692E95...' (The 4-Phone Lineup). This is the 'Money Shot'."
    )

    # --- SLIDE 9: THE ASK ---
    add_zen_slide(
        "Fueling the Scale",
        [
            "Ask: $100k Bridge.",
            "I'm not asking to build the MVP.",
            "I'm asking to scale the MVP I'm holding right now.",
            "Unlocks: First 1,000 homeowners."
        ],
        "IMAGE: '805E0F42...' (Phone in Hand looking at alerts). Shows readiness."
    )

    # Save
    prs.save('Reclaim_Zen_Pitch.pptx')
    print("Deck generated! Open 'Reclaim_Zen_Pitch.pptx' and drop your images in.")

# Run it
if __name__ == "__main__":
    create_zen_deck()