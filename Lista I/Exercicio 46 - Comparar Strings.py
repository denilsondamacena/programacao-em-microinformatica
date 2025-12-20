texto1=input("Digite a primeira palavra: ")
texto2=input("Digite a segunda palavra: ")

len1 = len(texto1)
len2 = len(texto2)

if len1 > len2:
    print(f"A primeira palavra é maior ({len1} caracteres) que a segunda ({len2} caracteres).")
elif len1 < len2:
    print(f"A segunda palavra é maior ({len2} caracteres) que a primeira ({len1} caracteres).")
else:
    print(f"As duas palavras têm o mesmo tamanho ({len1} caracteres).")
