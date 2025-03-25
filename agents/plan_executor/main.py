"""Example script demonstrating the usage of PlanExecutorAgent.

This script shows how to initialize and use the PlanExecutorAgent to
break down complex tasks into executable steps and manage their execution.
"""

import asyncio
import os
from dotenv import load_dotenv
from plan_executor import PlanExecutorAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenAI API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('OPENAI_API_KEY environment variable is not set')
    
    # Initialize the Plan Executor agent
    agent = PlanExecutorAgent(api_key)
    
    # Example: Create and execute a plan for a data analysis task
    task = {
        'objective': 'Analyze customer feedback data',
        'steps': [
            'Load and clean the data',
            'Perform sentiment analysis',
            'Generate insights report'
        ]
    }
    
    try:
        # Execute the plan
        result = await agent.execute_plan(task)
        print('Plan execution completed successfully')
        print('Results:', result)
    except NotImplementedError:
        print('Note: Plan execution is not yet implemented')
    except Exception as e:
        print(f'Error executing plan: {e}')

if __name__ == '__main__':
    asyncio.run(main())