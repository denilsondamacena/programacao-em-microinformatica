notas = []
qtd_notas = 4  
i = 1         
while i <= qtd_notas:
    try:
        nota = float(input(f"Digite a {i}ª nota: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            i += 1 
        else:
            print("A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro! Digite apenas números.")
print("-" * 30)
media = sum(notas) / len(notas)
if media >= 6.0:
    print(f"Média {media:.2f}, aluno aprovado.")
elif media >= 3.0:
    print(f"Média {media:.2f}, aluno em recuperação.")
else:
    print(f"Média {media:.2f}, aluno reprovado.")