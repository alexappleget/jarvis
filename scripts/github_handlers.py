from github import Github
from config import GITHUB_TOKEN, GITHUB_USERNAME

def get_pr_description_personal(repo: str, pr_number: int):
  """
  Fetch PR details from a personal GitHub repository.
  Returns PR context for the AI to generate a description.
  """
  try:
    github = Github(GITHUB_TOKEN)
    user = github.get_user(GITHUB_USERNAME)
    repo_obj = user.get_repo(repo)
    pr = repo_obj.get_pull(pr_number)

    files_changed = [file.filename for file in pr.get_files()]

    commits = [{"message": commit.commit.message, "author": commit.commit.author.name} for commit in pr.get_commits()]

    with open('github_pr_template.md', 'r') as f:
      template = f.read()

    return {
      "success": True,
      "pr_title": pr.title,
      "pr_body": pr.body or "(No description)",
      "files_changed": files_changed,
      "commits": commits,
      "base_branch": pr.base.ref,
      "head_branch": pr.head.ref,
      "template": template,
    }
  
  except Exception as error:
    print(f"Error in getting personal PR description: {error}")

def update_pr_description_personal(repo: str, pr_number: int, description: str):
  """Update the PR body with the generated description."""
  try:
    github = Github(GITHUB_TOKEN)
    user = github.get_user(GITHUB_USERNAME)
    repo_obj = user.get_repo
    pr = repo_obj.get_pull(pr_number)

    pr.edit(body=description)

    return {"success": True}
  
  except Exception as error:
    print(f"Error updating personal PR description: {error}")