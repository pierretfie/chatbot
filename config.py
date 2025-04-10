import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    # Model paths
    TINYLLAMA_PATH: str = os.path.expanduser('~/tinyllama/tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf')
    PIPER_DIR: str = os.path.expanduser('~/piper_models/piper')
    PIPER_MODEL_PATH: str = os.path.expanduser('~/piper_models/en_GB-jenny_dioco-medium/en_GB-jenny_dioco-medium.onnx')
    
    # Audio settings
    SAMPLE_RATE: str = '22050'
    
    # Model settings
    CONTEXT_SIZE: int = 1024
    MAX_TOKENS: int = 512
    N_THREADS: int = 8
    
    # Conversation settings
    MAX_HISTORY: int = 10
    
    # Typing animation settings
    MIN_TYPING_DELAY: float = 0.01
    MAX_TYPING_DELAY: float = 0.03
    
    # Resource thresholds
    MEMORY_THRESHOLD: float = 80.0  # percentage
    GPU_MEMORY_THRESHOLD: float = 80.0  # percentage
    CPU_THRESHOLD: float = 80.0  # percentage
    
    # Error messages
    ERROR_MESSAGES = {
        'model_error': "I apologize, but I encountered an error while processing your request.",
        'resource_error': "I'm currently experiencing high resource usage. Please try again in a moment.",
        'file_not_found': "Required file not found: {path}",
        'initialization_error': "Failed to initialize: {error}"
    } 