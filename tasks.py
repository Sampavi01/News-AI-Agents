# tasks.py (Modified)

from crewai import Task
from tools import search_tool, website_content_search_tool
# <<< REMOVED 'content_strategist' FROM IMPORTS >>>
from agents import news_researcher, news_writer, editor

# Task 1: Create a Content Plan (REMOVED)
# ---------------------------------------
# plan_task = Task(...)

# Task 2: Research and Synthesize (MODIFIED)
# <<< CONTEXT IS REMOVED SINCE plan_task NO LONGER EXISTS >>>
research_task = Task(
  description=(
    "Conduct a thorough research investigation into {topic}. "
    "Your goal is to gather all the necessary facts, statistics, and recent developments. "
    "Uncover the key players and groundbreaking technologies."
  ),
  expected_output='A detailed research report with synthesized findings, key statistics, and a list of credible source URLs for a blog post about {topic}.',
  tools=[search_tool, website_content_search_tool],
  agent=news_researcher,
  # context=[plan_task], # <<< THIS LINE IS REMOVED
)

# Task 3: Write the Blog Post (MODIFIED)
# <<< DESCRIPTION IS EXPANDED, CONTEXT IS CHANGED >>>
write_task = Task(
  description=(
    "Using the provided research report, write a compelling blog post on {topic}. "
    "Your first step is to create a clear and logical outline for the article, including a catchy headline, an introduction, 3-4 main points, and a conclusion. "
    "Once the outline is ready, write the full blog post. "
    "The tone should be engaging, informative, and accessible to a broad audience."
  ),
  expected_output='A well-written, formatted markdown document on {topic}, complete with a headline and structured outline, ready for publication.',
  tools=[search_tool],
  agent=news_writer,
  # <<< 'plan_task' IS REMOVED FROM THE CONTEXT >>>
  context=[research_task],
)

# Task 4: Edit and Finalize (No changes needed, but context is checked)
edit_task = Task(
  description=(
    "Review the drafted blog post. Check for clarity, accuracy, grammar, and overall quality. "
    "Ensure the article aligns perfectly with the research. "
    "Provide the final, polished version of the article, ready for publishing."
  ),
  expected_output='The final, publish-ready markdown article on {topic}, with any necessary revisions and a final approval check.',
  agent=editor,
  context=[write_task],
  output_file='final_blog_post.md'
)