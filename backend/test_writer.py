import json

from agents.email_writer import write_email

lead = {
    "company_name": "Riverside Dental Care",
    "website": "https://riversidedentalaustin.com",
    "location": "Austin, TX",
    "description": "A family-owned dental practice offering general and cosmetic dentistry in South Austin.",
    "fit_reason": "As a growing family practice, they likely handle a high volume of appointment scheduling and could benefit from reduced no-shows.",
    "contact_hint": "Dr. Sweeney",
}

result = write_email(lead)

print(json.dumps(result, indent=2))
