from autogen import AssistantAgent

supervisor_agent = AssistantAgent(
    name="SupervisorAgent",
    llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": None,
    }
)
