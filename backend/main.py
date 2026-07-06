from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "alive", "project": "lead-gen-agent v1"}
