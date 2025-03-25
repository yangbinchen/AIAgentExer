from typing import Dict, Any, List
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def validate_knowledge_input(data: Dict[str, Any]) -> bool:
    """Validate knowledge input data format"""
    required_fields = ['content', 'metadata', 'source']
    try:
        for field in required_fields:
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return False
        return True
    except Exception as e:
        logger.error(f"Error validating knowledge input: {str(e)}")
        return False

def process_chunk(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Process text into overlapping chunks for embedding"""
    chunks = []
    if len(text) <= chunk_size:
        return [text]
        
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

def calculate_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors"""
    try:
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5
        return dot_product / (norm1 * norm2)
    except Exception as e:
        logger.error(f"Error calculating similarity: {str(e)}")
        return 0.0