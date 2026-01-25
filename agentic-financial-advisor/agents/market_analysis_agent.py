from autogen import AssistantAgent
from config.llm_config import llm_config

market_analysis_agent = AssistantAgent(
    name="MarketAnalysisAgent",
    llm_config=llm_config,
    system_message=(
        "You are a financial market analyst. "
        "Analyze current market trends and macroeconomic conditions."
    )
)
