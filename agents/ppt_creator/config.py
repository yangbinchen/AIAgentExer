from typing import Dict, Any

class PPTCreatorConfig:
    """Configuration for PPT Creator Agent"""
    
    def __init__(self):
        self.openai_model = "gpt-4-1106-preview"  # 使用最新GPT-4模型
        self.dalle_model = "dall-e-3"  # 使用DALL·E 3模型
        self.max_tokens = 4096
        self.temperature = 0.7
        
    def to_dict(self) -> Dict[Any, Any]:
        """Convert config to dictionary"""
        return self.__dict__
    
    @classmethod
    def from_dict(cls, config_dict: Dict[Any, Any]) -> 'PPTCreatorConfig':
        """Create config from dictionary"""
        config = cls()
        for key, value in config_dict.items():
            setattr(config, key, value)
        return config