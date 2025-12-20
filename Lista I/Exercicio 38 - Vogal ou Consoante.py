letra=input("Digite uma letra: ").lower()

if letra in "a,e,i,o,u":
    print(f"A letra '{letra}' é uma vogal")
else:
    print(f" A letra '{letra}' é uma consoante")