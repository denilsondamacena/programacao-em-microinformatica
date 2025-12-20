peso=float(input("Digite o peso: "))
altura=float(input("Digite a altura: "))
imc=(peso/(altura*altura))
if imc < 18.5:
    print(f"IMC: {imc:.2f}, abaixo do peso")
elif imc < 25:
    print(f"IMC: {imc:.2f}, normal")
elif imc < 30:
    print(f"IMC: {imc:.2f}, sobrepeso")
elif imc < 35:
    print(f"IMC: {imc:.2f}, obesidade grau I")
elif imc < 40:
    print(f"IMC: {imc:.2f}, obesidade grau II")
else:
    print(f"IMC: {imc:.2f}, obesidade grau III (severa")
