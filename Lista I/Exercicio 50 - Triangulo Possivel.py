lado1=float(input("Digite o tamanho do primeiro lado: "))
lado2=float(input("Digite o tamanho do segundo lado: "))
lado3=float(input("Digite o tamanho do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É um triângulo do tipo: ")
    if (lado1 == lado2 == lado3):
         print("Equilátero (três lados iguais)")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
         print("Isósceles (dois lados iguais)")
    else:
        print("Escaleno (três lados diferentes)")
else:
     print("Não é possível formar um triângulo!")