from typing import Dict, Any, List, Annotated
import re
from ..core.retriever import ELPRetriever
from ..config import Config

class SpecializedELPTools:
    def __init__(self):
        self.retriever = ELPRetriever()
        self.retriever.load_index()
    
    def buscar_indicadores_por_unidade(
        self, 
        unidade: Annotated[str, "Nome da unidade (ex: ASSCOM, DTIC, GADP)"],
        ano: Annotated[str, "Ano dos indicadores (ex: 2024, 2025)"] = None
    ) -> str:
        """
        Busca indicadores estratégicos específicos de uma unidade.
        """
        try:
            query = f"indicadores estratégicos {unidade}"
            if ano:
                query += f" {ano}"
            
            results = self.retriever.search_by_unidade(query, unidade, k=10)
            
            if not results:
                return f"Nenhum indicador estratégico encontrado para a unidade '{unidade}'."
            
            response = f"**INDICADORES ESTRATÉGICOS - UNIDADE: {unidade.upper()}**\n\n"
            
            for result in results:
                response += f"**Fonte:** {result['metadata']['source']}\n"
                response += f"**Score:** {result['score']:.3f}\n"
                response += f"**Conteúdo:**\n{result['content'][:500]}...\n\n"
                response += "---\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar indicadores: {str(e)}"
    
    def buscar_planos_aquisicao_por_unidade(
        self, 
        unidade: Annotated[str, "Nome da unidade"],
        ano: Annotated[str, "Ano do plano (ex: 2024, 2025, 2026)"] = None
    ) -> str:
        """
        Busca planos de aquisição específicos de uma unidade.
        """
        try:
            query = f"plano aquisição {unidade}"
            if ano:
                query += f" {ano}"
            
            results = self.retriever.search_by_unidade(query, unidade, k=10)
            
            if not results:
                return f"Nenhum plano de aquisição encontrado para a unidade '{unidade}'."
            
            response = f"**PLANOS DE AQUISIÇÃO - UNIDADE: {unidade.upper()}**\n\n"
            
            for result in results:
                response += f"**Fonte:** {result['metadata']['source']}\n"
                response += f"**Score:** {result['score']:.3f}\n"
                response += f"**Conteúdo:**\n{result['content'][:600]}...\n\n"
                response += "---\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar planos de aquisição: {str(e)}"
    
    def buscar_riscos_por_unidade(
        self, 
        unidade: Annotated[str, "Nome da unidade"],
        ano: Annotated[str, "Ano dos riscos (ex: 2024, 2025)"] = None
    ) -> str:
        """
        Busca riscos operacionais específicos de uma unidade.
        """
        try:
            query = f"riscos operacionais {unidade}"
            if ano:
                query += f" {ano}"
            
            results = self.retriever.search_by_unidade(query, unidade, k=10)
            
            if not results:
                return f"Nenhum risco operacional encontrado para a unidade '{unidade}'."
            
            response = f"**RISCOS OPERACIONAIS - UNIDADE: {unidade.upper()}**\n\n"
            
            for result in results:
                response += f"**Fonte:** {result['metadata']['source']}\n"
                response += f"**Score:** {result['score']:.3f}\n"
                response += f"**Conteúdo:**\n{result['content'][:500]}...\n\n"
                response += "---\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar riscos: {str(e)}"
    
    def buscar_iniciativas_por_unidade(
        self, 
        unidade: Annotated[str, "Nome da unidade"],
        ano: Annotated[str, "Ano das iniciativas (ex: 2024, 2025)"] = None
    ) -> str:
        """
        Busca iniciativas estratégicas específicas de uma unidade.
        """
        try:
            query = f"iniciativas estratégicas {unidade}"
            if ano:
                query += f" {ano}"
            
            results = self.retriever.search_by_unidade(query, unidade, k=10)
            
            if not results:
                return f"Nenhuma iniciativa estratégica encontrada para a unidade '{unidade}'."
            
            response = f"**INICIATIVAS ESTRATÉGICAS - UNIDADE: {unidade.upper()}**\n\n"
            
            for result in results:
                response += f"**Fonte:** {result['metadata']['source']}\n"
                response += f"**Score:** {result['score']:.3f}\n"
                response += f"**Conteúdo:**\n{result['content'][:500]}...\n\n"
                response += "---\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar iniciativas: {str(e)}"
    
    def buscar_pta_por_unidade(
        self, 
        unidade: Annotated[str, "Nome da unidade"],
        ano: Annotated[str, "Ano do PTA (ex: 2024, 2025, 2026)"] = None
    ) -> str:
        """
        Busca PTA (Plano de Trabalho Anual) específico de uma unidade.
        """
        try:
            query = f"PTA plano trabalho anual {unidade}"
            if ano:
                query += f" {ano}"
            
            results = self.retriever.search_by_unidade(query, unidade, k=10)
            
            if not results:
                return f"Nenhum PTA encontrado para a unidade '{unidade}'."
            
            response = f"**PTA (PLANO DE TRABALHO ANUAL) - UNIDADE: {unidade.upper()}**\n\n"
            
            for result in results:
                response += f"**Fonte:** {result['metadata']['source']}\n"
                response += f"**Score:** {result['score']:.3f}\n"
                response += f"**Conteúdo:**\n{result['content'][:600]}...\n\n"
                response += "---\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao buscar PTA: {str(e)}"
    
    def analise_completa_unidade(
        self, 
        unidade: Annotated[str, "Nome da unidade para análise completa"]
    ) -> str:
        """
        Realiza análise completa de uma unidade, incluindo indicadores, riscos, iniciativas e planos.
        """
        try:
            response = f"**ANÁLISE COMPLETA DA UNIDADE: {unidade.upper()}**\n\n"
            
            # Busca indicadores estratégicos
            indicadores_query = f"indicadores estratégicos {unidade}"
            indicadores_results = self.retriever.search_by_unidade(indicadores_query, unidade, k=5)
            
            if indicadores_results:
                response += "## 📊 INDICADORES ESTRATÉGICOS\n\n"
                for result in indicadores_results:
                    response += f"**{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                    response += f"{result['content'][:300]}...\n\n"
            
            # Busca riscos operacionais
            riscos_query = f"riscos operacionais {unidade}"
            riscos_results = self.retriever.search_by_unidade(riscos_query, unidade, k=3)
            
            if riscos_results:
                response += "## ⚠️ RISCOS OPERACIONAIS\n\n"
                for result in riscos_results:
                    response += f"**{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                    response += f"{result['content'][:300]}...\n\n"
            
            # Busca iniciativas estratégicas
            iniciativas_query = f"iniciativas estratégicas {unidade}"
            iniciativas_results = self.retriever.search_by_unidade(iniciativas_query, unidade, k=3)
            
            if iniciativas_results:
                response += "## 🎯 INICIATIVAS ESTRATÉGICAS\n\n"
                for result in iniciativas_results:
                    response += f"**{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                    response += f"{result['content'][:300]}...\n\n"
            
            # Busca planos de aquisição
            aquisicoes_query = f"plano aquisição {unidade}"
            aquisicoes_results = self.retriever.search_by_unidade(aquisicoes_query, unidade, k=3)
            
            if aquisicoes_results:
                response += "## �� PLANOS DE AQUISIÇÃO\n\n"
                for result in aquisicoes_results:
                    response += f"**{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                    response += f"{result['content'][:300]}...\n\n"
            
            if not any([indicadores_results, riscos_results, iniciativas_results, aquisicoes_results]):
                return f"Nenhuma informação encontrada para a unidade '{unidade}'."
            
            return response
            
        except Exception as e:
            return f"Erro na análise completa: {str(e)}"
    
    def comparar_unidades(
        self, 
        unidade1: Annotated[str, "Primeira unidade para comparação"],
        unidade2: Annotated[str, "Segunda unidade para comparação"],
        tipo_documento: Annotated[str, "Tipo de documento (indicadores, riscos, iniciativas, aquisicoes)"] = "indicadores"
    ) -> str:
        """
        Compara duas unidades em um tipo específico de documento.
        """
        try:
            response = f"**COMPARAÇÃO: {unidade1.upper()} vs {unidade2.upper()}**\n"
            response += f"**Tipo:** {tipo_documento.upper()}\n\n"
            
            # Busca dados da primeira unidade
            query1 = f"{tipo_documento} {unidade1}"
            results1 = self.retriever.search_by_unidade(query1, unidade1, k=5)
            
            # Busca dados da segunda unidade
            query2 = f"{tipo_documento} {unidade2}"
            results2 = self.retriever.search_by_unidade(query2, unidade2, k=5)
            
            response += f"## {unidade1.upper()}\n"
            if results1:
                for result in results1:
                    response += f"**{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                    response += f"{result['content'][:200]}...\n\n"
            else:
                response += f"Nenhum {tipo_documento} encontrado.\n\n"
            
            response += f"## {unidade2.upper()}\n"
            if results2:
                for result in results2:
                    response += f"**{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                    response += f"{result['content'][:200]}...\n\n"
            else:
                response += f"Nenhum {tipo_documento} encontrado.\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro na comparação: {str(e)}"
    
    def listar_todas_unidades(self) -> str:
        """
        Lista todas as unidades disponíveis na base de conhecimento.
        """
        try:
            # Busca por termos gerais para obter todas as unidades
            query = "unidade"
            results = self.retriever.search(query, k=50)
            
            if not results:
                return "Nenhuma unidade encontrada na base de conhecimento."
            
            # Extrai unidades únicas
            unidades_unicas = set()
            for result in results:
                unidade = result['metadata']['unidade']
                if unidade and unidade != "Geral":
                    unidades_unicas.add(unidade)
            
            response = "**UNIDADES DISPONÍVEIS NA BASE DE CONHECIMENTO**\n\n"
            response += f"Total de unidades: {len(unidades_unicas)}\n\n"
            
            for i, unidade in enumerate(sorted(unidades_unicas), 1):
                response += f"{i}. **{unidade}**\n"
            
            return response
            
        except Exception as e:
            return f"Erro ao listar unidades: {str(e)}"
    
    def buscar_por_ano(
        self, 
        ano: Annotated[str, "Ano para busca (ex: 2024, 2025, 2026)"],
        tipo_documento: Annotated[str, "Tipo de documento (opcional)"] = None
    ) -> str:
        """
        Busca documentos por ano específico.
        """
        try:
            query = f"{ano}"
            if tipo_documento:
                query += f" {tipo_documento}"
            
            results = self.retriever.search(query, k=20)
            
            if not results:
                return f"Nenhum documento encontrado para o ano {ano}."
            
            response = f"**DOCUMENTOS DO ANO: {ano}**\n\n"
            
            # Organiza por tipo de documento
            documentos_por_tipo = {}
            for result in results:
                source = result['metadata']['source']
                if 'indicador' in source.lower():
                    documentos_por_tipo.setdefault('indicadores', []).append(result)
                elif 'risco' in source.lower():
                    documentos_por_tipo.setdefault('riscos', []).append(result)
                elif 'iniciativa' in source.lower():
                    documentos_por_tipo.setdefault('iniciativas', []).append(result)
                elif 'aquisição' in source.lower():
                    documentos_por_tipo.setdefault('aquisicoes', []).append(result)
                elif 'pta' in source.lower():
                    documentos_por_tipo.setdefault('pta', []).append(result)
                else:
                    documentos_por_tipo.setdefault('outros', []).append(result)
            
            for tipo, docs in documentos_por_tipo.items():
                if docs:
                    response += f"### {tipo.upper()} ({len(docs)} documentos)\n"
                    for doc in docs[:3]:  # Limita a 3 por tipo
                        response += f"- **{doc['metadata']['source']}** (Score: {doc['score']:.3f})\n"
                        response += f"  Unidade: {doc['metadata']['unidade']}\n"
                        response += f"  {doc['content'][:150]}...\n\n"
            
            return response
            
        except Exception as e:
            return f"Erro na busca por ano: {str(e)}"

def get_specialized_tools() -> Dict[str, Any]:
    """
    Retorna todas as ferramentas especializadas disponíveis.
    """
    tools_instance = SpecializedELPTools()
    
    return {
        "buscar_indicadores_por_unidade": tools_instance.buscar_indicadores_por_unidade,
        "buscar_planos_aquisicao_por_unidade": tools_instance.buscar_planos_aquisicao_por_unidade,
        "buscar_riscos_por_unidade": tools_instance.buscar_riscos_por_unidade,
        "buscar_iniciativas_por_unidade": tools_instance.buscar_iniciativas_por_unidade,
        "buscar_pta_por_unidade": tools_instance.buscar_pta_por_unidade,
        "analise_completa_unidade": tools_instance.analise_completa_unidade,
        "comparar_unidades": tools_instance.comparar_unidades,
        "listar_todas_unidades": tools_instance.listar_todas_unidades,
        "buscar_por_ano": tools_instance.buscar_por_ano
    }
