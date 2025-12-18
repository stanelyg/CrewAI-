🤖 CrewAI Projects
This repository contains projects built using CrewAI, a framework for orchestrating AI agents that collaborate to solve complex tasks.
CrewAI enables you to define agents with specific roles, assign them tasks, and control how they work together as a crew.

🚀 What is CrewAI?
CrewAI is a Python-based framework for building multi-agent AI systems.
Each agent has:
- A role (e.g. Researcher, Developer, Reviewer)
- A goal
- Optional tools (search, code execution, APIs)
Agents collaborate through structured workflows to complete tasks efficiently.

🧩 Core Concepts
🔹 Agent
An Agent represents an AI worker with a defined role and responsibility.
Example roles:
- Researcher
- Python Developer
- Data Analyst
- Reviewer

🔹 Task
A Task defines what needs to be done and which agent is responsible for it.
Tasks can:
- Depend on other tasks
- Produce outputs used by later tasks
- Be executed sequentially or in parallel

🔹 Crew
A Crew is a collection of agents and tasks working together.
The crew controls:
- Execution flow (sequential or parallel)
- Context sharing between agents
- Overall orchestration
