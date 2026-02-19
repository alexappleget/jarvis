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
        "name": "add_google_calendar_event",
        "description": "Add a new event to Alex's Google Calendar.",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "The title or summary of the calendar event.",
                },
                "start_time": {
                    "type": "string",
                    "description": "The start date and time of the event in ISO 8601 format (e.g., '2026-02-19T10:00:00').",
                },
                "end_time": {
                    "type": "string",
                    "description": "The end date and time of the event in ISO 8601 format (e.g., '2026-02-19T11:00:00').",
                },
                "description": {
                    "type": "string",
                    "description": "An optional description or notes for the event.",
                },
                "location": {
                    "type": "string",
                    "description": "An optional location for the event.",
                },
            },
            "required": ["summary", "start_time", "end_time"],
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
                    "description": "The name for the new file (e.g., 'notes.txt').",
                },
            },
            "required": ["filename"],
        },
    },
]
