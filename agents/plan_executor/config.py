from typing import Dict, Any
from pydantic import BaseModel

class PlanExecutorConfig(BaseModel):
    """Configuration for Plan Executor"""
    model_name: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 2000
    inventory_threshold: Dict[str, Any] = {
        "low_stock": 20,
        "high_stock": 80,
        "reorder_point": 30
    }
    monitoring_interval: int = 3600  # in seconds
    performance_metrics: Dict[str, bool] = {
        "stock_turnover": True,
        "order_fulfillment": True,
        "inventory_accuracy": True
    }