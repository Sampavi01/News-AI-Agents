# CrewAI-Projects ✨

Autonomous AI agents for smart web search, analysis, and task execution using **CrewAI**, **Google Gemini**, and **SerperDevTool**.  

## Key Features 🚀
- 🤖 **CrewAI Agents:** Build & coordinate multiple AI agents effortlessly.  
- 🧠 **Advanced Reasoning:** Leverage Google Gemini for deep language understanding.  
- 🌐 **Live Web Search:** Real-time info with SerperDevTool (`SERPER_API_KEY`).  
- 🔗 **LLM Integration:** Connect securely to LLMs via `LITELLM_API_KEY`.  
- ⚙️ **Extensible:** Add new agents, tools, and tasks easily. 

### 🌐 Streamlit Demo (app.py)
![Streamlit Demo](ezgif.com-speed%20(11).gif)

## 📂 Directory Structure


```text
CrewAI-Projects/
├── LICENSE
├── README.md
└── crewgooglegemini/
    ├── agents.py         # Agent definitions
    ├── crew.py           # Crew orchestration logic
    ├── requirements.txt  # Python dependencies
    ├── tasks.py          # Task definitions
    ├── tools.py          # Tool integrations (e.g.,SerperDevTool)
    └── __pycache__/
```

## Getting Started

### 1. Clone the Repository

```powershell
git clone https://github.com/Sampavi01/News-AI-Agents.git
cd CrewAI-Projects/crewgooglegemini
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Environment Variables


Create a `.env` file in the `crewgooglegemini` directory (or set environment variables directly) with your API keys:

```env
# SerperDevTool for web search
SERPER_API_KEY=your_serper_api_key_here

# LITELLM for LLM access (e.g., Google Gemini, OpenAI, etc.)
LITELLM_API_KEY=your_litellm_api_key_here
```

> **Note:**
> - `SERPER_API_KEY` is required for internet search capabilities.
> - `LITELLM_API_KEY` is required for connecting to LLM providers via LiteLLM (used for Google Gemini or other supported models).

### 4. Run the Main Script

```powershell
python crew.py
```
### 💻 CLI Demo (crew.py)
![CLI Demo](ezgif.com-speed%20(10).gif)

## Usage Guide

- **Define Agents:** Customize or add new agents in `agents.py`.
- **Create Tasks:** Specify agent tasks in `tasks.py`.
- **Integrate Tools:** Add or modify tools in `tools.py`.
- **Test & Orchestrate:** Use `crew.py` to run your agent crew, or `test.py` for examples and testing.

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request to help improve this project.

## License

This project is licensed under the terms of the LICENSE file.
