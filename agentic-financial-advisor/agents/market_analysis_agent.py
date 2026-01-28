# ============================================================================
# market_analysis_agent.py
# Defines the Market Analysis Agent for financial market analysis
# This agent specializes in analyzing trends and macroeconomic conditions
# ============================================================================

# Import the AssistantAgent class from AutoGen for creating an AI agent
# AssistantAgent is a specialized agent type designed for handling tasks
from autogen import AssistantAgent

# Import the shared LLM configuration from central config file
# This ensures all agents use the same model settings for consistency
from config.llm_config import llm_config

# ============================================================================
# Create the Market Analysis Agent instance
# This agent is configured specifically for financial market analysis
# ============================================================================
market_analysis_agent = AssistantAgent(
    # Agent name: Used to identify this agent in group conversations
    # This name will appear in logs and chat histories
    name="MarketAnalysisAgent",
    
    # LLM configuration: Pass the shared configuration dictionary
    # Contains model type, API endpoint, temperature, and authentication details
    llm_config=llm_config,
    
    # System message: Defines the agent's role and expertise
    # This instruction shapes the agent's behavior and response style
    # The agent will focus on financial market analysis as per this message
    system_message=(
        "You are a financial market analyst. "  # Role definition
        "Analyze current market trends and macroeconomic conditions."  # Primary responsibility
    )
)
