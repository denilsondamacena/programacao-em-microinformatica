valor=float(input("Digite o valor da compra: R$ "))

if valor <= 100:
    desconto = 0.05
elif valor <= 500:
    desconto = 0.10
else:
    desconto = 0.15

valor_final= valor * (1 - desconto)
print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Valor a pagar: R$ {valor_final:.2f}")
