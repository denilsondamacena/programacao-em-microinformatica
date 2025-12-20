ADMIN_USER = "admin"
ADMIN_PASS = "1234"

USER_USER = "user"
USER_PASS = "abcd"

GUEST_USER = "guest"
GUEST_PASS = "0000"

def validar_credencial(usuario, senha):
    if usuario == ADMIN_USER and senha == ADMIN_PASS:
        return "administrador"
    elif usuario == USER_USER and senha == USER_PASS:
        return "usuário"
    elif usuario == GUEST_USER and senha == GUEST_PASS:
        return "convidado"
    else:
        return None

def autenticar():
    tentativas = 0
    max_tentativas = 3
    bloqueio = 5
    while True: 
        if tentativas >= max_tentativas:
            print("Você atingiu o limite de tentativas. Sistema bloqueado temporariamente.")
            for i in range(bloqueio, 0, -1):
                print(f"Aguarde {i} segundos...") 
            print("Você já pode tentar novamente!")
            tentativas = 0 
            continue
        try:
            usuario = input("Digite o Usuário: ")
            senha = input("Digite a Senha: ")
            nivel = validar_credencial(usuario, senha)
            if nivel:
                print(f"Login bem-sucedido! Nível de acesso: {nivel}")               
                if nivel == "administrador":
                    print("Você tem acesso total ao programa!")
                elif nivel == "usuário":
                    print("Você tem acesso limitado ao programa.")
                else:
                    print("Você está logado como convidado.")
                break              
            else:
                tentativas += 1
                tentativas_restantes = max_tentativas - tentativas
                print(f"Credenciais inválidas. Tentativas restantes: {tentativas_restantes}")
        except:
            print("Erro inesperado na leitura dos dados. Tente novamente.")
            continue 
autenticar()