"""Utility functions and tools for open-source agents"""
from typing import Any, Dict, List

def create_tool(name: str, description: str, func: callable) -> Dict[str, Any]:
    """Create a tool configuration for agents"""
    return {
        "name": name,
        "description": description,
        "function": func
    }

def format_result(result: Any) -> str:
    """Format the result of a tool execution"""
    return str(result)

def parse_task(task: str) -> List[str]:
    """Parse a task into subtasks"""
    # TODO: Implement task parsing logic
    return [task]

def validate_tool_result(result: str) -> bool:
    """Validate the result of a tool execution"""
    return bool(result)

def create_memory_store(memory_type: str = "simple", size: int = 1000) -> List[Any]:
    """Create a memory store for the agent"""
    return []

def update_memory(memory: List[Any], item: Any) -> List[Any]:
    """Update the agent's memory with a new item"""
    memory.append(item)
    return memory[:1000]  # Keep last 1000 items