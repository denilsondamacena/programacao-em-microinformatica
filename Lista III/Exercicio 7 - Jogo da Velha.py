tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
jogador_atual = "X"
jogo_ativo = True
vencedor = None
jogadas_realizadas = 0

while jogo_ativo:
    print("\n--- Jogo da Velha ---")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("----------------------\n")

    print(f"É a vez do jogador {jogador_atual}. Escolha uma posição (1-9):")

    jogada_valida = False
    posicao_escolhida = -1
    indice = -1

    while not jogada_valida:
        try:
            entrada = input()
            posicao_escolhida = int(entrada)
            indice = posicao_escolhida - 1
            if 1 <= posicao_escolhida <= 9:
                if tabuleiro[indice] != "X" and tabuleiro[indice] != "O":
                    jogada_valida = True
                else:
                    print("Essa célula já foi preenchida! Escolha outra.")
            else:
                print("Entrada inválida. Digite um número de 1 a 9.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
        except IndexError:
            print("Erro de índice. Tente novamente com um número de 1 a 9.")
    tabuleiro[indice] = jogador_atual
    jogadas_realizadas = jogadas_realizadas + 1
    if tabuleiro[0] == tabuleiro[1] and tabuleiro[1] == tabuleiro[2]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[3] == tabuleiro[4] and tabuleiro[4] == tabuleiro[5]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[6] == tabuleiro[7] and tabuleiro[7] == tabuleiro[8]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[0] == tabuleiro[3] and tabuleiro[3] == tabuleiro[6]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[1] == tabuleiro[4] and tabuleiro[4] == tabuleiro[7]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[2] == tabuleiro[5] and tabuleiro[5] == tabuleiro[8]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[0] == tabuleiro[4] and tabuleiro[4] == tabuleiro[8]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif tabuleiro[2] == tabuleiro[4] and tabuleiro[4] == tabuleiro[6]:
        vencedor = jogador_atual
        jogo_ativo = False
    elif jogadas_realizadas == 9:
        vencedor = None
        jogo_ativo = False
    if jogo_ativo:
        if jogador_atual == "X":
            jogador_atual = "O"
        elif jogador_atual == "O":
            jogador_atual = "X"

print("\n--- Jogo da Velha (Resultado Final) ---")
print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
print("---+---+---")
print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
print("---+---+---")
print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
print("--------------------------------------\n")

if vencedor is not None:
    print(f"PARABÉNS! O jogador {vencedor} VENCEU o jogo!")
else:
    print("O jogo terminou em EMPATE!")