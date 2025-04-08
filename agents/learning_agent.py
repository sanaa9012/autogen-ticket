from autogen import AssistantAgent

learning_agent = AssistantAgent(
    name="LearningAgent",
    llm_config={
        "model": "gpt-4gpt-3.5-turbo",
        "api_key": None,
    }
)
