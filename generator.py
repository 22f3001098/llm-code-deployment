import os
import uuid

def generate_app(brief: str, task: str):
    """
    Use OpenAI LLM to generate minimal app code based on the brief.
    For simplicity, just create a folder with a basic index.html.
    """
    folder_name = f"{task}_{uuid.uuid4().hex[:6]}"
    os.makedirs(folder_name, exist_ok=True)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{task}</title>
    </head>
    <body>
        <h1>{brief}</h1>
    </body>
    </html>
    """
    with open(os.path.join(folder_name, "index.html"), "w") as f:
        f.write(html_content)

    pages_url = f"https://your-github-username.github.io/{folder_name}/"
    return folder_name, pages_url
