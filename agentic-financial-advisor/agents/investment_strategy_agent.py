from autogen import AssistantAgent
from config.llm_config import llm_config

investment_strategy_agent = AssistantAgent(
    name="InvestmentStrategyAgent",
    llm_config=llm_config,
    system_message=(
        "You are an investment advisor. "
        "Suggest short-term and long-term investments with justification."
    )
)
