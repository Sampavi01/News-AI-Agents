# crew.py (Final Corrected Version)

from crewai import Crew, Process
from agents import content_strategist, news_researcher, news_writer, editor
from tasks import plan_task, research_task, write_task, edit_task
from litellm_model import llm

# Define the Crew
crew = Crew(
    # <<< THE FIX IS HERE: The 'editor' agent has been removed from this list.
    agents=[content_strategist, news_researcher, news_writer],
    tasks=[plan_task, research_task, write_task, edit_task],
    process=Process.hierarchical,  # Use a hierarchical process
    manager_llm=llm,
    manager_agent=editor,          # The 'editor' is correctly designated as the manager here.
    verbose=True
)

# Function to run the crew
def run_crew(topic):
    result = crew.kickoff(inputs={'topic': topic})
    return result

# Example of running from the command line
if __name__ == "__main__":
    try:
        topic_input = input("What is the topic for the tech article? ")
        if topic_input:
            final_result = run_crew(topic_input)
            print("\n\n########################")
            print("## Here is the Final Result:")
            print("########################\n")
            print(final_result)
    except Exception as e:
        print(f"An error occurred: {e}")