lado1=float(input("Digite o tamanho do primeiro lado: "))
lado2=float(input("Digite o tamanho do segundo lado: "))
lado3=float(input("Digite o tamanho do terceiro lado: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if (lado1 == lado2 == lado3):
         print("Triângulo equilátero (três lados iguais)")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
         print("Triângulo isósceles (dois lados iguais)")
    else:
        print("Triângulo escaleno (três lados diferentes)")
else:
    print("Os valores informados não formam um triângulo válido.")