print("Jogo da Adivinhação")
print("Tente adivinhar o número entre 1 e 100!")

numero_secreto = 42
acertou = False

while not acertou:
    chute = int(input("Digite seu palpite: "))

    if chute == numero_secreto:
        print("Parabéns! Você acertou! 🎉")
        acertou = True
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")