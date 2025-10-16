from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from generator import generate_app
from utils import push_to_github
import os

app = FastAPI()

STUDENT_SECRET = os.getenv("STUDENT_SECRET")

class TaskRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    brief: str
    evaluation_url: str

@app.post("/api/endpoint")
async def receive_task(request: TaskRequest):
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
