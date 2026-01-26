"""
report_generation_agent.py
Defines the Report Generation Agent for creating structured financial reports.
"""

from autogen import AssistantAgent
from config.llm_config import llm_config

# Create the Report Generation Agent with specialized system message
report_generation_agent = AssistantAgent(
    name="ReportGenerationAgent",
    llm_config=llm_config,
    system_message=(
        "Generate a structured investment report including "
        "market overview, risk analysis, strategies, and conclusion."
    )
)
