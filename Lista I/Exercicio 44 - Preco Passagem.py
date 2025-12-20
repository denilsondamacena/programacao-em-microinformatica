idade=int(input("Digite a idade do passageiro: "))
passagem=float(input("Digite o valor da passagem: "))

if idade <= 12:
    preco = passagem * 0.5
elif idade >= 60:
    preco = passagem * 0.7
else:
    preco = passagem
print(f"Preço da passagem: R$ {preco:.2f}")
