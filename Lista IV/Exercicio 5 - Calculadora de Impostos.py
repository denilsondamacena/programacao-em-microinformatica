def calcular_imposto(renda):
    imposto = 0.0
    faixas = [20000.0, 40000.0, 60000.0, 80000.0]
    aliquotas = [0.05, 0.10, 0.15, 0.20, 0.25] 
    renda_restante = renda
    limite_anterior = 0.0
    for i in range(len(faixas)):
        limite_atual = faixas[i]
        valor_faixa = limite_atual - limite_anterior 
        aliquota_atual = aliquotas[i] 
        if renda_restante > valor_faixa:
            imposto_na_faixa = valor_faixa * aliquota_atual
            imposto = imposto + imposto_na_faixa
            renda_restante = renda_restante - valor_faixa
        else:
            imposto_na_faixa = renda_restante * aliquota_atual
            imposto = imposto + imposto_na_faixa
            renda_restante = 0.0 
            break 
        limite_anterior = limite_atual
    if renda_restante > 0.0:
        imposto = imposto + (renda_restante * aliquotas[-1])
    return imposto

while True:
    print("\n=== CALCULADORA DE IMPOSTO PROGRESSIVO ===")
    print("1 - Calcular imposto de um ano")
    print("2 - Comparar dois anos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "3":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        renda = 0.0
        try:
            renda_str = input("Digite sua renda anual: R$ ")
            renda = float(renda_str)
            if renda < 0:
                print("A renda não pode ser negativa. Tente novamente.")
                continue
        except:
            print("Valor inválido! Digite um número válido para a renda.")
            continue
        imposto = calcular_imposto(renda)       
        print(f"Imposto devido: R$ {imposto:.2f}")
        print(f"Renda líquida: R$ {renda - imposto:.2f}")
    elif opcao == "2":
        renda_ano1 = 0.0
        renda_ano2 = 0.0      
        try:
            renda_ano1_str = input("Digite a renda do primeiro ano: R$ ")
            renda_ano2_str = input("Digite a renda do segundo ano: R$ ")
            renda_ano1 = float(renda_ano1_str)
            renda_ano2 = float(renda_ano2_str)           
            if renda_ano1 < 0 or renda_ano2 < 0:
                print("As rendas não podem ser negativas. Tente novamente.")
                continue           
        except:
            print("Valor inválido! Digite números válidos para as rendas.")
            continue
        imposto1 = calcular_imposto(renda_ano1)
        imposto2 = calcular_imposto(renda_ano2)
        print("\n--- Comparação Anual ---")
        print(f"Ano 1 → Imposto: R$ {imposto1:.2f} | Líquido: R$ {renda_ano1 - imposto1:.2f}")
        print(f"Ano 2 → Imposto: R$ {imposto2:.2f} | Líquido: R$ {renda_ano2 - imposto2:.2f}")
        if imposto2 > imposto1:
            print("O imposto aumentou no segundo ano.")
        elif imposto2 < imposto1:
            print("O imposto diminuiu no segundo ano.")
        else:
            print("O imposto permaneceu o mesmo.")
    else:
        print("Opção inválida! Tente novamente.")