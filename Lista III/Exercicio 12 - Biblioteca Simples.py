catalogo = [
    [201, "Cem Anos de Solidão", "Gabriel García Márquez", True],
    [202, "O Nome da Rosa", "Umberto Eco", True],
    [203, "Crime e Castigo", "Fiódor Dostoiévski", False],
    [204, "Orgulho e Preconceito", "Jane Austen", True],
    [205, "Dom Casmurro", "Machado de Assis", True]
]
emprestimos = [
    (1, 203, 7)
]
proximo_id_emprestimo = 2
jogo_ativo = True
multa_por_dia = 0.50

while jogo_ativo:
    print("\n---------------------------------------")
    print("SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("---------------------------------------")
    print("1. Exibir Catálogo Completo")
    print("2. Busca de Livro por Título/Autor")
    print("3. Realizar Empréstimo")
    print("4. Devolver Livro / Calcular Multa")
    print("5. Sair")    
    try:
        escolha = input("Escolha uma opção (1-5): ")
        escolha_int = int(escolha)        
    except ValueError:
        print("Opção inválida. Digite um número de 1 a 5.")
        continue
    if escolha_int == 1:
        print("\n--- Catálogo de Livros ---")
        print("ID | TÍTULO | AUTOR | STATUS")
        print("---------------------------------------")        
        indice_livro = 0
        tamanho_catalogo = len(catalogo)        
        while indice_livro < tamanho_catalogo:
            livro = catalogo[indice_livro]            
            id_livro = livro[0]
            titulo = livro[1]
            autor = livro[2]
            disponivel = livro[3]            
            status_str = "Disponível"
            if not disponivel:
                status_str = "Emprestado"                
            print(f"{id_livro} | {titulo} | {autor} | {status_str}")            
            indice_livro = indice_livro + 1
    elif escolha_int == 2:
        termo_busca = input("Digite o Título ou Autor para buscar: ").lower()
        resultados_encontrados = False        
        indice_livro = 0
        tamanho_catalogo = len(catalogo)        
        print("\n--- Resultados da Busca ---")        
        while indice_livro < tamanho_catalogo:
            livro = catalogo[indice_livro]            
            titulo_low = livro[1].lower()
            autor_low = livro[2].lower()            
            if termo_busca in titulo_low or termo_busca in autor_low:
                resultados_encontrados = True                
                status_str = "Disponível"
                if not livro[3]:
                    status_str = "Emprestado"                    
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Status: {status_str}")            
            indice_livro = indice_livro + 1            
        if not resultados_encontrados:
            print("Nenhum livro encontrado com o termo informado.")
    elif escolha_int == 3:
        try:
            id_emprestar = int(input("Digite o ID do livro que deseja emprestar: "))            
            livro_encontrado = False
            indice_livro = 0
            tamanho_catalogo = len(catalogo)            
            while indice_livro < tamanho_catalogo:
                livro = catalogo[indice_livro]                
                if livro[0] == id_emprestar:
                    livro_encontrado = True                    
                    if livro[3] == True:
                        catalogo[indice_livro] = [livro[0], livro[1], livro[2], False]                         
                        novo_emprestimo = (proximo_id_emprestimo, id_emprestar, 0)                        
                        emprestimos.append(novo_emprestimo)                        
                        proximo_id_emprestimo = proximo_id_emprestimo + 1                        
                        print(f"\nLivro '{livro[1]}' emprestado com sucesso! (Empréstimo ID: {novo_emprestimo[0]})")
                    else:
                        print(f"\nLivro '{livro[1]}' não está disponível (já emprestado).")                    
                    break                    
                indice_livro = indice_livro + 1           
            if not livro_encontrado:
                print("\nID de livro não encontrado no catálogo.")                
        except ValueError:
            print("\nEntrada inválida. Digite o ID como um número.")
    elif escolha_int == 4:
        try:
            id_devolver = int(input("Digite o ID do livro que está sendo devolvido: "))            
            livro_encontrado_cat = False
            indice_livro_cat = 0
            tamanho_cat = len(catalogo)           
            while indice_livro_cat < tamanho_cat:
                livro_cat = catalogo[indice_livro_cat]               
                if livro_cat[0] == id_devolver:
                    livro_encontrado_cat = True                   
                    catalogo[indice_livro_cat] = [livro_cat[0], livro_cat[1], livro_cat[2], True]
                    print(f"Livro '{livro_cat[1]}' foi liberado no catálogo.")
                    break                   
                indice_livro_cat = indice_livro_cat + 1           
            emprestimo_encontrado = False
            indice_emprestimo = 0
            nova_lista_emprestimos = []            
            dias_atraso = 0           
            while indice_emprestimo < len(emprestimos):
                emprestimo = emprestimos[indice_emprestimo]               
                if emprestimo[1] == id_devolver:
                    emprestimo_encontrado = True
                    dias_atraso = emprestimo[2]
                else:
                    nova_lista_emprestimos.append(emprestimo)                   
                indice_emprestimo = indice_emprestimo + 1              
            emprestimos = nova_lista_emprestimos    
            if emprestimo_encontrado:
                if dias_atraso > 0:
                    valor_multa = dias_atraso * multa_por_dia
                    print(f"ATRASO DETECTADO: {dias_atraso} dias.")
                    print(f"MULTA A PAGAR: R$ {valor_multa:.2f}")
                else:
                    print("Devolução sem atraso. Nenhuma multa.")
            elif livro_encontrado_cat:
                print("Livro devolvido, mas não havia registro de empréstimo ativo.")
            else:
                print("\nID de livro não encontrado para devolução.")
        except ValueError:
            print("\nEntrada inválida. Digite o ID como um número.")
    elif escolha_int == 5:
        jogo_ativo = False
        print("\nObrigado por usar o Sistema da Biblioteca. Tchau!")
    else:
        print("Opção inválida. Digite um número de 1 a 5.")