from typing import Dict, Any, List, Callable, Optional
import logging
from .config import FunctionCallerConfig
from .utils import retry_on_failure, validate_function_input, sanitize_input

logger = logging.getLogger(__name__)

class FunctionCaller:
    """Core class for function calling and management"""
    
    def __init__(self, config: FunctionCallerConfig = None):
        self.config = config or FunctionCallerConfig()
        self.registered_functions: Dict[str, Callable] = {}
        self.function_schemas: Dict[str, Dict[str, Any]] = {}
        
    def register_function(self, name: str, func: Callable, schema: Dict[str, Any]) -> None:
        """Register a function with its schema"""
        if name in self.registered_functions:
            logger.warning(f"Function {name} already registered, overwriting")
        self.registered_functions[name] = func
        self.function_schemas[name] = schema
        
    @retry_on_failure(max_retries=3)
    async def call_function(self, name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Call a registered function with parameters"""
        if name not in self.registered_functions:
            raise ValueError(f"Function {name} not registered")
            
        # Validate and sanitize input
        if not validate_function_input(params, self.function_schemas[name]):
            raise ValueError(f"Invalid parameters for function {name}")
        sanitized_params = sanitize_input(params)
        
        try:
            result = await self.registered_functions[name](**sanitized_params)
            return {
                'status': 'success',
                'result': result
            }
        except Exception as e:
            logger.error(f"Error calling function {name}: {str(e)}")
            return {
                'status': 'error',
                'error': str(e)
            }
            
    def get_registered_functions(self) -> List[str]:
        """Get list of registered function names"""
        return list(self.registered_functions.keys())
    
    def get_function_schema(self, name: str) -> Optional[Dict[str, Any]]:
        """Get schema for a registered function"""
        return self.function_schemas.get(name)
    
    def validate_schema(self, schema: Dict[str, Any]) -> bool:
        """Validate function schema format"""
        required_fields = ['parameters', 'returns']
        try:
            for field in required_fields:
                if field not in schema:
                    logger.error(f"Missing required field in schema: {field}")
                    return False
            return True
        except Exception as e:
            logger.error(f"Error validating schema: {str(e)}")
            return False