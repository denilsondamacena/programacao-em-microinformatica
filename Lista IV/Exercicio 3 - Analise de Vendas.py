dados_vendas = [
    ["João", "Sul", 1200, 1500, 1800],
    ["Maria", "Norte", 800, 950, 1100],
    ["Pedro", "Leste", 500, "erro", 700],  # Dado inconsistente para teste
    ["Ana", "Oeste", 2000, 2500, 3000]
]

def calcular_estatisticas(vendas_validas):
    total = 0.0
    maior = float("-inf")
    menor = float("inf")
    
    for valor in vendas_validas:
        total += valor
        if valor > maior:
            maior = valor     
        if valor < menor:
            menor = valor         
    if len(vendas_validas) > 0:
        media = total / len(vendas_validas)
    else:
        media = total = maior = menor = 0.0
    return total, media, maior, menor

def sistema_vendas():
    while True:
        print("\n=== MENU DE ANÁLISE DE VENDAS ===")
        print("1 - Analisar por Período")
        print("2 - Analisar por Vendedor (Desempenho)")
        print("3 - Analisar por Região (Total Simples)")
        print("4 - Sair do Sistema")
        opcao = input("Escolha uma opção (1-4): ")       
        if opcao == "1":
            print("\n--- Estatísticas por Período ---")
            for indice_periodo in range(3):
                vendas_periodo = []
                periodo_numero = indice_periodo + 1
                for vendedor in dados_vendas:
                    indice_venda = indice_periodo + 2
                    valor_venda = vendedor[indice_venda]
                    nome_vendedor = vendedor[0]
                    try:
                        venda_float = float(valor_venda)
                        vendas_periodo.append(venda_float)
                    except:
                        print(f"AVISO: Dado inválido (Não Numérico) ignorado para {nome_vendedor} no Período {periodo_numero}")
                total, media, maior, menor = calcular_estatisticas(vendas_periodo)
                print(f"Período {periodo_numero}: Total = {total:.2f} | Média = {media:.2f}")      
        elif opcao == "2":
            print("\n--- Estatísticas por Vendedor ---")
            for vendedor in dados_vendas:
                vendas_validas = []
                nome_vendedor = vendedor[0]
                regiao = vendedor[1]              
                for i in range(2, 5):
                    valor_venda = vendedor[i]                 
                    try:
                        vendas_validas.append(float(valor_venda))
                    except:
                        print(f"AVISO: Dado inválido (Não Numérico) ignorado para {nome_vendedor}")                       
                total, media, maior, menor = calcular_estatisticas(vendas_validas)              
                print(f"{nome_vendedor} ({regiao}) → Total de Vendas: {total:.2f}")                            
                if total >= 5000:
                    desempenho = "Excelente"
                elif total >= 3000:
                    desempenho = "Bom"
                else:
                    desempenho = "Regular"                
                print(f"Desempenho: {desempenho}")        
        elif opcao == "3":
            print("\n--- Estatísticas por Região (Total) ---")
            vendas_sul = []
            vendas_norte = []
            vendas_leste = []
            vendas_oeste = []
            for vendedor in dados_vendas:
                regiao = vendedor[1]               
                for i in range(2, 5):
                    valor_venda = vendedor[i]                   
                    try:
                        venda_float = float(valor_venda)                       
                        if regiao == "Sul":
                            vendas_sul.append(venda_float)
                        elif regiao == "Norte":
                            vendas_norte.append(venda_float)
                        elif regiao == "Leste":
                            vendas_leste.append(venda_float)
                        elif regiao == "Oeste":
                            vendas_oeste.append(venda_float)                           
                    except:
                        continue           
            total, _, _, _ = calcular_estatisticas(vendas_sul)
            print(f"Sul: Total de Vendas = {total:.2f}")           
            total, _, _, _ = calcular_estatisticas(vendas_norte)
            print(f"Norte: Total de Vendas = {total:.2f}")          
            total, _, _, _ = calcular_estatisticas(vendas_leste)
            print(f"Leste: Total de Vendas = {total:.2f}")          
            total, _, _, _ = calcular_estatisticas(vendas_oeste)
            print(f"Oeste: Total de Vendas = {total:.2f}")      
        elif opcao == "4":
            print("Saindo do Sistema de Análise. Até mais!")
            break          
        else:
            print("Opção inválida! Por favor, digite um número de 1 a 4.")
sistema_vendas()
