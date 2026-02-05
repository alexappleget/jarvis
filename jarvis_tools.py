JARVIS_TOOLS = [
    {
        "type": "function",
        "name": "get_pr_description_personal",
        "description": "Fetch details from a GitHub PR in Alex's personal repository and generate a structured PR description following the github_pr_template.md format, including a clear description of changes, type of change classification, and completed checklist items",
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
]