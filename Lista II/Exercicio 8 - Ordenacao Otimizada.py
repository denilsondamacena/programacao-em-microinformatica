def ordenar(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for indice_analisado in range(0, n - i - 1):
            if lista[indice_analisado] > lista[indice_analisado + 1]:
                lista[indice_analisado], lista[indice_analisado + 1] = lista[indice_analisado + 1], lista[indice_analisado]
                trocou = True
        if not trocou:
            break
    return lista
entrada = input("Digite os números separados por espaço: ")
numeros_ordenar = [int(x) for x in entrada.split()]
ordenada = ordenar(numeros_ordenar)
print("Lista ordenada:", ordenada)