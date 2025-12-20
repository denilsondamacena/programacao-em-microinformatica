dividendo=int(input("Digite o dividendo: "))
divisor=int(input("Digite o divisor: "))
if divisor != 0:
    resultado=dividendo % divisor
    print(f"O resto da divisão de {dividendo} por {divisor} é {resultado}")
else:
    print("Erro! Não é possível dividir por zero.")