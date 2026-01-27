# Agentic Financial Advisor

An intelligent, multi-agent financial advisory system built with AutoGen that provides comprehensive market analysis, risk assessment, investment strategies, and structured reports using AI-powered agents.

## Features

- **Multi-Agent Architecture**: Specialized agents for different aspects of financial analysis
  - Market Analysis Agent: Analyzes current market trends and macroeconomic conditions
  - Risk Assessment Agent: Evaluates investment and market risks (Low, Medium, High)
  - Investment Strategy Agent: Provides short-term and long-term investment recommendations
  - Report Generation Agent: Creates structured financial reports

- **Real-Time Data Integration**: Fetches live market data using Yahoo Finance API
- **AI-Powered Orchestration**: Uses AutoGen's GroupChat for seamless agent collaboration
- **Local LLM Support**: Runs on local Ollama models for privacy and cost-efficiency

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.2 model pulled in Ollama (`ollama pull llama3.2`)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agentic-financial-advisor
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

4. Verify Llama 3.2 model is available:
   ```bash
   ollama list
   ```
   Should show `llama3.2` in the list.

## Usage

### Running the Application

Execute the main script to run a sample financial analysis:

```bash
python main.py
```

This will initiate a multi-agent conversation analyzing the current market scenario and providing investment recommendations with risk analysis.

### Customizing Queries

To analyze different financial scenarios, modify the query in `main.py`:

```python
# In main.py, change the query string
orchestrator.run(
    "Your custom financial analysis query here"
)
```

Examples of queries:
- "Analyze the tech sector performance and suggest investments"
- "Assess cryptocurrency market risks for 2024"
- "Provide portfolio diversification strategies for retirement planning"

### Project Structure

```
agentic-financial-advisor/
├── main.py                          # Main entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── agents/                          # Specialized AI agents
│   ├── market_analysis_agent.py
│   ├── risk_assessment_agent.py
│   ├── investment_strategy_agent.py
│   └── report_generation_agent.py
├── config/
│   └── llm_config.py               # LLM configuration for Ollama
├── orchestrator/
│   └── financial_advisor_orchestrator.py  # Agent orchestration logic
└── tools/
    └── market_data_tool.py         # Market data fetching utility
```

## Configuration

The system uses Ollama with Llama 3.2 by default. To modify the LLM configuration, edit `config/llm_config.py`:

```python
llm_config = {
    "model": "your-model-name",  # Change model here
    "api_key": "ollama",
    "base_url": "http://localhost:11434/v1",
    "temperature": 0.3
}
```

## Dependencies

- **pyautogen**: Multi-agent conversation framework
- **yfinance**: Yahoo Finance API for market data
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization

## Troubleshooting

### Common Issues

1. **Ollama Connection Error**: Ensure Ollama is running on `http://localhost:11434`
2. **Model Not Found**: Run `ollama pull llama3.2` to download the model
3. **Import Errors**: Verify all dependencies are installed with `pip install -r requirements.txt`


