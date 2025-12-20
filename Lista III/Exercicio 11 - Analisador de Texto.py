texto_input = input("Cole ou digite o texto para análise: \n")
total_caracteres = 0
total_palavras = 0
total_frases = 0
total_caracteres = len(texto_input)
tokens_palavras = texto_input.split(' ')
contador_tokens = 0
tamanho_tokens = len(tokens_palavras)

while contador_tokens < tamanho_tokens:
    token = tokens_palavras[contador_tokens]    
    if token:
        total_palavras = total_palavras + 1
    contador_tokens = contador_tokens + 1

delimitadores = ['.', '!', '?']
contador_char = 0
tamanho_texto = len(texto_input)

while contador_char < tamanho_texto:
    caractere = texto_input[contador_char]    
    if caractere == '.' or caractere == '!' or caractere == '?':
        total_frases = total_frases + 1
    contador_char = contador_char + 1
if total_frases == 0 and total_caracteres > 0:
    total_frases = 1
print("\n--- Estatísticas ---")
print(f"Total de Caracteres: {total_caracteres}")
print(f"Total de Palavras: {total_palavras}")
print(f"Total de Frases: {total_frases}")
print("\n--- Busca Avançada (Simulação) ---")
termo_busca = input("Digite o termo a buscar: ")

if not termo_busca:
    print("Busca ignorada (termo vazio).")
else:
    try:
        indice_simples = texto_input.index(termo_busca)
        print(f"  Ocorrência Exata ('{termo_busca}'): Encontrada na posição {indice_simples}.")
    except ValueError:
        print(f"  Ocorrência Exata ('{termo_busca}'): Não encontrada.")
    texto_minusculo = texto_input.lower()
    termo_minusculo = termo_busca.lower()   
    contador_ocorrencias = 0   
    inicio_busca = 0    
    while True:
        try:
            indice = texto_minusculo.index(termo_minusculo, inicio_busca)           
            contador_ocorrencias = contador_ocorrencias + 1           
            inicio_busca = indice + 1          
        except ValueError:
            break
    print(f"  Total de Ocorrências (Case-Insensitive): {contador_ocorrencias}.")
print("---------------------------------------")