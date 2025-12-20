def cronometro_regressivo(segundos):
    print("Iniciando cronômetro regressivo...")
    for i in range(segundos, -1, -1):
        print(i)
    print("Tempo esgotado!")
tempo = int(input("Digite o tempo em segundos para o cronômetro: "))
cronometro_regressivo(tempo)