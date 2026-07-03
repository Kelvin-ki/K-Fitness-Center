#!/usr/bin/env python3
"""Generate a step-by-step K Fitness Center content workflow brief.

This script turns the poster workflow in data/content-workflow.json into a
ready-to-review content production brief. It does not call external AI services;
it prepares the exact step-by-step inputs, prompts, and outputs that staff or an
automation tool can pass into writing, image, video, and publishing systems.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "content-workflow.json"
DEFAULT_OUTPUT = ROOT / "output" / "k-fitness-content-brief.md"

BUSINESS = {
    "name": "K Fitness Center",
    "location": "Shwe Kokko Myain, Myawaddy",
    "map": "https://maps.app.goo.gl/pDefLUxTmSoZ3RB18?g_st=ipc",
    "phones": "09966766466, 09676003533, 09675844933",
    "hours": "Monday to Saturday, 6:00 AM to 1:00 AM. Sunday closed.",
    "monthly": "1700฿ + 300฿ membership fee",
    "three_months": "5000฿ + 1 month free",
    "six_months": "10000฿ + 3 months free",
}


def load_workflow(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_brief(workflow: dict, topic: str, platform: str, language: str) -> str:
    steps = workflow["workflow"]
    feedback = workflow["feedback_loop"]
    checklist = workflow["publishing_checklist"]

    lines = [
        f"# {BUSINESS['name']} Content Production Brief",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"Topic: **{topic}**  ",
        f"Platform: **{platform}**  ",
        f"Language: **{language}**",
        "",
        "## Business Source of Truth",
        "",
        f"- Location: {BUSINESS['location']}",
        f"- Google Map: {BUSINESS['map']}",
        f"- Phone: {BUSINESS['phones']}",
        f"- Opening: {BUSINESS['hours']}",
        f"- Monthly: {BUSINESS['monthly']}",
        f"- 3 months: {BUSINESS['three_months']}",
        f"- 6 months: {BUSINESS['six_months']}",
        "",
        f"## Step 1 — {steps[0]['name']} ({steps[0]['module']})",
        "",
        "Tasks:",
        bullet_list(steps[0]["tasks"]),
        "",
        "Output to create:",
        f"- Main topic: {topic}",
        "- 3 alternative hooks:",
        "  1. Want better results but do not know where to start?",
        "  2. Start training today, not next month.",
        "  3. Build strength, burn fat, and stay consistent at K Fitness Center.",
        "",
        f"## Step 2 — {steps[1]['name']} ({steps[1]['module']})",
        "",
        "Tasks:",
        bullet_list(steps[1]["tasks"]),
        "",
        "Approved plan:",
        "- Content type: Short video + image poster",
        "- Format: Vertical 9:16 for TikTok/Reels/Shorts, square 1:1 for Facebook/Instagram",
        "- Target customer: Beginner or returning gym customer in Shwe Kokko / Myawaddy",
        "- Posting time: Evening after work, or morning before gym rush",
        "",
        f"## Step 3 — {steps[2]['name']} ({steps[2]['module']})",
        "",
        "Tasks:",
        bullet_list(steps[2]["tasks"]),
        "",
        "Caption formula: **Question > Emotion > Trust > Offer > Close**",
        "",
        "Draft caption:",
        "> Want to start your fitness journey but not sure what to do first?  ",
        "> Starting alone can feel hard, but K Fitness Center makes it simple.  ",
        "> Train with equipment, free group classes, nutrition guidance, and coach support.  ",
        f"> Monthly plan: {BUSINESS['monthly']}. 3 months: {BUSINESS['three_months']}. 6 months: {BUSINESS['six_months']}.  ",
        f"> Visit {BUSINESS['location']} or call {BUSINESS['phones']}. Map: {BUSINESS['map']}",
        "",
        f"## Step 4 — {steps[3]['name']} ({steps[3]['module']})",
        "",
        "Tasks:",
        bullet_list(steps[3]["tasks"]),
        "",
        "Image brief:",
        "- Brand color: black + yellow + white",
        "- Main headline: START STRONG AT K FITNESS CENTER",
        "- Visual: confident gym member, dumbbells, clean gym background",
        "- Footer: phone numbers + map note",
        "- Safety: no unrealistic body transformation promise",
        "",
        f"## Step 5 — {steps[4]['name']} ({steps[4]['module']})",
        "",
        "Tasks:",
        bullet_list(steps[4]["tasks"]),
        "",
        "Video script:",
        "- Scene 1: Hook text on screen — \"Still waiting to start gym?\"",
        "- Scene 2: Show equipment and beginner exercise clips",
        "- Scene 3: Show group class energy: Aerobics, Zumba, Trampoline, Step Board",
        "- Scene 4: Show offer: monthly, 3-month, and 6-month plans",
        "- Scene 5: CTA: \"Message or call K Fitness Center today\"",
        "",
        f"## Step 6 — {steps[5]['name']} ({steps[5]['module']})",
        "",
        "Tasks:",
        bullet_list(steps[5]["tasks"]),
        "",
        "Publishing plan:",
        "- Facebook/Instagram: poster + full caption",
        "- TikTok/Reels/Shorts: 15-30 second vertical video",
        "- Telegram: short caption + poster + phone numbers",
        "- YouTube: Shorts version first; long video can follow if engagement is high",
        "",
        "## Step 7 — Feedback & Performance Data",
        "",
        "Track:",
        bullet_list(feedback),
        "",
        "Weekly improvement rules:",
        "- If comments ask about price, make the next post price-focused.",
        "- If video watch time drops early, make the first 2 seconds stronger.",
        "- If messages increase after showing promotions, repeat the offer with a new visual.",
        "- If health/injury comments appear, reply safely and recommend medical consultation.",
        "",
        "## Final Publishing Checklist",
        "",
        bullet_list(checklist),
    ]
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate K Fitness step-by-step content brief")
    parser.add_argument("--topic", default="Beginner workout guide", help="Content topic")
    parser.add_argument("--platform", default="Facebook / TikTok / YouTube Shorts", help="Target platform")
    parser.add_argument("--language", default="Myanmar-English bilingual", help="Output language direction")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="Workflow JSON path")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output markdown path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workflow = load_workflow(args.data)
    brief = render_brief(workflow, args.topic, args.platform, args.language)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(brief, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
