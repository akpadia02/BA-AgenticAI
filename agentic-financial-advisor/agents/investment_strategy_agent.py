# ============================================================================
# investment_strategy_agent.py
# Defines the Investment Strategy Agent for investment recommendations
# This agent specializes in creating investment strategies with justifications
# ============================================================================

# Import the AssistantAgent class from AutoGen for creating an AI agent
# AssistantAgent is a specialized agent type designed for handling tasks
from autogen import AssistantAgent

# Import the shared LLM configuration from central config file
# This ensures all agents use the same model settings for consistency
from config.llm_config import llm_config

# ============================================================================
# Create the Investment Strategy Agent instance
# This agent is configured specifically for developing investment strategies
# ============================================================================
investment_strategy_agent = AssistantAgent(
    # Agent name: Used to identify this agent in group conversations
    # This name will appear in logs and chat histories
    name="InvestmentStrategyAgent",
    
    # LLM configuration: Pass the shared configuration dictionary
    # Contains model type, API endpoint, temperature, and authentication details
    llm_config=llm_config,
    
    # System message: Defines the agent's role and expertise
    # This instruction shapes the agent's behavior and response style
    # The agent will focus on investment advisory as per this message
    system_message=(
        "You are an investment advisor. "  # Role definition
        "Suggest short-term and long-term investments with justification."  # Primary responsibility
    )
)
