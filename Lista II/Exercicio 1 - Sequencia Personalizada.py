def sequencia(inicio, fim, passo):
    sequencia_lista = list(range(inicio, fim, passo))
    tamanho = len(sequencia_lista)
    soma = sum(sequencia_lista)
    media = soma / tamanho    

    print("--- Estatísticas da Sequência ---")
    print(f"Sequência gerada: {sequencia_lista}")
    print(f"Tamanho: {tamanho}")
    print(f"Soma Total: {soma}")
    print(f"Média Aritmética: {media:.2f}")
    print("Programa encerrado")
    print("-"*50)

sequencia(0,50,6)