from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from generator import generate_app
from utils import push_to_github
import os

app = FastAPI()

# Secret to verify requests
STUDENT_SECRET = os.getenv("STUDENT_SECRET")

# Request model
class TaskRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    brief: str
    evaluation_url: str

# Root GET endpoint for testing
@app.get("/")
def root():
    return {"message": "LLM Code Deployment API is running!"}

# POST endpoint to receive tasks
@app.post("/api/endpoint")
async def receive_task(request: TaskRequest):
    # Verify secret
    if request.secret != STUDENT_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # Generate minimal app using LLM
    repo_path, pages_url = generate_app(request.brief, request.task)

    # Push to GitHub and enable Pages
    repo_url, commit_sha = push_to_github(repo_path, request.task)

    return {
        "status": "ok",
        "message": "Task received",
        "data": {
            "email": request.email,
            "task": request.task,
            "round": request.round,
            "repo_url": repo_url,
            "commit_sha": commit_sha,
            "pages_url": pages_url
        }
    }
