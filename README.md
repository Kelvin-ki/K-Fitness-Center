# K Fitness Center

A static landing page/infographic and knowledge base for the **K Fitness Center – Automated Content Creation System** workflow.

## Business Source of Truth

| Field | Official information |
| --- | --- |
| Gym name | K Fitness Center |
| Location | Shwe Kokko Myain, Myawaddy |
| Google Map | https://maps.app.goo.gl/pDefLUxTmSoZ3RB18?g_st=ipc |
| Phone numbers | 09966766466, 09676003533, 09675844933 |
| Opening hours | Monday to Saturday, 6:00 AM to 1:00 AM |
| Sunday | Closed |

### Pricing

| Plan or service | Price |
| --- | --- |
| Single visit | 250฿ |
| Monthly plan | 1700฿ + 300฿ membership fee |
| 3-month plan | 5000฿ with 1 month free |
| 6-month plan | 10000฿ with 3 months free |
| Private Coach | +2000฿ |
| Pickup service | +2000฿ |

### Free Group Classes

Aerobics, Zumba, Trampoline, and Step Board are free group classes for members.

### Services

K Fitness Center supports Muscle gain, fat loss, CrossFit, private coaching, nutrition guidance, and pickup service.

## Official AI Assistant Role

The official assistant answers customer questions about prices, opening hours, services, membership options, location, contact numbers, and marketing posts. It supports Myanmar, English, Chinese, and bilingual Myanmar-English customer conversations.

For detailed response scripts and templates, use `docs/assistant-playbook.md`.

## Sales Style

1. Answer the question directly.
2. Highlight the customer benefit.
3. Recommend the best plan for the customer's goal.
4. Ask for the next action and include a contact number when closing.

## Safety Rules

- Do not provide medical diagnosis.
- Do not promise exact weight-loss results.
- If a customer mentions pain, injury, dizziness, pregnancy, or any health condition, ask them to consult a qualified medical professional before training.
- Fitness guidance is general information and not a replacement for professional medical advice.

## Marketing Post Structure

Use this five-part structure for Facebook, Telegram, TikTok, and YouTube content:

1. **Question** — open with a relatable customer problem.
2. **Emotion** — connect with the customer's goal or frustration.
3. **Trust** — mention K Fitness Center coaching, safety, and support.
4. **Offer** — recommend the right plan, class, or service.
5. **Close** — give phone numbers and the map link.

## Claude Code Installation

Claude Code has been installed in this environment using the official npm package:

```bash
npm install -g @anthropic-ai/claude-code@latest
claude --version
```

Verified installed version: `2.1.185 (Claude Code)`.

Requirements and maintenance notes:

- Node.js 18 or later is required; this environment has Node.js 20.20.2.
- Do not use `sudo npm install -g` for Claude Code.
- Upgrade with `npm install -g @anthropic-ai/claude-code@latest`.

## Preview locally

```bash
python3 -m http.server 4173
```

Then open <http://127.0.0.1:4173/index.html>.
