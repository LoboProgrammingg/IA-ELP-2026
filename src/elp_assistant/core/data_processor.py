import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Optional
import docling
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self):
        self.converter = DocumentConverter()
    
    def convert_pdf_to_markdown(self, pdf_path: Path, output_path: Path) -> bool:
        """
        Converte um arquivo PDF para Markdown usando Docling.
        """
        try:
            logger.info(f"Convertendo PDF: {pdf_path.name}")
            
            result = self.converter.convert(str(pdf_path))
            markdown_content = result.document.export_to_markdown()
            
            # Limpeza e formatação do conteúdo
            cleaned_content = self._clean_markdown_content(markdown_content)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            logger.info(f"PDF convertido com sucesso: {output_path.name}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao converter PDF {pdf_path.name}: {str(e)}")
            return False
    
    def convert_csv_to_markdown(self, csv_path: Path, output_path: Path) -> bool:
        """
        Converte um arquivo CSV para Markdown usando Docling.
        Aplica formatação especial APENAS se tiver coluna 'Unidade'.
        """
        try:
            logger.info(f"Convertendo CSV: {csv_path.name}")
            
            # Usar Docling para converter CSV
            result = self.converter.convert(str(csv_path))
            markdown_content = result.document.export_to_markdown()
            
            # Verificar se tem coluna 'Unidade' para aplicar formatação especial
            if self._has_unidade_column(csv_path):
                logger.info(f"CSV com coluna 'Unidade' detectada - aplicando formatação especial")
                formatted_content = self._convert_table_to_unidade_format(markdown_content, csv_path)
            else:
                logger.info(f"CSV sem coluna 'Unidade' - aplicando formatação normal")
                formatted_content = self._convert_table_to_normal_format(markdown_content, csv_path)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            
            logger.info(f"CSV convertido com sucesso: {output_path.name}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao converter CSV {csv_path.name}: {str(e)}")
            return False
    
    def _has_unidade_column(self, csv_path: Path) -> bool:
        """Verifica se o CSV tem coluna 'Unidade'."""
        try:
            df = pd.read_csv(csv_path, encoding='utf-8', nrows=0)
            return 'Unidade' in df.columns
        except:
            try:
                df = pd.read_csv(csv_path, encoding='latin-1', nrows=0)
                return 'Unidade' in df.columns
            except:
                return False
    
    def _convert_table_to_unidade_format(self, markdown_content: str, csv_path: Path) -> str:
        """Converte tabela do Docling para formato especial com UNIDADE."""
        try:
            # Ler CSV para obter dados
            df = pd.read_csv(csv_path, encoding='utf-8')
            
            # Agrupar por Unidade
            grouped = df.groupby('Unidade')
            
            formatted_lines = []
            formatted_lines.append(f"# {csv_path.stem}")
            formatted_lines.append("")
            
            for unidade, group in grouped:
                if pd.isna(unidade) or unidade == '':
                    continue
                    
                formatted_lines.append(f"## UNIDADE: [{unidade}]")
                formatted_lines.append("")
                
                for _, row in group.iterrows():
                    formatted_lines.append("### Indicador")
                    formatted_lines.append("")
                    
                    for col in df.columns:
                        if col != 'Unidade' and pd.notna(row[col]) and str(row[col]).strip() != '':
                            clean_col = self._clean_column_name(col)
                            formatted_lines.append(f"**{clean_col}:** {row[col]}")
                    
                    formatted_lines.append("")
            
            return '\n'.join(formatted_lines)
            
        except Exception as e:
            logger.warning(f"Erro ao converter para formato UNIDADE: {e}")
            return markdown_content
    
    def _convert_table_to_normal_format(self, markdown_content: str, csv_path: Path) -> str:
        """Converte tabela do Docling para formato normal usando primeira coluna."""
        try:
            # Ler CSV para obter dados
            df = pd.read_csv(csv_path, encoding='utf-8')
            first_col = df.columns[0]
            
            formatted_lines = []
            formatted_lines.append(f"# {csv_path.stem}")
            formatted_lines.append("")
            
            for idx, row in df.iterrows():
                first_value = row[first_col]
                
                if pd.notna(first_value) and str(first_value).strip() != '':
                    clean_col = self._clean_column_name(first_col)
                    formatted_lines.append(f"## {clean_col}: {first_value}")
                    formatted_lines.append("")
                    
                    # Adicionar outras colunas como detalhes
                    for col in df.columns[1:]:  # Pular primeira coluna
                        if pd.notna(row[col]) and str(row[col]).strip() != '':
                            clean_col = self._clean_column_name(col)
                            formatted_lines.append(f"**{clean_col}:** {row[col]}")
                    
                    formatted_lines.append("")
            
            return '\n'.join(formatted_lines)
            
        except Exception as e:
            logger.warning(f"Erro ao converter para formato normal: {e}")
            return markdown_content
    
    def _clean_column_name(self, col_name: str) -> str:
        """Limpa e formata nomes de colunas."""
        # Remove caracteres especiais e normaliza
        clean_name = re.sub(r'[^\w\s]', '', str(col_name))
        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
        
        # Capitaliza primeira letra de cada palavra
        clean_name = ' '.join(word.capitalize() for word in clean_name.split())
        
        return clean_name
    
    def _clean_markdown_content(self, content: str) -> str:
        """Limpa e melhora o conteúdo Markdown."""
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove linhas muito curtas que podem ser ruído
            if len(line.strip()) < 3 and line.strip() != '':
                continue
            
            # Limpa espaços excessivos
            line = re.sub(r'\s+', ' ', line.strip())
            
            if line:
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def process_document(self, input_path: Path, output_path: Path) -> bool:
        """
        Processa um documento baseado em sua extensão usando Docling.
        """
        suffix = input_path.suffix.lower()
        
        if suffix == '.pdf':
            return self.convert_pdf_to_markdown(input_path, output_path)
        elif suffix == '.csv':
            return self.convert_csv_to_markdown(input_path, output_path)
        else:
            logger.warning(f"Formato não suportado: {suffix}")
            return False
