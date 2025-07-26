from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Create the Gemini LLM instance with your Google API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Pass the llm to Crew
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    llm=llm,         
    verbose=True     # optional but helps debug
)

# Kickoff the process
result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
