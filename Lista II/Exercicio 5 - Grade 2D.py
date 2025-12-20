def coordenadas(linhas, colunas):
    grade = []
    for eixo_vertical in range(linhas):
        linha = []
        for eixo_horizontal in range(colunas):
            linha.append((eixo_vertical, eixo_horizontal))
        grade.append(linha)
    return grade
linhas = int(input("Digite o número de linhas da grade: "))
colunas = int(input("Digite o número de colunas da grade: "))
grade = coordenadas(linhas, colunas)
print("\nGrade 2D:")
for linha in grade:
    print(linha)