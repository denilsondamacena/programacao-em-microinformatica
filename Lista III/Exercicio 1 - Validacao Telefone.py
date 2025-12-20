while True:
    try:
        ddd=int(input("Digite o número do DDD (xx): "))
        if 10 <= ddd <= 99:
            break
        print("O DDD deve conter dois dígitos")
    except ValueError:
            print("Este não é um DDD válido")
while True: 
    try:
        numero=int(input("Digite o número do telefone: "))
        if 10000000 <= numero <= 999999999:
            break
        else:
            print("O número deve conter oito ou nove dígitos")
    except ValueError:
        print("Este não é um número válido!")
numero_str = str (numero)
print("-"*30)  
if len(numero_str) == 8:
    tipo = "Telefone Fixo"
    print(f"{tipo}: ({ddd}) {numero_str[:4]}-{numero_str[4:]}")
elif len(numero_str) == 9:
    tipo = "Celular"
    print(f"{tipo}: ({ddd}) {numero_str[:5]}-{numero_str[5:]}")
else:
    print("Este número não é válido no Brasil.")