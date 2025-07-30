# CrewAI-Projects

Empowering autonomous AI agents to search, analyze, and process information from the web using CrewAI, Google Gemini, and SerperDevTool.

---

## Overview

**CrewAI-Projects** is a modular framework for orchestrating AI agents capable of performing complex, multi-step tasks. Leveraging the power of [CrewAI](https://github.com/joaomdmoura/crewai), Google Gemini, and SerperDevTool, this project enables agents to autonomously search the internet, extract insights, and collaborate to solve real-world problems.

## Key Features

- **Seamless CrewAI Integration:** Build, manage, and coordinate multiple AI agents with CrewAI.
- **Advanced Reasoning:** Utilize Google Gemini for state-of-the-art language understanding and reasoning.
- **Live Internet Search:** Integrate SerperDevTool for real-time web search (requires `SERPER_API_KEY`).
- **Extensible Architecture:** Easily add new agents, tools, and tasks to suit your workflow.

## Directory Structure

```text
CrewAI-Projects/
├── LICENSE
├── README.md
└── crewgooglegemini/
    ├── agents.py         # Agent definitions
    ├── crew.py           # Crew orchestration logic
    ├── requirements.txt  # Python dependencies
    ├── tasks.py          # Task definitions
    ├── test.py           # Example/test script
    ├── tools.py          # Tool integrations (e.g., SerperDevTool)
    └── __pycache__/
```

## Getting Started

### 1. Clone the Repository

```powershell
git clone https://github.com/Sampavi01/News-AI-Agents.git
cd CrewAI-Projects
```

### 2. Install Dependencies

```powershell
pip install -r crewgooglegemini/requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root (or set environment variables directly) with your Serper API key:

```env
SERPER_API_KEY=your_serper_api_key_here
```

### 4. Run the Main Script

```powershell
python crewgooglegemini/crew.py
```

## Usage Guide

- **Define Agents:** Customize or add new agents in `agents.py`.
- **Create Tasks:** Specify agent tasks in `tasks.py`.
- **Integrate Tools:** Add or modify tools in `tools.py`.
- **Test & Orchestrate:** Use `crew.py` to run your agent crew, or `test.py` for examples and testing.

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request to help improve this project.

## License

This project is licensed under the terms of the LICENSE file.
