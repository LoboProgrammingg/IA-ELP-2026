import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class TextChunk:
    content: str
    metadata: Dict[str, str]
    chunk_id: str

class ELPTextSplitter:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.unidade_pattern = re.compile(r'^## Unidade (.+)$', re.MULTILINE)
    
    def extract_unidades_from_markdown(self, content: str) -> List[Tuple[str, int, int]]:
        unidade_matches = []
        for match in self.unidade_pattern.finditer(content):
            unidade_name = match.group(1).strip()
            start_pos = match.start()
            end_pos = match.end()
            unidade_matches.append((unidade_name, start_pos, end_pos))
        return unidade_matches
    
    def split_text_by_unidade(self, content: str, filename: str) -> List[TextChunk]:
        unidade_matches = self.extract_unidades_from_markdown(content)
        chunks = []
        
        if not unidade_matches:
            chunks.append(TextChunk(
                content=content[:self.chunk_size],
                metadata={"source": filename, "unidade": "Geral"},
                chunk_id=f"{filename}_general_0"
            ))
            return chunks
        
        for i, (unidade_name, start_pos, end_pos) in enumerate(unidade_matches):
            next_start = unidade_matches[i + 1][1] if i + 1 < len(unidade_matches) else len(content)
            unidade_content = content[end_pos:next_start].strip()
            
            if len(unidade_content) <= self.chunk_size:
                chunks.append(TextChunk(
                    content=unidade_content,
                    metadata={"source": filename, "unidade": unidade_name},
                    chunk_id=f"{filename}_{unidade_name}_{i}"
                ))
            else:
                sub_chunks = self._split_large_content(unidade_content, filename, unidade_name, i)
                chunks.extend(sub_chunks)
        
        return chunks
    
    def _split_large_content(self, content: str, filename: str, unidade: str, base_index: int) -> List[TextChunk]:
        chunks = []
        start = 0
        chunk_index = 0
        
        while start < len(content):
            end = min(start + self.chunk_size, len(content))
            
            if end < len(content):
                end = self._find_sentence_boundary(content, start, end)
            
            chunk_content = content[start:end].strip()
            if chunk_content:
                chunks.append(TextChunk(
                    content=chunk_content,
                    metadata={"source": filename, "unidade": unidade},
                    chunk_id=f"{filename}_{unidade}_{base_index}_{chunk_index}"
                ))
                chunk_index += 1
            
            start = max(start + self.chunk_size - self.chunk_overlap, end)
        
        return chunks
    
    def _find_sentence_boundary(self, text: str, start: int, end: int) -> int:
        sentence_endings = ['.', '!', '?', '\n\n']
        for i in range(end - 1, start, -1):
            if text[i] in sentence_endings:
                return i + 1
        return end
    
    def process_markdown_files(self, processed_dir: Path) -> List[TextChunk]:
        all_chunks = []
        
        for md_file in processed_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                chunks = self.split_text_by_unidade(content, md_file.stem)
                all_chunks.extend(chunks)
                
            except Exception as e:
                print(f"Erro ao processar {md_file}: {e}")
        
        return all_chunks
