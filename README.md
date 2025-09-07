This project demonstrates an agentic AI pipeline that transforms a natural language user prompt into a fully functional software project. It uses LangGraph to orchestrate three specialized agents — Planner, Architect, and Coder — which collaborate to generate project files inside a sandboxed folder.

🚀 Features

Planner Agent → Converts user requests into a structured engineering project plan.

Architect Agent → Breaks the plan into step-by-step, file-specific implementation tasks.

Coder Agent → Iteratively executes tasks, writing project files using safe file tools.

Safe File Handling → All generated code is stored inside generated_project/, with path checks to prevent unsafe writes.

Extensible Design → Built with LangGraph and Pydantic for structured, modular development.

📂 Project Structure
.
├── graph.py       # Main orchestrator: sets up LLM, defines agents, builds LangGraph workflow
├── prompts.py     # Prompt templates for Planner, Architect, and Coder agents
├── states.py      # Pydantic models defining Plan, TaskPlan, ImplementationTask, CoderState
├── tools.py       # Safe file operations and utilities (read, write, list, run commands)
└── generated_project/   # All generated project files will be stored here
