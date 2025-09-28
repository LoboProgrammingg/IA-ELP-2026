import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.data_dir = self.project_root / "data"
        self.raw_data_dir = self.data_dir / "raw"
        self.processed_data_dir = self.data_dir / "processed"
        self.vector_store_dir = self.data_dir / "vector_store"
        
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        
        self._validate_config()
        self._ensure_directories()
    
    def _validate_config(self):
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY não encontrada nas variáveis de ambiente")
        
        if not self.tavily_api_key:
            print("AVISO: TAVILY_API_KEY não encontrada - funcionalidade de busca externa limitada")
    
    def _ensure_directories(self):
        for directory in [self.data_dir, self.raw_data_dir, self.processed_data_dir, self.vector_store_dir]:
            directory.mkdir(parents=True, exist_ok=True)
    
    def get_gemini_config(self) -> Dict[str, Any]:
        return {
            "api_key": self.gemini_api_key,
            "model": "gemini-1.5-pro",
            "embedding_model": "models/embedding-001"
        }
    
    def get_tavily_config(self) -> Dict[str, Any]:
        return {
            "api_key": self.tavily_api_key,
            "search_depth": "basic"
        }

config = Config()
