from typing import Dict, Any, List, Annotated
import google.generativeai as genai
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from ..config import Config
from ..core.retriever import ELPRetriever
from ..tools.custom_tools import get_custom_tools
from ..tools.specialized_tools import get_specialized_tools
from ..prompts.templates import get_prompt_template

class ELPAgent:
    def __init__(self):
        self.retriever = None
        self.tools = {}
        self.agent = None
        self._initialize_components()
    
    def _initialize_components(self):
        """Inicializa todos os componentes do agente."""
        self._setup_retriever()
        self._setup_tools()
        self._setup_agent()
    
    def _setup_retriever(self):
        """Configura o sistema de recuperação de documentos."""
        self.retriever = ELPRetriever()
        self.retriever.load_index()
    
    def _setup_tools(self):
        """Configura as ferramentas customizadas e especializadas."""
        # Ferramentas básicas
        custom_tools = get_custom_tools()
        
        # Ferramentas especializadas
        specialized_tools = get_specialized_tools()
        
        def buscar_kpis_da_unidade(
            unidade: Annotated[str, "Nome da unidade da MTI para buscar KPIs"]
        ) -> str:
            """Busca KPIs específicos de uma unidade da MTI."""
            return custom_tools["buscar_kpis_da_unidade"](unidade)
        
        def buscar_indicadores_estrategicos() -> str:
            """Busca todos os indicadores estratégicos da MTI."""
            return custom_tools["buscar_indicadores_estrategicos"]()
        
        def analisar_documento(
            nome_documento: Annotated[str, "Nome do documento para análise"]
        ) -> str:
            """Analisa um documento específico da base de conhecimento."""
            return custom_tools["analisar_documento"](nome_documento)
        
        def buscar_contexto_elp(
            query: Annotated[str, "Consulta para buscar contexto relevante na base de conhecimento"]
        ) -> str:
            """Busca contexto relevante na base de conhecimento da ELP."""
            results = self.retriever.search(query, k=5)
            
            if not results:
                return "Nenhum contexto relevante encontrado."
            
            response = f"**Contexto encontrado para: {query}**\n\n"
            for i, result in enumerate(results, 1):
                response += f"{i}. **Score: {result['score']:.3f}**\n"
                response += f"   Unidade: {result['metadata']['unidade']}\n"
                response += f"   Fonte: {result['metadata']['source']}\n"
                response += f"   Conteúdo: {result['content'][:400]}...\n\n"
            
            return response
        
        def listar_todos_documentos() -> str:
            """Lista todos os documentos disponíveis na base de conhecimento."""
            return custom_tools["listar_todos_documentos"]()
        
        def relatorio_completo_documentos() -> str:
            """Gera um relatório completo de todos os documentos da base de conhecimento."""
            return custom_tools["relatorio_completo_documentos"]()
        
        def analise_estrategica_completa(
            tema: Annotated[str, "Tema para análise estratégica completa"]
        ) -> str:
            """Realiza análise estratégica completa de um tema específico."""
            # Busca contexto geral
            context_results = self.retriever.search(tema, k=8)
            
            if not context_results:
                return f"Nenhum contexto encontrado para o tema: {tema}"
            
            # Organiza contexto por tipo de documento
            context_by_type = {}
            for result in context_results:
                source = result['metadata']['source']
                if 'indicador' in source.lower():
                    context_by_type.setdefault('indicadores', []).append(result)
                elif 'risco' in source.lower():
                    context_by_type.setdefault('riscos', []).append(result)
                elif 'iniciativa' in source.lower():
                    context_by_type.setdefault('iniciativas', []).append(result)
                elif 'aquisição' in source.lower():
                    context_by_type.setdefault('aquisicoes', []).append(result)
                else:
                    context_by_type.setdefault('geral', []).append(result)
            
            # Monta análise estruturada
            analysis = f"**ANÁLISE ESTRATÉGICA: {tema.upper()}**\n\n"
            
            for category, results in context_by_type.items():
                if results:
                    analysis += f"### {category.upper()}\n"
                    for result in results[:3]:  # Limita a 3 por categoria
                        analysis += f"- **{result['metadata']['source']}** (Score: {result['score']:.3f})\n"
                        analysis += f"  {result['content'][:200]}...\n\n"
            
            return analysis
        
        # Ferramentas especializadas
        def buscar_indicadores_por_unidade(
            unidade: Annotated[str, "Nome da unidade (ex: ASSCOM, DTIC, GADP)"],
            ano: Annotated[str, "Ano dos indicadores (ex: 2024, 2025)"] = None
        ) -> str:
            """Busca indicadores estratégicos específicos de uma unidade."""
            return specialized_tools["buscar_indicadores_por_unidade"](unidade, ano)
        
        def buscar_planos_aquisicao_por_unidade(
            unidade: Annotated[str, "Nome da unidade"],
            ano: Annotated[str, "Ano do plano (ex: 2024, 2025, 2026)"] = None
        ) -> str:
            """Busca planos de aquisição específicos de uma unidade."""
            return specialized_tools["buscar_planos_aquisicao_por_unidade"](unidade, ano)
        
        def buscar_riscos_por_unidade(
            unidade: Annotated[str, "Nome da unidade"],
            ano: Annotated[str, "Ano dos riscos (ex: 2024, 2025)"] = None
        ) -> str:
            """Busca riscos operacionais específicos de uma unidade."""
            return specialized_tools["buscar_riscos_por_unidade"](unidade, ano)
        
        def buscar_iniciativas_por_unidade(
            unidade: Annotated[str, "Nome da unidade"],
            ano: Annotated[str, "Ano das iniciativas (ex: 2024, 2025)"] = None
        ) -> str:
            """Busca iniciativas estratégicas específicas de uma unidade."""
            return specialized_tools["buscar_iniciativas_por_unidade"](unidade, ano)
        
        def buscar_pta_por_unidade(
            unidade: Annotated[str, "Nome da unidade"],
            ano: Annotated[str, "Ano do PTA (ex: 2024, 2025, 2026)"] = None
        ) -> str:
            """Busca PTA (Plano de Trabalho Anual) específico de uma unidade."""
            return specialized_tools["buscar_pta_por_unidade"](unidade, ano)
        
        def analise_completa_unidade(
            unidade: Annotated[str, "Nome da unidade para análise completa"]
        ) -> str:
            """Realiza análise completa de uma unidade, incluindo indicadores, riscos, iniciativas e planos."""
            return specialized_tools["analise_completa_unidade"](unidade)
        
        def comparar_unidades(
            unidade1: Annotated[str, "Primeira unidade para comparação"],
            unidade2: Annotated[str, "Segunda unidade para comparação"],
            tipo_documento: Annotated[str, "Tipo de documento (indicadores, riscos, iniciativas, aquisicoes)"] = "indicadores"
        ) -> str:
            """Compara duas unidades em um tipo específico de documento."""
            return specialized_tools["comparar_unidades"](unidade1, unidade2, tipo_documento)
        
        def listar_todas_unidades() -> str:
            """Lista todas as unidades disponíveis na base de conhecimento."""
            return specialized_tools["listar_todas_unidades"]()
        
        def buscar_por_ano(
            ano: Annotated[str, "Ano para busca (ex: 2024, 2025, 2026)"],
            tipo_documento: Annotated[str, "Tipo de documento (opcional)"] = None
        ) -> str:
            """Busca documentos por ano específico."""
            return specialized_tools["buscar_por_ano"](ano, tipo_documento)
        
        self.tools = [
            # Ferramentas básicas
            buscar_kpis_da_unidade,
            buscar_indicadores_estrategicos,
            analisar_documento,
            buscar_contexto_elp,
            listar_todos_documentos,
            relatorio_completo_documentos,
            analise_estrategica_completa,
            
            # Ferramentas especializadas
            buscar_indicadores_por_unidade,
            buscar_planos_aquisicao_por_unidade,
            buscar_riscos_por_unidade,
            buscar_iniciativas_por_unidade,
            buscar_pta_por_unidade,
            analise_completa_unidade,
            comparar_unidades,
            listar_todas_unidades,
            buscar_por_ano,
            
            # Ferramenta externa
            TavilyTools()
        ]
    
    def _setup_agent(self):
        """Monta o agente final com todos os componentes."""
        system_instructions = """Você é um Analista Estratégico Sênior especialista na Estratégia de Longo Prazo (ELP) da MTI.

## SUA IDENTIDADE E EXPERTISE
Você possui mais de 10 anos de experiência em análise estratégica governamental e é especialista em:
- Análise de indicadores estratégicos e operacionais
- Interpretação de dados de KPIs e métricas de performance
- Elaboração e revisão de estratégias de longo prazo
- Análise de riscos operacionais e iniciativas estratégicas
- Planejamento de aquisições e gestão de recursos públicos

## CONTEXTO DA MTI
A MTI (Ministério de Tecnologia e Inovação) está atualizando sua Estratégia de Longo Prazo para o período 2026-2030. Você tem acesso a uma base de conhecimento completa com 19 documentos que incluem:
- Indicadores estratégicos e operacionais
- Planos de aquisição (2024-2026)
- Iniciativas estratégicas
- Análise de riscos operacionais
- Dados de satisfação e disponibilidade

## INSTRUÇÕES DE COMPORTAMENTO

### 1. ANÁLISE BASEADA EM DADOS
- Sempre baseie suas análises em dados concretos da base de conhecimento
- Cite fontes específicas e scores de relevância quando disponíveis
- Diferencie entre dados quantitativos e qualitativos
- Indique limitações quando os dados forem insuficientes

### 2. USO DE FERRAMENTAS ESPECIALIZADAS
- Use `listar_todas_unidades` para ver todas as unidades disponíveis
- Use `analise_completa_unidade` para análise abrangente de uma unidade específica
- Use `buscar_indicadores_por_unidade` para indicadores específicos por unidade
- Use `buscar_planos_aquisicao_por_unidade` para planos de aquisição por unidade
- Use `buscar_riscos_por_unidade` para riscos operacionais por unidade
- Use `buscar_iniciativas_por_unidade` para iniciativas estratégicas por unidade
- Use `buscar_pta_por_unidade` para PTA por unidade
- Use `comparar_unidades` para comparar duas unidades
- Use `buscar_por_ano` para buscar documentos por ano específico
- Use `relatorio_completo_documentos` para obter visão geral de todos os documentos
- Use `listar_todos_documentos` para ver todos os documentos disponíveis
- Use `buscar_contexto_elp` para consultas gerais sobre a ELP
- Use `tavily_search` apenas para informações externas complementares

### 3. ESTRUTURA DE RESPOSTAS
- Comece com um resumo executivo da análise
- Forneça dados específicos com citações
- Inclua insights estratégicos relevantes
- Termine com recomendações práticas quando apropriado

### 4. TOM E ESTILO
- Mantenha tom profissional e técnico
- Use linguagem clara e precisa
- Evite jargões desnecessários
- Seja objetivo e direto

## IMPORTANTE
- Responda sempre em português brasileiro
- Seja preciso e baseado em evidências
- Indique quando precisar de mais informações
- Mantenha foco na estratégia de longo prazo da MTI
- SEMPRE use os 19 documentos da base de conhecimento como fonte principal
- PRIORIZE o uso das ferramentas especializadas por unidade para análises mais precisas"""

        self.agent = Agent(
            model=Gemini(id="gemini-2.5-flash"),
            name="elp_analyst",
            tools=self.tools,
            instructions=system_instructions
        )
    
    def chat(self, message: str) -> str:
        """Processa uma mensagem do usuário e retorna a resposta do agente."""
        try:
            response = self.agent.run(message)
            return response
            
        except Exception as e:
            return f"Erro ao processar mensagem: {str(e)}"
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Retorna o histórico da conversa."""
        return self.agent.get_history()
    
    def clear_memory(self):
        """Limpa a memória conversacional."""
        self.agent.clear_history()
    
    def analyze_with_template(self, template_type: str, **kwargs) -> str:
        """Executa análise usando template específico."""
        try:
            template = get_prompt_template(template_type, **kwargs)
            response = self.agent.run(template)
            return response
        except Exception as e:
            return f"Erro na análise com template: {str(e)}"

def create_elp_agent() -> ELPAgent:
    """Factory function para criar uma instância do agente ELP."""
    return ELPAgent()
