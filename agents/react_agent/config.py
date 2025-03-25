from typing import Dict, Any
from pydantic import BaseModel

class ReactAgentConfig(BaseModel):
    """Configuration for React Agent"""
    model_name: str = "gpt-4"
    temperature: float = 0.5
    max_tokens: int = 1800
    max_iterations: int = 10
    thought_process: Dict[str, bool] = {
        "log_thoughts": True,
        "save_history": True,
        "analyze_patterns": True
    }
    action_config: Dict[str, Any] = {
        "timeout": 60,  # seconds
        "max_retries": 3,
        "parallel_actions": False
    }
    memory_settings: Dict[str, Any] = {
        "use_memory": True,
        "memory_window": 5,
        "priority_threshold": 0.7
    }