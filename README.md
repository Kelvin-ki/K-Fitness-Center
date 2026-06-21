# K Fitness Center

A static landing page/infographic for the **K Fitness Center – Automated Content Creation System** workflow.

## Preview locally

```bash
python3 -m http.server 4173
```

Then open <http://127.0.0.1:4173/index.html>.

## n8n Workflow Automation

This repository includes a local n8n installation for building and testing the automated content creation workflow used by K Fitness Center.

> Note: the requested package name `n8m` is not available on npm, so the automation tool referenced by this project, `n8n`, has been installed instead.

### Install dependencies

```bash
npm install
```

### Start n8n locally

```bash
npm run n8n:start
```

By default, n8n starts its editor UI on <http://localhost:5678>. Use it to design workflows for topic research, AI content generation, review, publishing, and analytics feedback.
