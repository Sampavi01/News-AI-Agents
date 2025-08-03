import streamlit as st
from crew import run_crew # Import the function from your main script

st.set_page_config(page_title="AI Agent Crew", page_icon="🤖")

st.title("🤖 AI Agent Crew")
st.markdown("### Powered by CrewAI & Streamlit")

st.write(
    "This application leverages a team of AI agents to research, plan, write, "
    "and edit a comprehensive blog post on any given tech topic."
)

# Input topic from user
topic = st.text_input(
    "Enter the topic for the blog post:",
    placeholder="e.g., 'The Future of Quantum Computing'"
)

if st.button("🚀 Generate Article"):
    if topic:
        with st.spinner("🤖 The AI Crew is on the job! This may take a few minutes..."):
            try:
                # Run the crew with the user's topic
                result = run_crew(topic)
                
                st.success("Article generated successfully!")
                
                # Display the final result
                st.markdown("---")
                st.subheader("Final Polished Article:")
                st.markdown(result)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic to start.")