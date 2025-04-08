from autogen import AssistantAgent

human_operator = AssistantAgent(
    name="HumanOperator",
    llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": None,
    }
)
