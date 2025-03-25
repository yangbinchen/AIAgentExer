from typing import Dict, Any

class PPTCreatorConfig:
    """Configuration for PPT Creator Agent"""
    
    def __init__(self):
        self.openai_model = "gpt-4-1106-preview"  # ʹ������GPT-4ģ��
        self.dalle_model = "dall-e-3"  # ʹ��DALL��E 3ģ��
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