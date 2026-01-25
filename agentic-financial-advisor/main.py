from agents.market_analysis_agent import market_analysis_agent
from agents.risk_assessment_agent import risk_assessment_agent
from agents.investment_strategy_agent import investment_strategy_agent
from agents.report_generation_agent import report_generation_agent
from orchestrator.financial_advisor_orchestrator import FinancialAdvisorOrchestrator

def main():
    agents = [
        market_analysis_agent,
        risk_assessment_agent,
        investment_strategy_agent,
        report_generation_agent
    ]

    orchestrator = FinancialAdvisorOrchestrator(agents)

    orchestrator.run(
        "Analyze current market scenario and suggest "
        "short-term and long-term investments with risk analysis."
    )

if __name__ == "__main__":
    main()
