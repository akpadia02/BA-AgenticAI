# ============================================================================
# risk_assessment_agent.py
# Defines the Risk Assessment Agent for evaluating financial risks
# This agent specializes in identifying and classifying investment risks
# ============================================================================

# Import the AssistantAgent class from AutoGen for creating an AI agent
# AssistantAgent is a specialized agent type designed for handling tasks
from autogen import AssistantAgent

# Import the shared LLM configuration from central config file
# This ensures all agents use the same model settings for consistency
from config.llm_config import llm_config

# ============================================================================
# Create the Risk Assessment Agent instance
# This agent is configured specifically for risk evaluation and analysis
# ============================================================================
risk_assessment_agent = AssistantAgent(
    # Agent name: Used to identify this agent in group conversations
    # This name will appear in logs and chat histories
    name="RiskAssessmentAgent",
    
    # LLM configuration: Pass the shared configuration dictionary
    # Contains model type, API endpoint, temperature, and authentication details
    llm_config=llm_config,
    
    # System message: Defines the agent's role and expertise
    # This instruction shapes the agent's behavior and response style
    # The agent will focus on risk management and assessment as per this message
    system_message=(
        "You are a risk management expert. "  # Role definition
        "Assess market and investment risks as Low, Medium, or High."  # Risk classification task
    )
)
