"""Example script demonstrating the usage of KnowledgeBaseAgent.

This script shows how to initialize and use the KnowledgeBaseAgent to
manage and query a knowledge base using OpenAI's API.
"""

import asyncio
import os
from dotenv import load_dotenv
from knowledge_base import KnowledgeBaseAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenAI API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('OPENAI_API_KEY environment variable is not set')
    
    # Initialize the Knowledge Base agent
    agent = KnowledgeBaseAgent(api_key)
    
    # Example: Add some knowledge to the base
    documents = [
        {
            'title': 'Python Programming',
            'content': 'Python is a high-level programming language...'
        },
        {
            'title': 'Machine Learning',
            'content': 'Machine learning is a subset of artificial intelligence...'
        }
    ]
    
    try:
        # Add documents to knowledge base
        await agent.add_documents(documents)
        
        # Query the knowledge base
        query = 'What is Python programming?'
        response = await agent.query(query)
        print(f'Query: {query}')
        print(f'Response: {response}')
    except NotImplementedError:
        print('Note: Knowledge base operations are not yet implemented')
    except Exception as e:
        print(f'Error processing knowledge base operation: {e}')

if __name__ == '__main__':
    asyncio.run(main())