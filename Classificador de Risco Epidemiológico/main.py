"""
Projeto: Classificador de Risco Epidemiológico (Com Gráficos)
Descrição: Sistema simples de triagem educacional para avaliar o risco 
           epidemiológico com base em dados fornecidos pelo usuário, 
           incluindo visualização gráfica dos resultados.
"""

import matplotlib.pyplot as plt

def obter_resposta_sim_nao(pergunta):
    """Garante que o usuário responda apenas 's' (sim) ou 'n' (não)."""
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

def obter_idade():
    """Obtém a idade do usuário de forma segura."""
    while True:
        try:
            idade = int(input("Qual é a sua idade? "))
            if idade < 0 or idade > 120:
                print("Por favor, insira uma idade válida.")
                continue
            return idade
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def calcular_risco(idade, tem_sintomas, tem_comorbidades, vacinado, contato_recente):
    """Calcula a pontuação de risco e retorna a classificação e a pontuação total."""
    pontuacao = 0

    if idade >= 60: pontuacao += 2
    if tem_sintomas: pontuacao += 3
    if tem_comorbidades: pontuacao += 2
    if contato_recente: pontuacao += 2
    if vacinado: pontuacao -= 2

    if pontuacao < 2:
        classificacao = "Baixo Risco"
    elif 2 <= pontuacao <= 4:
        classificacao = "Médio Risco"
    else:
        classificacao = "Alto Risco"
        
    return classificacao, pontuacao

def gerar_grafico(idade, tem_sintomas, tem_comorbidades, vacinado, contato_recente, pontuacao_total):
    """Gera um gráfico de barras mostrando o impacto de cada fator."""
    # Definindo os rótulos do eixo X
    fatores = ['Idade (>=60)', 'Sintomas', 'Comorbidades', 'Contato', 'Vacinação']
    
    # Calculando os pontos individuais para o gráfico
    pts_idade = 2 if idade >= 60 else 0
    pts_sintomas = 3 if tem_sintomas else 0
    pts_comorbidades = 2 if tem_comorbidades else 0
    pts_contato = 2 if contato_recente else 0
    pts_vacina = -2 if vacinado else 0

    pontos = [pts_idade, pts_sintomas, pts_comorbidades, pts_contato, pts_vacina]
    
    # Cores: Vermelho para risco (>0), Verde para proteção (<0), Cinza para neutro (0)
    cores = ['#ff4c4c' if p > 0 else '#4cff4c' if p < 0 else '#cccccc' for p in pontos]

    # Criando a figura do gráfico
    plt.figure(figsize=(9, 5))
    barras = plt.bar(fatores, pontos, color=cores, edgecolor='black')
    
    plt.axhline(0, color='black', linewidth=1.2) # Linha do zero
    plt.title(f'Impacto dos Fatores no Seu Risco (Pontuação Final: {pontuacao_total})', fontsize=14, pad=15)
    plt.ylabel('Pontos Atribuídos', fontsize=12)
    plt.xlabel('Fatores Avaliados', fontsize=12)
    
    # Adicionando os valores numéricos em cima (ou embaixo) de cada barra
    for barra in barras:
        yval = barra.get_height()
        offset = 0.15 if yval >= 0 else -0.35
        va = 'bottom' if yval >= 0 else 'top'
        plt.text(barra.get_x() + barra.get_width()/2, yval + offset, 
                 f"{int(yval)}", ha='center', va=va, fontweight='bold')

    plt.ylim(-3, 4) # Ajusta o limite do eixo Y para acomodar os números
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    print("\n[!] Gerando gráfico de análise... (Feche a janela do gráfico para encerrar o programa)")
    plt.show()

def exibir_orientacoes(classificacao):
    """Exibe o resultado e as mensagens educativas."""
    print("\n" + "="*40)
    print(f" RESULTADO DA ANÁLISE: {classificacao.upper()}")
    print("="*40)

    if classificacao == "Baixo Risco":
        print("\nOrientação: Seu risco atual é baixo.")
        print("- Continue mantendo bons hábitos de higiene.")
        print("- Mantenha sua carteira de vacinação atualizada.")
    elif classificacao == "Médio Risco":
        print("\nOrientação: Seu risco é moderado. Atenção!")
        print("- Fique atento ao surgimento ou agravamento de sintomas.")
        print("- Evite aglomerações e use máscara em locais fechados.")
    else:
        print("\nOrientação: SEU RISCO É ALTO. Aja com precaução.")
        print("- Isole-se preventivamente para proteger outras pessoas.")
        print("- Procure atendimento médico imediatamente.")

    print("\n*Aviso: Este sistema é educativo e não substitui um diagnóstico médico.*")

def main():
    print("="*50)
    print(" BEM-VINDO AO CLASSIFICADOR DE RISCO EPIDEMIOLÓGICO ")
    print("="*50)
    print("Responda às perguntas abaixo:\n")

    # Coleta de dados
    idade = obter_idade()
    tem_sintomas = obter_resposta_sim_nao("Você está apresentando sintomas (febre, tosse, etc)?")
    tem_comorbidades = obter_resposta_sim_nao("Você possui alguma doença pré-existente?")
    vacinado = obter_resposta_sim_nao("Seu esquema vacinal está em dia?")
    contato_recente = obter_resposta_sim_nao("Teve contato com pessoas doentes recentemente?")

    # Processamento
    classificacao, pontuacao = calcular_risco(idade, tem_sintomas, tem_comorbidades, vacinado, contato_recente)

    # Saída em Texto
    exibir_orientacoes(classificacao)
    
    # Saída Gráfica
    gerar_grafico(idade, tem_sintomas, tem_comorbidades, vacinado, contato_recente, pontuacao)

if __name__ == "__main__":
    main()