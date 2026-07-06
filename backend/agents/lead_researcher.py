import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def research_leads(industry: str, location: str, role: str, count: int = 5) -> list[dict]:
    prompt = f"""Find {count} real businesses matching the industry "{industry}" in {location}, targeting the {role} as the decision-maker.

Return ONLY a JSON array, no markdown fences, no preamble, no explanation. Each element must have exactly this structure:

{{
  "company_name": string,
  "website": string,
  "location": string,
  "description": string (1 sentence),
  "fit_reason": string (1 sentence, why this business is a good outreach target),
  "contact_hint": string (real name if findable via search, otherwise empty string "")
}}
"""

    grounding_tool = types.Tool(google_search=types.GoogleSearch())

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(tools=[grounding_tool]),
    )

    text = response.text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse lead researcher response as JSON: {e}\n\nRaw response:\n{response.text}")
