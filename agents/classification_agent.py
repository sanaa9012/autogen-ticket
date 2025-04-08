from autogen import AssistantAgent

classification_agent = AssistantAgent(
    name="ClassificationAgent",
    llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": None,
    }
)
