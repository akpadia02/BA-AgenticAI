from agents.market_analysis_agent import market_analysis_agent
from agents.risk_assessment_agent import risk_assessment_agent
from agents.investment_strategy_agent import investment_strategy_agent
from agents.report_generation_agent import report_generation_agent
from orchestrator.financial_advisor_orchestrator import FinancialAdvisorOrchestrator

def main():
    """
    Main entry point for the Agentic Financial Advisor application.
    Initializes agents, creates an orchestrator, and runs the financial analysis query.
    """
    # List of specialized agents for financial analysis
    agents = [
        market_analysis_agent,
        risk_assessment_agent,
        investment_strategy_agent,
        report_generation_agent
    ]

    # Create orchestrator to manage agent interactions
    orchestrator = FinancialAdvisorOrchestrator(agents)

    # Run the analysis with a sample query
    orchestrator.run(
        "Analyze current market scenario and suggest "
        "short-term and long-term investments with risk analysis."
    )

if __name__ == "__main__":
    main()
