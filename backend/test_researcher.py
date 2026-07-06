import json

from agents.lead_researcher import research_leads

result = research_leads("dental clinics", "Austin, TX", "practice owner")

print(json.dumps(result, indent=2))
