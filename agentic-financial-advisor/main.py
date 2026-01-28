# ============================================================================
# main.py
# Main entry point for the Agentic Financial Advisor application
# Coordinates multiple specialized AI agents to provide comprehensive financial analysis
# ============================================================================

# Import all specialized financial advisor agents from their respective modules
from agents.market_analysis_agent import market_analysis_agent  # Agent for market trend analysis
from agents.risk_assessment_agent import risk_assessment_agent  # Agent for risk evaluation
from agents.investment_strategy_agent import investment_strategy_agent  # Agent for investment recommendations
from agents.report_generation_agent import report_generation_agent  # Agent for structured report generation
from orchestrator.financial_advisor_orchestrator import FinancialAdvisorOrchestrator  # Orchestrator class to manage agent interactions

def main():
    """
    Main entry point for the Agentic Financial Advisor application.
    This function:
    1. Initializes all specialized financial advisor agents
    2. Creates an orchestrator to manage agent interactions
    3. Runs the financial analysis workflow with a predefined query
    4. The agents collaborate to provide comprehensive financial insights
    """
    # Step 1: Create a list of all specialized agents for financial analysis
    # Each agent has a specific role:
    # - market_analysis_agent: Analyzes market trends and macroeconomic conditions
    # - risk_assessment_agent: Evaluates investment and market risks
    # - investment_strategy_agent: Suggests appropriate investment strategies
    # - report_generation_agent: Compiles all analysis into a structured report
    agents = [
        market_analysis_agent,
        risk_assessment_agent,
        investment_strategy_agent,
        report_generation_agent
    ]

    # Step 2: Create an orchestrator instance to manage the group chat
    # The orchestrator handles:
    # - Agent registration and initialization
    # - Group chat setup with round-robin speaker selection
    # - Communication coordination between agents
    # - Maximum of 5 rounds of conversation for focused analysis
    orchestrator = FinancialAdvisorOrchestrator(agents)

    # Step 3: Execute the financial analysis workflow
    # Send the analysis query to all agents through the orchestrator
    # The query asks for:
    # - Current market scenario analysis
    # - Short-term and long-term investment suggestions
    # - Comprehensive risk analysis and assessment
    orchestrator.run(
        "Analyze current market scenario and suggest "
        "short-term and long-term investments with risk analysis."
    )

# Program entry point - ensures main() only runs when script is executed directly
if __name__ == "__main__":
    main()
