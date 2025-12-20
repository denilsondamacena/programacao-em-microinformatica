n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
n4=float(input("Digite a quarta nota: "))
media=(n1+n2+n3+n4)/4
if media >= 6.0:
    print(f"Média {media}. Aluno aprovado!")
elif media >= 3.0:
    print(f"Média {media}. Aluno em recuperação!")
else:
    print(f"Média {media}. Aluno reprovado!")