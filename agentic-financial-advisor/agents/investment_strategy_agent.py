"""
investment_strategy_agent.py
Defines the Investment Strategy Agent for providing investment recommendations.
"""

from autogen import AssistantAgent
from config.llm_config import llm_config

# Create the Investment Strategy Agent with specialized system message
investment_strategy_agent = AssistantAgent(
    name="InvestmentStrategyAgent",
    llm_config=llm_config,
    system_message=(
        "You are an investment advisor. "
        "Suggest short-term and long-term investments with justification."
    )
)
