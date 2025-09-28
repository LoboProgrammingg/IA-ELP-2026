# 🤖 IA Assistente ELP da MTI

Sistema de IA especialista na Estratégia de Longo Prazo (ELP) da MTI para o período 2026-2030.

## 🚀 Início Rápido

### 1. Instalar Dependências
```bash
./instalar_dependencias.sh
```

### 2. Configurar Variáveis de Ambiente
Edite o arquivo `.env` com suas chaves de API:
```bash
GEMINI_API_KEY=sua_chave_aqui
TAVILY_API_KEY=sua_chave_aqui
```

### 3. Processar Dados (Primeira vez)
```bash
./executar_ingestao.sh
```

### 4. Usar a IA
```bash
./iniciar_chat.sh
```

## 📋 Scripts Disponíveis

| Script | Descrição |
|--------|-----------|
| `instalar_dependencias.sh` | Instala todas as dependências usando Poetry |
| `executar_ingestao.sh` | Processa documentos e cria índice FAISS |
| `iniciar_chat.sh` | Inicia o chat interativo com a IA |

## 🐍 Comandos Poetry Diretos

Se preferir usar Poetry diretamente:

```bash
# Instalar dependências
poetry install

# Executar ingestão
poetry run python scripts/ingest.py

# Iniciar chat
poetry run python chat_elp.py

# Entrar no ambiente virtual
poetry shell
```

## 💬 Exemplos de Perguntas

- "Quais são os principais indicadores estratégicos da MTI?"
- "Analise os riscos operacionais para 2025"
- "Realize uma análise estratégica completa sobre tecnologia e inovação"
- "Busque KPIs da unidade ASSCOM"

## 📁 Estrutura do Projeto

```
AGNO-MTI/
├── src/elp_assistant/          # Código principal
├── data/                       # Dados processados
├── scripts/                    # Scripts de ingestão
├── chat_elp.py                # Chat interativo
├── pyproject.toml             # Configuração Poetry
└── *.sh                       # Scripts de execução
```

## 🔧 Tecnologias

- **Framework**: Agno
- **LLM**: Google Gemini 2.5-flash
- **Vector Store**: FAISS
- **Busca Externa**: Tavily Search API
- **Gerenciamento**: Poetry
