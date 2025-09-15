# tasks.py
from crewai import Task
from tools import search_tool, website_content_search_tool
from agents import news_researcher, news_writer

# --- Task 1: Research and Synthesize ---
research_task = Task(
    description=(
        "Conduct a thorough research investigation into {topic}. "
        "Gather facts, statistics, and recent developments. "
        "Identify key players and technologies."
    ),
    expected_output=(
        "A detailed research report with synthesized findings, key statistics, "
        "and a list of credible sources for a blog post about {topic}."
    ),
    tools=[search_tool, website_content_search_tool],
    agent=news_researcher,
)

# --- Task 2: Write and Edit Blog Post ---
write_task = Task(
    description=(
        "Using the research report, write a compelling blog post on {topic}. "
        "First, create a clear outline with a catchy headline, introduction, 3-4 main points, and conclusion. "
        "Then, write the full article. "
        "Finally, review the article for clarity, accuracy, grammar, and overall quality, "
        "ensuring it aligns with the research. Produce a polished, publish-ready markdown article."
    ),
    expected_output=(
        "A polished markdown document on {topic}, complete with headline, structured outline, "
        "and final revisions, ready for publication."
    ),
    tools=[search_tool],
    agent=news_writer,
    context=[research_task],
    output_file='final_blog_post.md'
)

# --- Updated Workflow Function ---
def run_blog_workflow(topic: str):
    print(f"Running workflow for topic: {topic}")
    
    # Format the descriptions with the topic
    research_task_desc = research_task.description.format(topic=topic)
    write_task_desc = write_task.description.format(topic=topic)
    
    # Step 1: Research
    research_result = research_task.execute_sync(description=research_task_desc)
    print("Research Result:")
    print(research_result)
    
    # Step 2: Write blog post
    write_result = write_task.execute_sync(description=write_task_desc, context=[research_result])
    print("Blog Post Result:")
    print(write_result)
    
    # Output is also saved to 'final_blog_post.md'
    return write_result

# Example usage
if __name__ == "__main__":
    topic_input = "AI in healthcare"
    final_blog_post = run_blog_workflow(topic_input)
