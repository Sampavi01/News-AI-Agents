# crew.py 

from crewai import Crew, Process
from agents import  news_researcher, news_writer
from tasks import  research_task, write_task
from litellm_model import llm

# Define the Crew
crew = Crew(
    agents=[news_researcher, news_writer],  # sufficient
    tasks=[research_task, write_task], # all tasks included
    manager_llm=llm  # handles orchestration
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