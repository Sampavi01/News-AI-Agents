from crewai import Task
# MODIFIED IMPORT
from tools import search_tool, website_content_search_tool
from agents import content_strategist, news_researcher, news_writer, editor

# Task 1: Create a Content Plan
plan_task = Task(
  description=(
    "1. Identify the key trends and sub-topics within {topic}.\n"
    "2. Determine the target audience and the key message of the blog post.\n"
    "3. Create a detailed outline for the blog post, including an introduction, 3-4 main body points with sub-bullets, and a conclusion.\n"
    "4. Suggest a compelling headline."
  ),
  expected_output="A comprehensive content plan document with a headline, target audience analysis, and a detailed outline for a blog post about {topic}.",
  agent=content_strategist,
)

# Task 2: Research and Synthesize
research_task = Task(
  description=(
    "1. Use the 'SerperDevTool' to find 3-5 relevant URLs for the topic: {topic}.\n"
    "2. For each URL, use the 'Website Content Search Tool' to extract the most relevant information that matches the key points from the content plan.\n"
    "3. The input for the 'Website Content Search Tool' MUST be a comma-separated string containing the URL and the specific query (e.g., 'https://example.com, What are the future trends of AI?').\n"
    "4. Synthesize all the gathered information into a detailed research report."
  ),
  expected_output='A detailed research report with synthesized findings, key statistics, and a list of credible source URLs for a blog post about {topic}.',
  tools=[search_tool, website_content_search_tool], # <-- USE THE NEW TOOL HERE
  agent=news_researcher,
  context=[plan_task],
)

# Task 3: Write the Blog Post
write_task = Task(
  description=(
    "Using the content plan and research report, write a compelling blog post on {topic}. "
    "The tone should be engaging, informative, and accessible to a broad audience. "
    "Follow the outline strictly. Ensure the article flows well and tells a coherent story."
  ),
  expected_output='A well-written, formatted markdown document of at least 4 paragraphs on {topic}, ready for publication.',
  tools=[search_tool],
  agent=news_writer,
  context=[plan_task, research_task],
)

# Task 4: Edit and Finalize
edit_task = Task(
  description=(
    "Review the drafted blog post. Check for clarity, accuracy, grammar, and overall quality. "
    "Ensure the article aligns perfectly with the original content plan and research. "
    "Provide the final, polished version of the article."
  ),
  expected_output='The final, publish-ready markdown article on {topic}, with any necessary revisions and a final approval check.',
  agent=editor,
  context=[write_task],
  output_file='final_blog_post.md'
)