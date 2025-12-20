dia=int(input("Digite o dia: "))
mes=int(input("Digite o mês: "))
ano=int(input("Digite o ano: "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    max_dia = 31
elif mes in [4, 6, 9, 11]:
    max_dia = 30
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        max_dia = 29
    else:
        max_dia = 28
else:
    max_dia = 0

if 1 <= dia <= max_dia and 1 <= mes <= 12:
    print(f"A data {dia}/{mes}/{ano} é válida.")
else:
    print(f"A data {dia}/{mes}/{ano} é inválida.")
