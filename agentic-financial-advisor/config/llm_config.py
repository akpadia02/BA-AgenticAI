# ============================================================================
# llm_config.py
# Central configuration file for Large Language Model (LLM) settings
# This configuration is used by all AutoGen agents in the application
# ============================================================================

# Define the LLM configuration dictionary that will be shared across all agents
# This ensures consistent model behavior and settings throughout the application
llm_config = {
    # Model selection: Using Llama 3.2 model
    # This is an open-source model compatible with Ollama
    "model": "llama3.2",
    
    # API authentication key
    # Set to "ollama" for local Ollama deployment
    # Can be changed to actual API key if using cloud-based LLM service
    "api_key": "ollama",
    
    # Base URL for the LLM API endpoint
    # Points to local Ollama service running on port 11434
    # Format: http://localhost:11434/v1
    # This assumes Ollama is running locally on the default port
    "base_url": "http://localhost:11434/v1",
    
    # Temperature parameter controls model creativity/randomness
    # Range: 0.0 to 1.0
    # 0.3: Low temperature = more deterministic, focused, consistent responses
    #      Good for financial analysis where we need reliable, predictable outputs
    # Higher values (>0.7): More creative but less reliable responses
    "temperature": 0.3
}
