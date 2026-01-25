from autogen import GroupChat, GroupChatManager, UserProxyAgent
from config.llm_config import llm_config

class FinancialAdvisorOrchestrator:

    def __init__(self, agents):
        self.user_proxy = UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False}
        )

        self.group_chat = GroupChat(
            agents=[self.user_proxy] + agents,
            messages=[],
            max_round=5,
            speaker_selection_method="round_robin"
        )

        self.manager = GroupChatManager(
            groupchat=self.group_chat,
            llm_config=llm_config
        )

    def run(self, query):
        self.user_proxy.initiate_chat(
            self.manager,
            message=query
        )
