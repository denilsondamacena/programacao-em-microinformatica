capital=float(input("Digite o capital: R$ "))
taxa=float(input("Digite a taxa de juros (%): "))
tempo=float(input("Digite o tempo (anos): "))
taxa_decimal = taxa / 100
juros=capital*taxa_decimal*tempo

print(f"O valor dos juros simples é: R$ {juros:.2f}")
