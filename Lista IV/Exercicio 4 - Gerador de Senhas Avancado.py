import random

LETRAS_MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
LETRAS_MAIUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMEROS = "0123456789"
SIMBOLOS = "!@#$%&*" 

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres_disponiveis = LETRAS_MINUSCULAS
    if usar_maiusculas == "s":
        caracteres_disponiveis = caracteres_disponiveis + LETRAS_MAIUSCULAS
    if usar_numeros == "s":
        caracteres_disponiveis = caracteres_disponiveis + NUMEROS
    if usar_simbolos == "s":
        caracteres_disponiveis = caracteres_disponiveis + SIMBOLOS
    senha = ""
    tamanho_pool = len(caracteres_disponiveis)   
    if tamanho_pool == 0:
        return "Nenhum caractere selecionado!"
    for i in range(tamanho):
        senha = senha + random.choice(caracteres_disponiveis)
    return senha

def validar_forca(senha):
    pontos = 0
    tem_minuscula = False
    tem_maiuscula = False
    tem_numero = False
    tem_simbolo = False
    for caractere in senha: 
        if caractere in LETRAS_MINUSCULAS:
            tem_minuscula = True      
        elif caractere in LETRAS_MAIUSCULAS:
            tem_maiuscula = True         
        elif caractere in NUMEROS:
            tem_numero = True           
        elif caractere in SIMBOLOS:
            tem_simbolo = True          
    if tem_minuscula: pontos = pontos + 1
    if tem_maiuscula: pontos = pontos + 1
    if tem_numero: pontos = pontos + 1
    if tem_simbolo: pontos = pontos + 1
    if pontos >= 4 and len(senha) >= 10:
        return "forte"
    elif pontos >= 2 and len(senha) >= 6:
        return "média"
    else:
        return "fraca"

def sistema_gerador():
    while True:
        print("\n=== GERADOR DE SENHAS ALEATÓRIO ===")
        print("1 - Gerar nova senha")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "2":
            print("Encerrando o programa...")
            break
        elif opcao == "1":
            tamanho = 0       
            try:
                tamanho_str = input("Digite o tamanho da senha (mínimo 6): ")
                tamanho = int(tamanho_str)
            except:
                print("Valor inválido! Digite um número inteiro.")
                continue
            if tamanho < 6:
                print("Tamanho muito pequeno. Usando o mínimo de 6.")
                tamanho = 6              
            usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower()
            usar_numeros = input("Incluir números? (s/n): ").lower()
            usar_simbolos = input("Incluir símbolos? (s/n): ").lower()         
            senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
            nivel = validar_forca(senha) 
            print(f"\nSenha gerada: {senha}")
            print(f"Força da senha: {nivel}")
            if nivel == "forte":
                print("Senha segura e aceita!")
            else:
                print("A senha é fraca/média. Tente uma nova senha com mais opções de caracteres e/ou um tamanho maior!")
        else:
            print("Opção inválida! Tente novamente.")
sistema_gerador()