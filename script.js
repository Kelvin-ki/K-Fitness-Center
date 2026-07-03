const form = document.querySelector('[data-n8n-form]');
const statusEl = document.querySelector('[data-n8n-status]');

const N8N_WEBHOOK_URL = form?.dataset.webhookUrl || '';

function setStatus(message, type = 'info') {
  if (!statusEl) return;
  statusEl.textContent = message;
  statusEl.dataset.state = type;
}

form?.addEventListener('submit', async (event) => {
  event.preventDefault();

  if (!N8N_WEBHOOK_URL) {
    setStatus('Please add your n8n webhook URL in index.html first.', 'warning');
    return;
  }

  const payload = Object.fromEntries(new FormData(form).entries());
  payload.source = 'K Fitness Center landing page';
  payload.submittedAt = new Date().toISOString();

  setStatus('Sending to n8n workflow...', 'info');

  try {
    const response = await fetch(N8N_WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`n8n returned ${response.status}`);
    }

    form.reset();
    setStatus('Success! Your request was sent to n8n automation.', 'success');
  } catch (error) {
    setStatus(`Could not send to n8n at ${N8N_WEBHOOK_URL}. Make sure your local workflow is active: ${error.message}`, 'error');
  }
});
