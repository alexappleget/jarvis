JARVIS_TOOLS = [
    {
        "type": "function",
        "name": "get_pr_description_personal",
        "description": "Fetch details from a GitHub PR in Alex's personal repository. Use this to get the PR title, files changed, commits, and the PR template. Then generate a professional description following the template format and call update_pr_description_personal to save it.",
        "parameters": {
            "type": "object",
            "properties": {
                "repo": {
                    "type": "string",
                    "description": "Repository name (e.g., 'jarvis', 'my-project')",
                },
                "pr_number": {
                    "type": "integer",
                    "description": "Pull request number to fetch and describe",
                },
            },
            "required": ["repo", "pr_number"],
        },
    },
    {
        "type": "function",
        "name": "update_pr_description_personal",
        "description": "Update the body of a GitHub PR in Alex's personal repository with a generated description that follows github_pr_template.md",
        "parameters": {
            "type": "object",
            "properties": {
                "repo": {
                    "type": "string",
                    "description": "Repository name (e.g., 'jarvis', 'my-project')",
                },
                "pr_number": {
                    "type": "integer",
                    "description": "Pull request number to update",
                },
                "description": {
                    "type": "string",
                    "description": "Full PR description to set as the PR body",
                },
            },
            "required": ["repo", "pr_number", "description"],
        },
    },
    {
        "type": "function",
        "name": "create_file",
        "description": "Create a new file with the specified name in the C:\\My Projects folder.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The name for the new file (e.g., 'notes.txt')."
                },
            },
            "required": ["filename"]
        }
    },
]