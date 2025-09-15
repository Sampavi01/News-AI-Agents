# agents.py
from crewai import Agent
from dotenv import load_dotenv
from tools import search_tool, website_content_search_tool
from litellm_model import llm

load_dotenv()

# --- Agent 1: Senior Researcher ---
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies and key trends in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation. You have a talent "
        "for digging deep, finding credible sources, and synthesizing complex information "
        "into actionable insights. You use your tools to go beyond surface-level searches."
    ),
    tools=[search_tool, website_content_search_tool],  # Matches research_task
    allow_delegation=False,
    llm=llm
)

# --- Agent 2: Expert Tech Writer ---
news_writer = Agent(
    role="Expert Tech Writer",
    goal="Compose a compelling and insightful blog post on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a renowned Tech Writer, famous for transforming complex technical "
        "details into engaging and easy-to-understand narratives. "
        "You follow instructions to produce high-quality, publish-ready articles."
    ),
    tools=[search_tool],  # Matches write_task
    allow_delegation=False,
    llm=llm
)
