"""Configuration for open-source agents"""

# OpenAI API settings
OPENAI_API_KEY = "your-api-key"
OPENAI_MODEL = "gpt-4-turbo-preview"

# Agent settings
MAX_ITERATIONS = 10
TEMPERATURE = 0.7
TOOLS_ENABLED = True

# Logging settings
LOG_LEVEL = "INFO"
LOG_FILE = "agent.log"

# Memory settings
MEMORY_TYPE = "simple"  # Options: simple, vector, buffer
MEMORY_SIZE = 1000