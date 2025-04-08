from autogen import AssistantAgent

monitoring_agent = AssistantAgent(
    name="MonitoringAgent",
    llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": None,
    }
)
