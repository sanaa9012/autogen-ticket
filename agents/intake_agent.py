from autogen import AssistantAgent

intake_agent = AssistantAgent(
    name="IntakeAgent",
    llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": None,
    }
)
