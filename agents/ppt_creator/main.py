"""Example script demonstrating the usage of PPTCreatorAgent.

This script shows how to initialize and use the PPTCreatorAgent to
generate PowerPoint presentations automatically.
"""

import asyncio
import os
from dotenv import load_dotenv
import PPTCreatorAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenAI API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('OPENAI_API_KEY environment variable is not set')
    
    # Initialize the PPT Creator agent
    agent = PPTCreatorAgent(api_key)
    
    # Example: Create a presentation about AI
    topic = 'Artificial Intelligence: Past, Present and Future'
    num_slides = 10
    
    try:
        # Generate the presentation
        ppt_path = await agent.create_presentation(topic, num_slides)
        print(f'Successfully created presentation at: {ppt_path}')
    except NotImplementedError:
        print('Note: Presentation creation is not yet implemented')
    except Exception as e:
        print(f'Error creating presentation: {e}')

if __name__ == '__main__':
    asyncio.run(main())