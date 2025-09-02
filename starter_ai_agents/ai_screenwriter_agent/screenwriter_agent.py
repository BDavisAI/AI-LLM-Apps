import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat

st.sidebar.title("API Key Configuration")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

st.title("🎬 AI Screenwriter")
idea = st.text_area("Describe your movie idea", height=200)

if openai_api_key and st.button("Generate Screenplay"):
    if idea.strip() == "":
        st.warning("Please enter an idea first.")
    else:
        agent = Agent(
            name="Screenwriter Agent",
            model=OpenAIChat(id="gpt-4o-mini", api_key=openai_api_key),
            instructions=[
                "You are an award‑winning Hollywood screenwriter.",
                "Given an idea, create:",
                "1. A compelling logline",
                "2. Main characters with short descriptions",
                "3. A three‑act outline",
                "4. The opening scene with brief dialogue",
                "Format the result in markdown with clear sections."
            ],
            markdown=True,
        )

        with st.spinner("Writing your screenplay..."):
            response = agent.run(idea)
            st.markdown(response.content)
else:
    st.sidebar.warning("Please provide your OpenAI API key to use the app.")
