# K Fitness Center

A static landing page/infographic for the **K Fitness Center – Automated Content Creation System** workflow.

## Preview locally

```bash
python3 -m http.server 4173
```

Then open <http://127.0.0.1:4173/index.html>.

## n8n connection

The landing page now includes an n8n lead/request form. To connect it:

1. In n8n, create a workflow with a **Webhook** trigger.
2. Set the webhook method to **POST** and copy the production webhook URL.
3. For the local n8n dashboard at <http://localhost:5678/home/workflows>, set the Webhook path to `kfitness-ai-os`. The page is already configured to send to <http://localhost:5678/webhook/kfitness-ai-os>.
4. If you deploy n8n somewhere else, open `index.html` and replace the `data-webhook-url` value with your production webhook URL.
5. Activate the n8n workflow.
6. Submit the form on the page. The browser sends JSON with `name`, `phone`, `requestType`, `message`, `source`, and `submittedAt` to n8n.

Suggested next n8n nodes: Google Sheets/Airtable for lead storage, Telegram or Messenger for staff alerts, and email/SMS for customer follow-up.
