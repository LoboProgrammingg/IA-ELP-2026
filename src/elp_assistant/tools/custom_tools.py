from typing import Dict, Any, List
import tavily
from ..config import Config
from ..core.retriever import ELPRetriever

class TavilySearchTool:
    def __init__(self):
        self.client = tavily.TavilyClient(api_key=Config.TAVILY_API_KEY)
    
    def search(self, query: str, max_results: int = 5) -> str:
        """
        Busca informações externas usando Tavily Search API.
        """
        try:
            response = self.client.search(
                query=query,
                search_depth="basic",
                max_results=max_results
            )
            
            results = []
            for result in response.get('results', []):
                results.append(f"**{result.get('title', 'Sem título')}**\n{result.get('content', 'Sem conteúdo')}\nURL: {result.get('url', 'N/A')}\n")
            
            return "\n".join(results) if results else "Nenhum resultado encontrado."
            
        except Exception as e:
            return f"Erro na busca externa: {str(e)}"

class KPISearchTool:
    def __init__(self):
        self.retriever = ELPRetriever()
        self.retriever.load_index()
    
    def buscar_kpis_da_unidade(self, unidade: str) -> str:
        """
        Busca KPIs específicos de uma unidade da MTI.
        """
        try:
            query = f"indicadores KPIs métricas {unidade}"
            results = self.retriever.search_by_unidade(query, unidade, k=5)
            
            if not results:
                return f"Nenhum KPI encontrado para a unidade '{unidade}'."
            
            response = f"**KPIs da Unidade: {unidade}**\n\n"
            for i, result in enumerate(results, 1):
                response += f"{i}. **Score: {result['score']:.3f}**\n"
                response += f"   Fonte: {result['metadata']['source']}\n"
                response += f"   Conteúdo: {result['content'][:300]}...\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar KPIs: {str(e)}"
    
    def buscar_indicadores_estrategicos(self) -> str:
        """
        Busca todos os indicadores estratégicos da MTI.
        """
        try:
            query = "indicadores estratégicos metas objetivos"
            results = self.retriever.search(query, k=10)
            
            if not results:
                return "Nenhum indicador estratégico encontrado."
            
            response = "**Indicadores Estratégicos da MTI**\n\n"
            unidades_encontradas = set()
            
            for result in results:
                unidade = result['metadata']['unidade']
                if unidade not in unidades_encontradas:
                    unidades_encontradas.add(unidade)
                    response += f"**Unidade: {unidade}**\n"
                    response += f"Score: {result['score']:.3f}\n"
                    response += f"Fonte: {result['metadata']['source']}\n"
                    response += f"Conteúdo: {result['content'][:200]}...\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar indicadores estratégicos: {str(e)}"

class DocumentAnalysisTool:
    def __init__(self):
        self.retriever = ELPRetriever()
        self.retriever.load_index()
    
    def analisar_documento(self, nome_documento: str) -> str:
        """
        Analisa um documento específico da base de conhecimento.
        """
        try:
            query = f"documento {nome_documento}"
            results = self.retriever.search(query, k=5)
            
            if not results:
                return f"Documento '{nome_documento}' não encontrado na base de conhecimento."
            
            response = f"**Análise do Documento: {nome_documento}**\n\n"
            
            for result in results:
                if nome_documento.lower() in result['metadata']['source'].lower():
                    response += f"**Unidade: {result['metadata']['unidade']}**\n"
                    response += f"Score: {result['score']:.3f}\n"
                    response += f"Conteúdo: {result['content'][:400]}...\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao analisar documento: {str(e)}"
    
    def listar_todos_documentos(self) -> str:
        """
        Lista todos os documentos disponíveis na base de conhecimento.
        """
        try:
            # Busca por termos gerais para obter todos os documentos
            query = "documentos base conhecimento MTI"
            results = self.retriever.search(query, k=50)  # Busca mais resultados
            
            if not results:
                return "Nenhum documento encontrado na base de conhecimento."
            
            # Organiza por fonte única
            documentos_unicos = {}
            for result in results:
                fonte = result['metadata']['source']
                if fonte not in documentos_unicos:
                    documentos_unicos[fonte] = {
                        'unidade': result['metadata']['unidade'],
                        'score': result['score'],
                        'preview': result['content'][:200]
                    }
            
            response = "**DOCUMENTOS DISPONÍVEIS NA BASE DE CONHECIMENTO**\n\n"
            response += f"Total de documentos únicos: {len(documentos_unicos)}\n\n"
            
            for i, (fonte, info) in enumerate(documentos_unicos.items(), 1):
                response += f"{i}. **{fonte}**\n"
                response += f"   Unidade: {info['unidade']}\n"
                response += f"   Score: {info['score']:.3f}\n"
                response += f"   Preview: {info['preview']}...\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao listar documentos: {str(e)}"
    
    def relatorio_completo_documentos(self) -> str:
        """
        Gera um relatório completo de todos os documentos da base de conhecimento.
        """
        try:
            # Busca por termos gerais para obter todos os documentos
            query = "documentos base conhecimento MTI estratégia"
            results = self.retriever.search(query, k=50)
            
            if not results:
                return "Nenhum documento encontrado na base de conhecimento."
            
            # Organiza por tipo de documento
            documentos_por_tipo = {
                'indicadores': [],
                'riscos': [],
                'iniciativas': [],
                'aquisicoes': [],
                'pta': [],
                'outros': []
            }
            
            for result in results:
                fonte = result['metadata']['source'].lower()
                if 'indicador' in fonte:
                    documentos_por_tipo['indicadores'].append(result)
                elif 'risco' in fonte:
                    documentos_por_tipo['riscos'].append(result)
                elif 'iniciativa' in fonte:
                    documentos_por_tipo['iniciativas'].append(result)
                elif 'aquisição' in fonte:
                    documentos_por_tipo['aquisicoes'].append(result)
                elif 'pta' in fonte:
                    documentos_por_tipo['pta'].append(result)
                else:
                    documentos_por_tipo['outros'].append(result)
            
            response = "**RELATÓRIO COMPLETO DA BASE DE CONHECIMENTO ELP MTI**\n\n"
            response += f"Total de documentos processados: {len(results)}\n\n"
            
            for tipo, docs in documentos_por_tipo.items():
                if docs:
                    response += f"## {tipo.upper()} ({len(docs)} documentos)\n\n"
                    
                    # Remove duplicatas por fonte
                    fontes_unicas = {}
                    for doc in docs:
                        fonte = doc['metadata']['source']
                        if fonte not in fontes_unicas:
                            fontes_unicas[fonte] = doc
                    
                    for fonte, doc in fontes_unicas.items():
                        response += f"### {fonte}\n"
                        response += f"**Unidade:** {doc['metadata']['unidade']}\n"
                        response += f"**Score:** {doc['score']:.3f}\n"
                        response += f"**Conteúdo:** {doc['content'][:300]}...\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao gerar relatório: {str(e)}"

def get_custom_tools() -> Dict[str, Any]:
    """
    Retorna todas as ferramentas customizadas disponíveis.
    """
    tavily_tool = TavilySearchTool()
    kpi_tool = KPISearchTool()
    analysis_tool = DocumentAnalysisTool()
    
    return {
        "tavily_search": tavily_tool.search,
        "buscar_kpis_da_unidade": kpi_tool.buscar_kpis_da_unidade,
        "buscar_indicadores_estrategicos": kpi_tool.buscar_indicadores_estrategicos,
        "analisar_documento": analysis_tool.analisar_documento,
        "listar_todos_documentos": analysis_tool.listar_todos_documentos,
        "relatorio_completo_documentos": analysis_tool.relatorio_completo_documentos
    }
