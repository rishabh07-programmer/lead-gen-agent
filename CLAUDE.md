# Project: Multi-Agent Lead Gen & Outreach System

## Rules
- NO browser automation — I test manually in my own browser
- Terminal output: concise. Don't dump full stack traces unless I ask — summarize the error and the fix
- This is a Render free tier deployment (512MB RAM). Flag any dependency over ~50MB before installing
- Use Claude Haiku model string during dev. Only switch to Sonnet when I say "demo mode"
- Commit after every working milestone — don't wait for me to ask
- PowerShell: no `&&`. Use `;` or separate lines. Env vars don't persist between sessions — use start.ps1

## Stack
- FastAPI + uvicorn (backend, serves frontend too)
- google-genai (Agent 1 — lead research, Gemini 2.5 Flash + Search grounding)
- anthropic (Agent 2 — email writer, Haiku dev / Sonnet demo)
- Plain HTML/CSS/JS frontend, SSE for streaming progress
- No database, no file storage — stateless request/response

## Current Milestone
Step 0: hello-world deploy to Render
