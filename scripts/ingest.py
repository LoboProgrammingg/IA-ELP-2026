"""
Script de ingestão para processar documentos da ELP da MTI.
Converte documentos PDF e CSV para Markdown e os salva em data/processed.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

from elp_assistant.config import config
from elp_assistant.core.data_processor import DataProcessor
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """
    Executa o pipeline completo de ingestão de dados.
    """
    logger.info("Iniciando pipeline de ingestão de dados...")
    
    processor = DataProcessor()
    raw_dir = config.raw_data_dir
    processed_dir = config.processed_data_dir
    
    supported_extensions = {'.pdf', '.csv'}
    processed_count = 0
    failed_count = 0
    
    logger.info(f"Processando arquivos de: {raw_dir}")
    logger.info(f"Salvando resultados em: {processed_dir}")
    
    for file_path in raw_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            logger.info(f"Processando: {file_path.name}")
            
            output_path = processed_dir / f"{file_path.stem}.md"
            
            success = processor.process_document(file_path, output_path)
            
            if success:
                processed_count += 1
                logger.info(f"✓ Sucesso: {file_path.name} -> {output_path.name}")
            else:
                failed_count += 1
                logger.error(f"✗ Falha: {file_path.name}")
    
    logger.info(f"Pipeline concluído!")
    logger.info(f"Arquivos processados com sucesso: {processed_count}")
    logger.info(f"Arquivos com falha: {failed_count}")
    
    if failed_count > 0:
        logger.warning("Alguns arquivos falharam no processamento. Verifique os logs acima.")
    
    return processed_count, failed_count

if __name__ == "__main__":
    try:
        success_count, failure_count = main()
        sys.exit(0 if failure_count == 0 else 1)
    except Exception as e:
        logger.error(f"Erro fatal no pipeline: {str(e)}")
        sys.exit(1)
