from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent / "src"))

from elp_assistant.config import Config
from elp_assistant.core.data_processor import DataProcessor
from elp_assistant.core.text_splitter import ELPTextSplitter
from elp_assistant.core.retriever import ELPRetriever

def main():
    Config.validate_config()
    Config.ensure_directories()
    
    print("🚀 Iniciando pipeline completo de ingestão...")
    
    processor = DataProcessor()
    splitter = ELPTextSplitter(chunk_size=1000, chunk_overlap=200)
    retriever = ELPRetriever()
    
    print("📄 Processando documentos...")
    processor.process_all_documents()
    
    print("✂️ Dividindo textos em chunks...")
    chunks = splitter.process_markdown_files(Config.PROCESSED_DATA_DIR)
    print(f"   Total de chunks criados: {len(chunks)}")
    
    print("🧠 Gerando embeddings e construindo índice...")
    retriever.build_faiss_index(chunks)
    
    print("💾 Salvando índice FAISS...")
    retriever.save_index()
    
    print("✅ Pipeline concluído com sucesso!")
    print(f"   📊 Estatísticas:")
    print(f"   - Documentos processados: {len(list(Config.PROCESSED_DATA_DIR.glob('*.md')))}")
    print(f"   - Chunks criados: {len(chunks)}")
    print(f"   - Unidades identificadas: {len(set(chunk.metadata['unidade'] for chunk in chunks))}")

if __name__ == "__main__":
    main()
