import random

minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+-=[]}{"
caracteres = minusculas + maiusculas + numeros + simbolos
while True:
    try:
        tamanho_senha = int(input("Digite o tamanho que deseja a senha: "))
        if tamanho_senha >= 8:
            break
        else:
            print("A senha deve conter pelo menos 8 caracteres.")
    except ValueError:
        print("Erro. Digite um número!")
senha = ""
i = 0
while i < tamanho_senha:
    senha += random.choice(caracteres)
    i += 1
print("-" * 40)
print(f"Senha gerada: {senha}")