def navegador(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
numeros = list(range(1, 21))
valor = int(input("Digite o número a buscar: "))
indice = navegador(numeros, valor)
if indice != -1:
    print(f"Número {valor} encontrado no índice {indice}.")
else:
    print(f"Número {valor} não encontrado na lista.")