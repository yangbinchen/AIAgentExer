"""Main entry point for running open-source agents"""
from typing import List
from .core import AutoGPTAgent, BabyAGIAgent

def run_autogpt(task: str) -> List[str]:
    """Run AutoGPT agent on a given task"""
    agent = AutoGPTAgent()
    
    # Add default tools
    agent.add_tool({
        "name": "search",
        "description": "Search the internet for information",
        "function": lambda x: f"Searching for {x}..."
    })
    
    # Execute the task
    thoughts = agent.think(task)
    results = []
    
    for thought in thoughts:
        result = agent.act(thought)
        agent.observe(result)
        results.append(result)
    
    return results

def run_babyagi(task: str) -> List[str]:
    """Run BabyAGI agent on a given task"""
    agent = BabyAGIAgent()
    
    # Add default tools
    agent.add_tool({
        "name": "execute",
        "description": "Execute a subtask",
        "function": lambda x: f"Executing {x}..."
    })
    
    # Execute the task
    thoughts = agent.think(task)
    results = []
    
    for thought in thoughts:
        result = agent.act(thought)
        agent.observe(result)
        results.append(result)
    
    return results

def main():
    """Example usage of open-source agents"""
    # Example task for AutoGPT
    print("Running AutoGPT...")
    results = run_autogpt("Find information about AI agents")
    print("AutoGPT Results:", results)
    
    # Example task for BabyAGI
    print("\nRunning BabyAGI...")
    results = run_babyagi("Create a learning plan for AI agents")
    print("BabyAGI Results:", results)

if __name__ == "__main__":
    main()