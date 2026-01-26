"""
market_analysis_agent.py
Defines the Market Analysis Agent for analyzing financial market trends and conditions.
"""

from autogen import AssistantAgent
from config.llm_config import llm_config

# Create the Market Analysis Agent with specialized system message
market_analysis_agent = AssistantAgent(
    name="MarketAnalysisAgent",
    llm_config=llm_config,
    system_message=(
        "You are a financial market analyst. "
        "Analyze current market trends and macroeconomic conditions."
    )
)
