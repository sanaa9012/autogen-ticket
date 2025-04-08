from autogen import AssistantAgent

assignment_agent = AssistantAgent(
    name="AssignmentAgent",
    llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": None,
    }
)
