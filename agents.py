
from crewai import Agent
# MODIFIED IMPORT: Remove scrape_tool

from dotenv import load_dotenv
from litellm_model import llm
from tools import search_tool, website_content_search_tool

load_dotenv()
<<<<<<< HEAD
import os

## call the gemini models
from litellm import completion

llm = "gemini/gemini-1.5-flash"
# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
=======

# Agent 1: The Content Strategist
content_strategist = Agent(
    role="Content Strategist",
    goal="Develop a detailed content plan for a blog post on {topic}",
    backstory=(
        "You are an expert Content Strategist with a knack for identifying compelling angles "
        "and structuring content for maximum impact and engagement. You create clear "
        "and concise plans that guide writers to success."
    ),
    llm=llm,
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)

# Agent 2: The Senior Researcher
# Agent 2: The Senior Researcher (MODIFIED)
news_researcher = Agent(
>>>>>>> 5b04454 (Expanded the agent system to improve task delegation and reasoning flow. Also added initial UI components to enhance interactivity and accessibility.)
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies and key trends in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation. You have a talent "
        "for digging deep, finding credible sources, and synthesizing complex information "
        "into actionable insights. You don't just find links; you analyze content."
    ),
    # MODIFIED TOOLS: Use website_search_tool instead of scrape_tool
    tools=[search_tool, website_content_search_tool],
    allow_delegation=False,
    llm=llm
)

# Agent 3: The Writer
news_writer = Agent(
    role='Expert Tech Writer',
    goal='Compose a compelling and insightful blog post on {topic} based on a provided content plan',
    verbose=True,
    memory=True,
    backstory=(
        "You are a renowned Tech Writer, famous for your ability to transform complex technical "
        "details into engaging and easy-to-understand narratives. You follow content plans "
        "diligently to produce high-quality, ready-to-publish articles."
    ),
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)

# Agent 4: The Editor (Manager Agent)
editor = Agent(
    role="Chief Editor",
    goal="Oversee the content creation process, ensuring the final blog post about {topic} is coherent, accurate, and meets the highest quality standards.",
    backstory=(
        "You are the Chief Editor of a major tech publication. With years of experience, you have a sharp eye for detail, a deep understanding of what makes a story compelling, and the leadership skills to manage a team of strategists, researchers, and writers to produce top-notch content."
    ),
    verbose=True,
    allow_delegation=True,
    llm=llm,
)    
