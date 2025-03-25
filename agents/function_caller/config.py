from typing import Dict, Any
from pydantic import BaseModel

class FunctionCallerConfig(BaseModel):
    """Configuration for Function Caller"""
    model_name: str = "gpt-4"
    temperature: float = 0.2
    max_tokens: int = 1500
    function_timeout: int = 30  # seconds
    retry_attempts: int = 3
    error_handling: Dict[str, Any] = {
        "log_errors": True,
        "raise_exceptions": False,
        "retry_on_failure": True
    }
    validation_rules: Dict[str, bool] = {
        "type_check": True,
        "schema_validation": True,
        "input_sanitization": True
    }