from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.email_writer import write_email
from agents.lead_researcher import research_leads

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateLeadsRequest(BaseModel):
    industry: str
    location: str
    role: str


@app.get("/")
def read_root():
    return {"status": "alive", "project": "lead-gen-agent v1"}


@app.post("/api/generate-leads")
def generate_leads(req: GenerateLeadsRequest):
    leads = research_leads(req.industry, req.location, req.role)

    combined = []
    for lead in leads:
        email = write_email(lead)
        combined.append({**lead, "email_subject": email["subject"], "email_body": email["body"]})

    return {"leads": combined}
