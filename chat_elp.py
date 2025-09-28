#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "src"))

from elp_assistant.agent.chain import create_elp_agent

def main():
    print("🤖 IA Assistente ELP da MTI")
    print("=" * 50)
    print("Digite suas perguntas sobre a Estratégia de Longo Prazo da MTI")
    print("Digite 'sair' para encerrar")
    print("=" * 50)
    
    try:
        agent = create_elp_agent()
        print("✅ Agente carregado com sucesso!")
        print()
        
        while True:
            pergunta = input("❓ Sua pergunta: ").strip()
            
            if pergunta.lower() in ['sair', 'exit', 'quit', '']:
                print("👋 Até logo!")
                break
            
            print("\n🤔 Analisando...")
            try:
                resposta = agent.chat(pergunta)
                print(f"\n📝 Resposta:\n{resposta}")
                print("\n" + "="*50 + "\n")
                
            except Exception as e:
                print(f"❌ Erro: {e}")
                print("\n" + "="*50 + "\n")
                
    except Exception as e:
        print(f"❌ Erro ao carregar agente: {e}")
        print("Verifique se as variáveis de ambiente estão configuradas corretamente.")

if __name__ == "__main__":
    main()
