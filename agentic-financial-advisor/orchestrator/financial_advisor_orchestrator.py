"""
financial_advisor_orchestrator.py
Orchestrates the interaction between multiple financial advisor agents using AutoGen's GroupChat.
"""

from autogen import GroupChat, GroupChatManager, UserProxyAgent
from config.llm_config import llm_config

class FinancialAdvisorOrchestrator:
    """
    Orchestrator class that manages a group chat of financial advisor agents.
    Handles the coordination and communication between specialized agents.
    """

    def __init__(self, agents):
        """
        Initialize the orchestrator with a list of agents.

        Args:
            agents (list): List of AutoGen AssistantAgent instances for financial analysis.
        """
        # Create a user proxy agent that doesn't require human input
        self.user_proxy = UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False}
        )

        # Set up group chat with all agents including the user proxy
        self.group_chat = GroupChat(
            agents=[self.user_proxy] + agents,
            messages=[],
            max_round=5,
            speaker_selection_method="round_robin"
        )

        # Create group chat manager to handle the conversation
        self.manager = GroupChatManager(
            groupchat=self.group_chat,
            llm_config=llm_config
        )

    def run(self, query):
        """
        Initiate and run the group chat with the given query.

        Args:
            query (str): The financial analysis query to process.
        """
        self.user_proxy.initiate_chat(
            self.manager,
            message=query
        )
