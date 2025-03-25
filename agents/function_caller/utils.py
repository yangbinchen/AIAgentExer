from typing import Dict, Any, Callable
import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: int = 1):
    """Decorator for retrying failed function calls"""
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Failed after {max_retries} attempts: {str(e)}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def validate_function_input(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """Validate function input against schema"""
    try:
        for field, field_type in schema.items():
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return False
            if not isinstance(data[field], field_type):
                logger.error(f"Invalid type for field {field}")
                return False
        return True
    except Exception as e:
        logger.error(f"Error validating function input: {str(e)}")
        return False

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Sanitize function input data"""
    sanitized = {}
    for key, value in data.items():
        if isinstance(value, str):
            # Basic string sanitization
            sanitized[key] = value.strip()
        elif isinstance(value, (int, float, bool)):
            sanitized[key] = value
        elif isinstance(value, dict):
            sanitized[key] = sanitize_input(value)
        elif isinstance(value, list):
            sanitized[key] = [sanitize_input({"item": v})["item"] for v in value]
        else:
            sanitized[key] = None
    return sanitized