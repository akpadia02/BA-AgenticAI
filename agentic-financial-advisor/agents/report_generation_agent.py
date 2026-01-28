# ============================================================================
# report_generation_agent.py
# Defines the Report Generation Agent for structured financial report creation
# This agent specializes in compiling analysis into professional reports
# ============================================================================

# Import the AssistantAgent class from AutoGen for creating an AI agent
# AssistantAgent is a specialized agent type designed for handling tasks
from autogen import AssistantAgent

# Import the shared LLM configuration from central config file
# This ensures all agents use the same model settings for consistency
from config.llm_config import llm_config

# ============================================================================
# Create the Report Generation Agent instance
# This agent is configured specifically for creating structured financial reports
# ============================================================================
report_generation_agent = AssistantAgent(
    # Agent name: Used to identify this agent in group conversations
    # This name will appear in logs and chat histories
    name="ReportGenerationAgent",
    
    # LLM configuration: Pass the shared configuration dictionary
    # Contains model type, API endpoint, temperature, and authentication details
    llm_config=llm_config,
    
    # System message: Defines the agent's role and expertise
    # This instruction shapes the agent's behavior and response style
    # The agent will focus on report generation as per this message
    system_message=(
        "Generate a structured investment report including "  # Main task
        "market overview, risk analysis, strategies, and conclusion."  # Report sections to include
    )
)
