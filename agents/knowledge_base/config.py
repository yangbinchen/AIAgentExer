from typing import Dict, Any
from pydantic import BaseModel

class KnowledgeBaseConfig(BaseModel):
    """Configuration for Knowledge Base"""
    model_name: str = "gpt-4"
    temperature: float = 0.3
    max_tokens: int = 1600
    embedding_model: str = "text-embedding-ada-002"
    knowledge_settings: Dict[str, Any] = {
        "chunk_size": 1000,
        "chunk_overlap": 200,
        "index_type": "faiss"
    }
    retrieval_config: Dict[str, Any] = {
        "top_k": 5,
        "similarity_threshold": 0.7,
        "rerank_results": True
    }
    update_policy: Dict[str, bool] = {
        "auto_update": True,
        "version_control": True,
        "backup_enabled": True
    }