from github import Github
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def push_to_github(folder_path: str, repo_name: str):
    """
    Creates a GitHub repo, pushes the folder, and returns repo URL and commit SHA.
    """
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    repo = user.create_repo(repo_name, private=False)
    
    # Simplified: Add index.html
    file_path = os.path.join(folder_path, "index.html")
    with open(file_path, "r") as f:
        content = f.read()
    repo.create_file("index.html", "Initial commit", content)

    # Return URLs
    repo_url = repo.html_url
    commit_sha = repo.get_commits()[0].sha
    pages_url = f"https://{user.login}.github.io/{repo_name}/"
    return repo_url, commit_sha
