import json
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def write_email(lead: dict) -> dict:
    greeting_instruction = (
        f'Greet them by name, e.g. "Hi Dr. Sweeney,", using contact_hint "{lead["contact_hint"]}".'
        if lead.get("contact_hint")
        else f'Use a generic greeting like "Hi there," or "Hi {lead["company_name"]} team,".'
    )

    prompt = f"""Write a cold outreach email to the following business:

Company: {lead["company_name"]}
Description: {lead["description"]}
Why they're a good fit: {lead["fit_reason"]}

Requirements:
- Pitch an AI-powered appointment scheduling and no-show reduction assistant.
- Tone: professional, warm, not salesy. 80-120 words.
- Reference something specific about their practice from the description or fit reason above.
- {greeting_instruction}
- Sign off as "Rishabh" from an AI automation freelance service.

Return ONLY valid JSON, no markdown fences, no preamble, with exactly this structure:

{{
  "subject": string,
  "body": string
}}
"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse email writer response as JSON: {e}\n\nRaw response:\n{response.content[0].text}")
