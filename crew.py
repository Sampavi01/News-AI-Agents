from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
import os

# Optional: Load environment variables
from dotenv import load_dotenv
load_dotenv()

from litellm import completion

# No need to pass LLM manually, CrewAI will use LiteLLM's default config
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True,
    # No llm= here — let CrewAI internally call litellm.completion()
)

# Set model name and let CrewAI auto-pick LiteLLM provider
os.environ["LITELLM_MODEL"] = "gemini/gemini-1.5-flash"

# Kickoff the process
result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)

