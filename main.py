import os
from dotenv import load_dotenv

# Load your OpenAI API key
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Import all agents
from agents.supervisor_agent import supervisor_agent
from agents.intake_agent import intake_agent
from agents.classification_agent import classification_agent
from agents.assignment_agent import assignment_agent
from agents.monitoring_agent import monitoring_agent
from agents.learning_agent import learning_agent
from agents.human_operator import human_operator

def chat_with_agent(agent, message):
    response = agent.generate_reply([{"role": "user", "content": message}])
    print(f"[{agent.name}] {response}\n")


def main():
    message = "User reports: 'Can’t access the internal dashboard, getting 403 error.'"

    chat_with_agent(supervisor_agent, message)
    chat_with_agent(intake_agent, message)
    chat_with_agent(classification_agent, message)
    chat_with_agent(assignment_agent, message)
    chat_with_agent(monitoring_agent, message)
    chat_with_agent(learning_agent, message)
    chat_with_agent(human_operator, message)

if __name__ == "__main__":
    main()
