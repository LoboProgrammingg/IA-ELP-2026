import json
import pickle
from pathlib import Path
from typing import List, Dict, Any
import faiss
import numpy as np
import google.generativeai as genai
from .text_splitter import TextChunk
from ..config import Config

class ELPRetriever:
    def __init__(self):
        self.embedding_model = None
        self.index = None
        self.metadata_store = []
        self.chunk_store = []
    
    def initialize_gemini_embeddings(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.embedding_model = genai.embed_content
    
    def generate_embeddings(self, chunks: List[TextChunk]) -> np.ndarray:
        if not self.embedding_model:
            self.initialize_gemini_embeddings()
        
        texts = [chunk.content for chunk in chunks]
        embeddings = []
        
        for text in texts:
            try:
                result = self.embedding_model(
                    model="models/embedding-001",
                    content=text,
                    task_type="retrieval_document"
                )
                embeddings.append(result['embedding'])
            except Exception as e:
                print(f"Erro ao gerar embedding: {e}")
                embeddings.append(np.zeros(768))
        
        return np.array(embeddings).astype('float32')
    
    def build_faiss_index(self, chunks: List[TextChunk]):
        embeddings = self.generate_embeddings(chunks)
        
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        
        self.chunk_store = chunks
        self.metadata_store = [
            {
                "chunk_id": chunk.chunk_id,
                "source": chunk.metadata["source"],
                "unidade": chunk.metadata["unidade"],
                "content_preview": chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content
            }
            for chunk in chunks
        ]
    
    def save_index(self):
        Config.ensure_directories()
        
        faiss.write_index(self.index, str(Config.FAISS_INDEX_PATH))
        
        with open(Config.METADATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.metadata_store, f, ensure_ascii=False, indent=2)
        
        chunks_data = [
            {
                "chunk_id": chunk.chunk_id,
                "content": chunk.content,
                "metadata": chunk.metadata
            }
            for chunk in self.chunk_store
        ]
        
        chunks_path = Config.VECTOR_STORE_DIR / "chunks.json"
        with open(chunks_path, 'w', encoding='utf-8') as f:
            json.dump(chunks_data, f, ensure_ascii=False, indent=2)
    
    def load_index(self):
        if not Config.FAISS_INDEX_PATH.exists():
            raise FileNotFoundError("Índice FAISS não encontrado. Execute o pipeline de ingestão primeiro.")
        
        self.index = faiss.read_index(str(Config.FAISS_INDEX_PATH))
        
        with open(Config.METADATA_PATH, 'r', encoding='utf-8') as f:
            self.metadata_store = json.load(f)
        
        chunks_path = Config.VECTOR_STORE_DIR / "chunks.json"
        with open(chunks_path, 'r', encoding='utf-8') as f:
            chunks_data = json.load(f)
        
        self.chunk_store = [
            TextChunk(
                content=chunk["content"],
                metadata=chunk["metadata"],
                chunk_id=chunk["chunk_id"]
            )
            for chunk in chunks_data
        ]
    
    def search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        if not self.embedding_model:
            self.initialize_gemini_embeddings()
        
        query_embedding = self.generate_embeddings([TextChunk(query, {}, "query")])[0]
        faiss.normalize_L2(query_embedding.reshape(1, -1))
        
        scores, indices = self.index.search(query_embedding.reshape(1, -1), k)
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < len(self.chunk_store):
                chunk = self.chunk_store[idx]
                results.append({
                    "content": chunk.content,
                    "metadata": chunk.metadata,
                    "score": float(score),
                    "chunk_id": chunk.chunk_id
                })
        
        return results
    
    def search_by_unidade(self, query: str, unidade: str, k: int = 3) -> List[Dict[str, Any]]:
        all_results = self.search(query, k * 3)
        
        filtered_results = [
            result for result in all_results
            if result["metadata"]["unidade"].lower() == unidade.lower()
        ]
        
        return filtered_results[:k]
