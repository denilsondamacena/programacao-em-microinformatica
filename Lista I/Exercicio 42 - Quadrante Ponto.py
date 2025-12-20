x=int(input("Digite o valor do eixo X: "))
y=int(input("Digite o valor do eixo Y: "))

if x == 0 and y == 0:
    print("Ponto de origem")
elif x == 0:
    print("Ponto sobre o eixo Y")
elif y == 0:
    print("Ponto sobre o eixo X")
elif x > 0 and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("Segundo quadrante")
elif x < 0 and y < 0:
    print("Terceiro quadrante")
else:
    print("Quarto quadrante")