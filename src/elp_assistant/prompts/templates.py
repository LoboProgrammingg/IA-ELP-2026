from typing import Dict, Any

class ELPPromptTemplates:
    """Templates de prompt avançados para o agente ELP."""
    
    @staticmethod
    def get_system_prompt() -> str:
        """Retorna o prompt de sistema principal do agente."""
        return """Você é um Analista Estratégico Sênior especialista na Estratégia de Longo Prazo (ELP) da MTI.

## SUA IDENTIDADE E EXPERTISE
Você possui mais de 10 anos de experiência em análise estratégica governamental e é especialista em:
- Análise de indicadores estratégicos e operacionais
- Interpretação de dados de KPIs e métricas de performance
- Elaboração e revisão de estratégias de longo prazo
- Análise de riscos operacionais e iniciativas estratégicas
- Planejamento de aquisições e gestão de recursos públicos

## CONTEXTO DA MTI
A MTI (Ministério de Tecnologia e Inovação) está atualizando sua Estratégia de Longo Prazo para o período 2026-2030. Você tem acesso a uma base de conhecimento completa com:
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

### 2. USO DE FERRAMENTAS
- Use `buscar_contexto_elp` para consultas gerais sobre a ELP
- Use `buscar_kpis_da_unidade` para análises específicas por unidade
- Use `buscar_indicadores_estrategicos` para visão geral dos indicadores
- Use `analisar_documento` para análise detalhada de documentos específicos
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

## EXEMPLOS DE CONSULTAS ESPECIALIZADAS

### Análise de Indicadores:
"Analise os indicadores estratégicos da unidade X e identifique tendências"

### Análise de Riscos:
"Quais são os principais riscos operacionais identificados para 2025?"

### Planejamento Estratégico:
"Como os planos de aquisição se alinham com as iniciativas estratégicas?"

### Análise Comparativa:
"Compare os indicadores de 2024 com as metas para 2025"

## IMPORTANTE
- Responda sempre em português brasileiro
- Seja preciso e baseado em evidências
- Indique quando precisar de mais informações
- Mantenha foco na estratégia de longo prazo da MTI"""

    @staticmethod
    def get_analysis_prompt(context: str, question: str) -> str:
        """Template para análise específica com contexto."""
        return f"""Com base no contexto fornecido abaixo, analise a seguinte questão:

CONTEXTO:
{context}

PERGUNTA:
{question}

INSTRUÇÕES:
1. Analise o contexto fornecido
2. Identifique informações relevantes para a pergunta
3. Forneça uma análise estruturada e baseada em dados
4. Cite fontes específicas quando possível
5. Inclua insights estratégicos relevantes"""

    @staticmethod
    def get_kpi_analysis_prompt(unidade: str, kpis_data: str) -> str:
        """Template para análise de KPIs por unidade."""
        return f"""Analise os seguintes KPIs da unidade {unidade}:

DADOS DOS KPIs:
{kpis_data}

INSTRUÇÕES:
1. Identifique os principais indicadores da unidade
2. Analise tendências e padrões nos dados
3. Compare com metas estabelecidas (se disponível)
4. Identifique pontos de atenção ou oportunidades
5. Forneça recomendações estratégicas específicas"""

    @staticmethod
    def get_risk_analysis_prompt(risks_data: str) -> str:
        """Template para análise de riscos."""
        return f"""Analise os seguintes dados de riscos operacionais:

DADOS DE RISCOS:
{risks_data}

INSTRUÇÕES:
1. Categorize os riscos por tipo e severidade
2. Identifique riscos críticos que requerem atenção imediata
3. Analise tendências temporais dos riscos
4. Sugira estratégias de mitigação
5. Priorize ações baseadas no impacto e probabilidade"""

    @staticmethod
    def get_strategic_planning_prompt(initiatives_data: str, acquisition_data: str) -> str:
        """Template para análise de planejamento estratégico."""
        return f"""Analise o alinhamento entre iniciativas estratégicas e planos de aquisição:

INICIATIVAS ESTRATÉGICAS:
{initiatives_data}

PLANOS DE AQUISIÇÃO:
{acquisition_data}

INSTRUÇÕES:
1. Identifique sinergias entre iniciativas e aquisições
2. Analise gaps ou desalinhamentos
3. Sugira otimizações no planejamento
4. Identifique oportunidades de consolidação
5. Forneça recomendações para melhor alinhamento estratégico"""

def get_prompt_template(template_type: str, **kwargs) -> str:
    """Factory function para obter templates de prompt."""
    templates = ELPPromptTemplates()
    
    if template_type == "system":
        return templates.get_system_prompt()
    elif template_type == "analysis":
        return templates.get_analysis_prompt(kwargs.get("context", ""), kwargs.get("question", ""))
    elif template_type == "kpi_analysis":
        return templates.get_kpi_analysis_prompt(kwargs.get("unidade", ""), kwargs.get("kpis_data", ""))
    elif template_type == "risk_analysis":
        return templates.get_risk_analysis_prompt(kwargs.get("risks_data", ""))
    elif template_type == "strategic_planning":
        return templates.get_strategic_planning_prompt(
            kwargs.get("initiatives_data", ""), 
            kwargs.get("acquisition_data", "")
        )
    else:
        return templates.get_system_prompt()
