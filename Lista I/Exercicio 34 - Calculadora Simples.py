num1=float(input("Digite o primeiro número: "))
operacao= input("Digite a operação (+, -, *, /): ")
num2=float(input("Digite o segundo número: "))
if operacao == "+":
    resultado= num1 + num2
    print(f"{num1}+{num2} = {resultado}")
elif operacao == "-":
    resultado= num1 - num2
    print(f"{num1}-{num2} = {resultado}")
elif operacao == "*":
    resultado= num1 * num2
    print(f"{num1}*{num2} = {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado= num1 / num2
        print(f"{num1}/{num2} = {resultado}")
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida!")


