"""Example script demonstrating the usage of ReactAgent.

This script shows how to initialize and use the ReactAgent to
solve complex tasks using the ReAct (Reasoning and Acting) paradigm.
"""

import asyncio
import os
from dotenv import load_dotenv
from react_agent import ReactAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenAI API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('OPENAI_API_KEY environment variable is not set')
    
    # Initialize the ReAct agent
    agent = ReactAgent(api_key)
    
    # Example: Solve a complex task using ReAct paradigm
    task = {
        'question': 'What is the population of the capital city of France, '
                   'and how does it compare to Tokyo?',
        'tools_available': ['search_web', 'calculate', 'compare_data']
    }
    
    try:
        # Process the task using ReAct approach
        result = await agent.solve_task(task)
        print('Task completed successfully')
        print('Answer:', result)
        
        # Show the reasoning steps
        steps = agent.get_reasoning_steps()
        print('\nReasoning steps:')
        for i, step in enumerate(steps, 1):
            print(f'{i}. {step}')
    except NotImplementedError:
        print('Note: ReAct agent implementation is not yet complete')
    except Exception as e:
        print(f'Error solving task: {e}')

if __name__ == '__main__':
    asyncio.run(main())