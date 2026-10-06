---
name: magnific-fitness-video
description: Create short fitness, nutrition, and gym marketing videos with Magnific. Use when a user requests Magnific fitness reels, food-versus-training videos, gym ads, or reusable prompts for these videos.
---

# Magnific Fitness Video

## Choose the creative direction
Use the topic and references already supplied. Choose sensible defaults without asking optional follow-up questions: vertical 9:16, approximately 15 seconds, photorealistic visuals, clean black/gold/white typography, energetic music. Match the user's language. Ask only for information essential to proceed.

Use only supplied official logos and face references. Without an official logo, use plain brand text only when the user requests branding. Do not invent faces that impersonate a specified person.

## Run Magnific
1. Discover the available Magnific tools and their current schemas. Never assume model names, pricing, or supported durations.
2. Call account_balance before paid generation. If authentication is expired, tell the user to sign out of the Magnific panel and sign in again. Preserve the creative brief; do not claim generation succeeded or bypass the service with another provider.
3. Read video_models_list and select an available model matching the duration, aspect ratio, resolution, and sound requirements. For longer or composed videos, inspect video_plan before proceeding.
4. Use video_generate with one video at the root of the request. Supply a clear sequence, camera direction, natural movement, sound intent, and exact on-screen text. Use actual asset URLs or creation identifiers for references, never display-page URLs.
5. Call creations_show once with every returned creation identifier. Let its widget display and poll the result. Distinguish queued generation from completed output.
6. Inspect completed output when tools permit. Check text readability, exercise movement, food realism, framing, and timing. Make only necessary corrections.
7. Present the rendered result and a brief status. Never claim a downloadable file, completed render, publication, or scientific verification without supporting tool results.

## Keep fitness messaging accurate
Treat “Food 70% / Training 30%” as a motivational framing, never a universal scientific formula or guaranteed result. Include a readable qualification in the video; if exact text rendering is unreliable, prefer the accurate phrase “Food + Training + Recovery” and explain the limitation.
Avoid guaranteed transformations, arbitrary before/after bodies, and claims that nutrition replaces resistance training. Browse authoritative sources when adding medical or specific nutrition advice.

## Use the example
Read [food-training-brief.md](references/food-training-brief.md) for the supplied 70/30 topic. Adapt its creative choices to supported model capabilities. If a model cannot reliably render text, use available composition tools to add accurate typography rather than promising readable generated lettering.
