def indices_reversos(lista, passo=1):
    tamanho = len(lista)  
    return [
        (i, lista[i]) 
        for i in range(tamanho - 1, -1, -passo)
    ]
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

print(f"Lista Original: {lista}")

resultado_reverso = indices_reversos(lista)
print(f"Reversa (1 em 1): {resultado_reverso}")

resultado_reverso_intercalado = indices_reversos(lista, passo=2)
print(f"Reversa (2 em 2): {resultado_reverso_intercalado}")