palavras = ["amor", "roma", "caro", "alma", "arco", "mala", "luar", "ramo", "raul", "apple", "papel", "abacaxi", "morango"]
anagramas = []
i = 0  
while i < len(palavras):
    palavra = palavras[i]
    palavra_base = "".join(sorted(palavra))
    encontrado = False
    j = 0 
    while j < len(anagramas):
        if "".join(sorted(anagramas[j][0])) == palavra_base:
            anagramas[j].append(palavra)
            encontrado = True
            break
        j += 1
    if not encontrado:
        anagramas.append([palavra])
    i += 1
k = 0
while k < len(anagramas):
    if len(anagramas[k]) > 1:
        print(anagramas[k])
    k += 1