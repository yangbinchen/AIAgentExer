from typing import Dict, Any, List
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def log_thought_process(thought: str, action: str, observation: str) -> None:
    """Log agent's thought process"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"[{timestamp}] Thought: {thought}")
    logger.info(f"[{timestamp}] Action: {action}")
    logger.info(f"[{timestamp}] Observation: {observation}")

def analyze_action_pattern(action_history: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze patterns in agent's actions"""
    patterns = {
        'common_actions': {},
        'success_rate': 0.0,
        'average_steps': 0
    }
    
    if not action_history:
        return patterns
        
    # Count action frequencies
    for action in action_history:
        action_type = action.get('type', 'unknown')
        patterns['common_actions'][action_type] = patterns['common_actions'].get(action_type, 0) + 1
    
    # Calculate success rate
    successful_actions = sum(1 for action in action_history if action.get('success', False))
    patterns['success_rate'] = successful_actions / len(action_history)
    
    # Calculate average steps per task
    patterns['average_steps'] = len(action_history) / max(1, len(set(action['task_id'] for action in action_history)))
    
    return patterns

def validate_action(action: Dict[str, Any]) -> bool:
    """Validate action format and parameters"""
    required_fields = ['type', 'parameters', 'task_id']
    try:
        for field in required_fields:
            if field not in action:
                logger.error(f"Missing required field: {field}")
                return False
        return True
    except Exception as e:
        logger.error(f"Error validating action: {str(e)}")
        return False