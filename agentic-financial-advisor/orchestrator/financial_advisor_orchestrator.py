# ============================================================================
# financial_advisor_orchestrator.py
# Orchestrates the interaction between multiple financial advisor agents
# Uses AutoGen's GroupChat to manage collaborative agent communication
# ============================================================================

# Import GroupChat class for managing multi-agent conversations
from autogen import GroupChat

# Import GroupChatManager to manage and facilitate group chat interactions
from autogen import GroupChatManager

# Import UserProxyAgent which represents the user in the conversation
# Acts as a user interface agent for initiating and managing queries
from autogen import UserProxyAgent

# Import the shared LLM configuration used across all agents
from config.llm_config import llm_config

class FinancialAdvisorOrchestrator:
    """
    Orchestrator class that manages a collaborative group of financial advisor agents.
    
    This class:
    - Initializes and coordinates multiple specialized agents
    - Creates a group chat environment for agent collaboration
    - Manages agent interactions and communication flow
    - Processes user queries through multiple agent perspectives
    
    Attributes:
        user_proxy (UserProxyAgent): Agent representing the user in conversations
        group_chat (GroupChat): Multi-agent conversation environment
        manager (GroupChatManager): Manager for coordinating group chat interactions
    """

    def __init__(self, agents):
        """
        Initialize the orchestrator with a list of agents.
        
        This method:
        1. Creates a user proxy agent (simulates user in the conversation)
        2. Sets up a group chat with all agents
        3. Initializes the group chat manager for communication coordination
        
        Args:
            agents (list): List of AutoGen AssistantAgent instances for financial analysis.
                          Examples: market_analysis_agent, risk_assessment_agent, etc.
        
        Workflow:
            - Creates UserProxyAgent that doesn't require human input
            - Combines UserProxyAgent with all provided agents
            - Configures group chat with round-robin speaker selection
            - Sets max conversation rounds to 5 for focused analysis
        """
        
        # Step 1: Create a UserProxyAgent instance
        # This agent represents the user in the group chat conversation
        # It initiates the chat and manages the overall flow
        self.user_proxy = UserProxyAgent(
            # Name identifier for the user proxy agent
            name="UserProxy",
            
            # Human input mode setting
            # "NEVER" means the agent won't wait for human input
            # Allows fully automated conversation between agents
            human_input_mode="NEVER",
            
            # Code execution configuration
            # use_docker: False means code will execute locally without Docker
            # This setting allows agents to run code if needed
            code_execution_config={"use_docker": False}
        )

        # Step 2: Set up the group chat environment
        # GroupChat creates a conversation space where multiple agents can interact
        self.group_chat = GroupChat(
            # List of agents participating in the group chat
            # Includes the UserProxy agent first, followed by all specialist agents
            agents=[self.user_proxy] + agents,
            
            # Initialize message list as empty
            # Messages will be added as agents communicate
            messages=[],
            
            # Maximum number of conversation rounds
            # Set to 5 to keep the conversation focused and finite
            # After 5 rounds, the conversation will terminate
            max_round=5,
            
            # Speaker selection method for agent turns
            # "round_robin" means agents take turns in order
            # Ensures all agents get equal opportunity to contribute
            speaker_selection_method="round_robin"
        )

        # Step 3: Create the GroupChatManager
        # This manager handles the actual conversation coordination
        # It decides when agents speak and how they interact
        self.manager = GroupChatManager(
            # The group chat instance to manage
            groupchat=self.group_chat,
            
            # LLM configuration for the manager
            # Uses the same configuration as all agents for consistency
            llm_config=llm_config
        )

    def run(self, query):
        """
        Initiate and run the group chat with the given financial analysis query.
        
        This method:
        1. Takes a user query about financial analysis
        2. Passes it to all agents through the orchestrator
        3. Facilitates automated conversation between agents
        4. Returns comprehensive analysis from multiple perspectives
        
        Args:
            query (str): The financial analysis query to process.
                        Example: "Analyze current market scenario and suggest 
                                short-term and long-term investments with risk analysis."
        
        Workflow:
            - UserProxy initiates chat with the GroupChatManager
            - Query is broadcast to all agents in the group
            - Each agent (in round-robin order) provides their expert perspective:
              * Market Analysis Agent analyzes market trends
              * Risk Assessment Agent evaluates risks
              * Investment Strategy Agent recommends investments
              * Report Generation Agent compiles results
            - Conversation continues for up to 5 rounds
            - Agents collaborate to provide comprehensive financial insights
        """
        
        # Initiate the group chat conversation
        # This starts the multi-agent interaction workflow
        self.user_proxy.initiate_chat(
            # The manager that will coordinate the conversation
            self.manager,
            
            # The initial query/message to send to all agents
            # This is the financial analysis question that agents will respond to
            message=query
        )
