from docling.document_converter import DocumentConverter

source = "data/raw/Estrutura dados IA - Indicadores_Disponibilidade_DTIC.csv"

converter = DocumentConverter()
result = converter.convert(source)

with open("Estrutura dados IA - Indicadores_Disponibilidade_DTIC.md", "w") as f:
    f.write(result.document.export_to_markdown())
    
