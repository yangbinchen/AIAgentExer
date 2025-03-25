"""Example script demonstrating the usage of FunctionCallerAgent.

This script shows how to initialize and use the FunctionCallerAgent to
handle function calling tasks with OpenAI's API.
"""

import asyncio
import os
from dotenv import load_dotenv
from function_caller import FunctionCallerAgent

# Example function that could be called by the agent
def get_weather(location: str, unit: str = 'celsius') -> str:
    """Get weather information for a location.
    
    Args:
        location: City or location name
        unit: Temperature unit ('celsius' or 'fahrenheit')
        
    Returns:
        Weather information as a string
    """
    # This is a mock implementation
    return f'Weather in {location}: 25бу{unit[0].upper()}'

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenAI API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('OPENAI_API_KEY environment variable is not set')
    
    # Initialize the Function Caller agent
    agent = FunctionCallerAgent(api_key)
    
    # Register the function that can be called
    agent.register_function(get_weather)
    
    # Example: Process a user query that might require calling the weather function
    user_query = "What's the weather like in Tokyo?"
    
    try:
        # Process the query and get response
        response = await agent.process_query(user_query)
        print(f'Agent response: {response}')
    except NotImplementedError:
        print('Note: Function calling is not yet implemented')
    except Exception as e:
        print(f'Error processing query: {e}')

if __name__ == '__main__':
    asyncio.run(main())