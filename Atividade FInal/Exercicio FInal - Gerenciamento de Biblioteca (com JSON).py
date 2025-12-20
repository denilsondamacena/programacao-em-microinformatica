import json
import os
from datetime import datetime, timedelta

CONFIG = (10, 1)
ARQUIVO_LIVROS = 'livros.json'
ARQUIVO_USUARIOS = 'usuarios.json'

def _carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def _salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

livros = _carregar_dados(ARQUIVO_LIVROS)
usuarios = _carregar_dados(ARQUIVO_USUARIOS)

def _gerar_novo_id(colecao):
    max_id = CONFIG[1] - 1 
    for chave in colecao:
        try:
            chave_int = int(chave) 
            if chave_int > max_id:
                max_id = chave_int
        except ValueError:
            pass
    return str(max_id + 1)

def cadastrar_livro():
    print("\n--- Cadastro de Novo Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN (International Standard Book Number): ")
    novo_id = _gerar_novo_id(livros)
    livros[novo_id] = {
    'id': int(novo_id),
    'titulo': titulo,
    'autor': autor,
    'isbn': isbn,
    'disponivel': True,
    'emprestimo': None
}
    _salvar_dados(livros, ARQUIVO_LIVROS)
    print(f"\n Livro '{titulo}' cadastrado com ID: {novo_id}")

def listar_livros(livros_a_listar):
    limite = CONFIG[0] 
    total_livros = len(livros_a_listar)
    total_paginas = (total_livros + limite - 1) // limite
    if total_livros == 0:
        print("\nNenhum livro encontrado.")
        return
    pagina_atual = 1
    while True: 
        print(f"\n--- Livros Cadastrados (Página {pagina_atual}/{total_paginas}) ---")
        inicio = (pagina_atual - 1) * limite
        fim = min(pagina_atual * limite, total_livros)
        chaves_ordenadas = sorted(livros_a_listar.keys(), key=lambda x: int(x))
        for i in range(inicio, fim):
            livro_id = chaves_ordenadas[i]
            livro = livros_a_listar[livro_id]
            disponibilidade = "Disponível" if livro['disponivel'] else "**EMPRESTADO**" 
            print(f"| ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | {disponibilidade}")
        if total_paginas == 1:
            break
        print("\nOpções de navegação:")
        if pagina_atual > 1:
            print("  <: Página Anterior")
        if pagina_atual < total_paginas:
            print("  >: Próxima Página")
        print("  S: Sair da listagem")
        opcao = input("Digite a opção: ").upper()
        if opcao == 'S':
            break 
        elif opcao == '>' and pagina_atual < total_paginas:
            pagina_atual += 1
        elif opcao == '<' and pagina_atual > 1:
            pagina_atual -= 1
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_usuario():
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Nome do Usuário: ")
    novo_id = _gerar_novo_id(usuarios)
    usuarios[novo_id] = {
        'id': int(novo_id),
        'nome': nome,
        'livros_emprestados': []
    }
    _salvar_dados(usuarios, ARQUIVO_USUARIOS)
    print(f"\n Usuário '{nome}' cadastrado com ID: {novo_id}")

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    print("\n--- Usuários Cadastrados ---")
    for user_id in sorted(usuarios.keys(), key=lambda x: int(x)):
        usuario = usuarios[user_id]
        qtd_emprestimos = len(usuario['livros_emprestados'])
        print(f"| ID: {usuario['id']} | Nome: {usuario['nome']} | Empréstimos: {qtd_emprestimos}")

def emprestar_livro():
    print("\n--- Empréstimo de Livro ---")
    livro_id = input("Digite o ID do Livro: ")
    user_id = input("Digite o ID do Usuário: ")
    livro = livros.get(livro_id)
    usuario = usuarios.get(user_id)
    if not livro:
        print("\n Livro não encontrado.")
        return
    if not usuario:
        print("\n Usuário não encontrado.")
        return
    if not livro['disponivel']:
        print("\n Livro indisponível para empréstimo.")
        return
    if usuario_tem_atrasos(usuario):
        print("\n Este usuário está com livros em atraso e não pode realizar novos empréstimos.")
        return
    hoje = datetime.now()
    data_limite = hoje + timedelta(days=7)
    livro['disponivel'] = False
    livro['emprestimo'] = {
        'user_id': user_id,
        'data_emprestimo': hoje.isoformat(),
        'data_limite': data_limite.isoformat()
    }
    usuario['livros_emprestados'].append(int(livro_id))
    _salvar_dados(livros, ARQUIVO_LIVROS)
    _salvar_dados(usuarios, ARQUIVO_USUARIOS)
    print(f"\n Livro '{livro['titulo']}' emprestado para '{usuario['nome']}'.")
    print(f"Data limite para devolução: {data_limite.strftime('%d/%m/%Y')}")

def usuario_tem_atrasos(usuario):
    for livro_id in usuario['livros_emprestados']:
        livro = livros.get(str(livro_id))
        if livro and livro['emprestimo'] is not None:
            data_limite = datetime.fromisoformat(livro['emprestimo']['data_limite'])
            if datetime.now() > data_limite:
                return True
    return False

def devolver_livro():
    print("\n--- Devolução de Livro ---")
    livro_id_str = input("Digite o ID do Livro a ser devolvido: ")
    try:
        livro_id = int(livro_id_str)
    except ValueError:
        print("\n ID do Livro deve ser um número inteiro.")
        return
    livro = livros.get(livro_id_str)
    if not livro:
        print("\n Livro não encontrado.")
        return
    if livro['disponivel']:
        print("\n Este livro já está disponível na biblioteca.")
        return
    encontrado = False
    for user_id, usuario in usuarios.items():
        if livro_id in usuario['livros_emprestados']:
            usuario['livros_emprestados'].remove(livro_id)
            if livro['emprestimo'] is not None:
                data_limite = datetime.fromisoformat(livro['emprestimo']['data_limite'])
                if datetime.now() > data_limite:
                    print("\n Devolução em atraso! Usuário ficará impedido de novos empréstimos até regularizar.")
                else:
                    print("\n Devolução dentro do prazo!")
            livro['disponivel'] = True
            livro['emprestimo'] = None
            encontrado = True
            _salvar_dados(livros, ARQUIVO_LIVROS)
            _salvar_dados(usuarios, ARQUIVO_USUARIOS)
            print(f" Livro '{livro['titulo']}' devolvido por '{usuario['nome']}'.")
            break
    if not encontrado:
        print("\n Erro: Livro não encontrado na lista de empréstimos de nenhum usuário.")

def buscar_livros():
    print("\n--- Busca Avançada ---")
    termo = input("Buscar por Título ou Autor: ").lower()
    resultados = {}
    for livro_id, livro in livros.items(): 
        string_busca = livro['titulo'].lower() + " " + livro['autor'].lower()
        if termo in string_busca:
            resultados[livro_id] = livro
    print(f"\nEncontrados {len(resultados)} resultado(s):")
    listar_livros(resultados)

def gerar_relatorio_estatisticas():
    print("\n--- Relatório de Estatísticas ---")
    total_livros = len(livros)
    total_usuarios = len(usuarios)
    livros_emprestados = 0
    for livro in livros.values():
        if not livro['disponivel']:
            livros_emprestados += 1        
    print(f"Total de Livros no Catálogo: {total_livros}")
    print(f"Total de Usuários Cadastrados: {total_usuarios}")
    print(f"Livros Emprestados: {livros_emprestados}")
    print(f"Livros Disponíveis: {total_livros - livros_emprestados}")
    if total_livros > 0:
        porcentagem = (livros_emprestados / total_livros) * 100
        print(f"Percentual de Livros Emprestados: {porcentagem:.2f}%")

def exibir_menu():
    print("\n" + "="*40)
    print("Sistema de Gerenciamento de Biblioteca")
    print("="*40)
    print("1. Cadastrar Livro")
    print("2. Listar Livros (Todos) - Paginado")
    print("3. Cadastrar Usuário")
    print("4. Listar Usuários")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Buscar Livros")
    print("8. Relatórios e Estatísticas")
    print("9. Sair")
    print("="*40)
    return input("Escolha uma opção: ") 

def main():
    while True: 
        opcao = exibir_menu()
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros(livros)
        elif opcao == '3':
            cadastrar_usuario()
        elif opcao == '4':
            listar_usuarios()
        elif opcao == '5':
            emprestar_livro()
        elif opcao == '6':
            devolver_livro()
        elif opcao == '7':
            buscar_livros()
        elif opcao == '8':
            gerar_relatorio_estatisticas()
        elif opcao == '9':
            print("\n Encerrando o sistema. Até mais!")
            break 
        else:
            print("\n Opção inválida. Digite um número de 1 a 9.")

if __name__ == "__main__":
    main()