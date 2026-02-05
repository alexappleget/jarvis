JARVIS_TOOLS = [
    {
        "type": "function",
        "name": "hello",
        "description": "Say hello to someone by name",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the person to greet",
                }
            },
            "required": ["name"],
        },
    }
]
