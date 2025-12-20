def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def calendario(mes, ano):
    dias_mes = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    if mes == 2 and bissexto(ano):
        dias_mes[2] = 29
    nomes_mes = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    if mes < 1 or mes > 12:
        print("Mês inválido! Digite um número entre 1 e 12.")
        return
    print(f"Calendário de {nomes_mes[mes]} de {ano}:")
    for dia in range(1, dias_mes[mes] + 1):
        print(f"{dia}/{mes}/{ano}")
numero_mes = int(input("Digite o número do mês (1 a 12): "))
ano = int(input("Digite o ano: "))
calendario(numero_mes, ano)