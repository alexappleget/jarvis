# AGENTS.md

## Project Overview

"jarvis" is a Python-based AI assistant and automation platform. All function logic lives in the `scripts/` directory. The main entry point is `app.py`, but all core logic is in `scripts/`. Agent tools (`jarvis_tools.py`), agent instructions (`jarvis_instructions.py`), and configuration (`config.py`) are always kept in the project root.

## Project Structure

- All scripts and function logic: [scripts/](scripts/)
- Agent tools: [jarvis_tools.py](jarvis_tools.py) (root)
- Agent instructions/persona: [jarvis_instructions.py](jarvis_instructions.py) (root)
- Configuration and environment variables: [config.py](config.py) (root)
- No tests or docs/ directory at this time

## Dependency Management

- All dependencies (including any future plugins/extensions) must be added to [requirements.txt](requirements.txt).
- Agents must never install packages directly; only add them to requirements.txt.

## Coding Standards

- Strictly follow PEP8 for all Python code.
- Use type hints for all function arguments. DO NOT use return type hints (the `-> int` part) anywhere.
- Every function must have a docstring describing its purpose and parameters.
- Code must be formatted with:
  ```
  black .
  isort .
  ```

## PR & Commit Guidelines

- PR title format: `[name of coding agent used] <short description of task>`
- All PRs must use the template in [github_pr_template.md](github_pr_template.md); this is always enforced.
- Commit messages must follow the conventional commit format.
- Linting/formatting must pass before PRs are submitted.
- Agents must never merge PRs into the main branch; user approval is always required.

## Agent-Specific Instructions

- If the agent is ever unsure about any action, it must ask the user for clarification before proceeding.
- Agents should only confirm task completion (e.g., "Task completed, Sir.") and never show tool output unless explicitly requested.
- Agents must never merge PRs into the main branch.
- Agents must never install packages or system dependencies; only add new dependencies to requirements.txt.
- If a task requires user guidance or confirmation, always ask before proceeding.

## Additional Notes

- For human contributors, see [README.md](README.md).
- This file is for coding agents. Human contributors should refer to the README.

---
