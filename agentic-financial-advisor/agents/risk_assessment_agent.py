from autogen import AssistantAgent
from config.llm_config import llm_config

risk_assessment_agent = AssistantAgent(
    name="RiskAssessmentAgent",
    llm_config=llm_config,
    system_message=(
        "You are a risk management expert. "
        "Assess market and investment risks as Low, Medium, or High."
    )
)
