print("A senha deve conter pelo menos 8 caracteres, com letras maiúscula, minúscula, números e um caractere especial (@#$%!&*?)")
senha=input("Digite a senha: ")

maiuscula = minuscula = numero = especial = False
i = 0

while i < len(senha):
    c = senha[i]
    if c.isupper():
        maiuscula = True
    elif c.islower():
        minuscula = True
    elif c.isdigit():
        numero = True
    elif c in "@#$%!&*?":
        especial = True
    i += 1

if len(senha) >= 8 and maiuscula and minuscula and numero and especial:
    print("Senha válida!")
else:
    print("Senha inválida.")