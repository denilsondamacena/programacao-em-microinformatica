estoque = []
while True:
    print("Menu: \n1. Adicionar produto \n2. Listar produtos " \
          "\n3. Atualizar produto \n4. Apagar produto \n5. Sair")
    opcao = int(input("Digite o número da opção desejada: "))
    print("-" * 40)
    if opcao == 1:
        produto = input("Digite o produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        novo_id = len(estoque)
        novo_produto = (novo_id, produto, quantidade)
        estoque.append(novo_produto)
        print("-" * 40)
    elif opcao == 2:
        i = 0
        while i < len(estoque):
            produto = estoque[i]
            print(f"ID: {produto[0]}   Nome: {produto[1]}   Quantidade: {produto[2]}")
            print("-" * 40)
            i += 1
    elif opcao == 3:
        novo_codigo = int(input("Digite o número do ID do produto que deseja atualizar: "))
        atualizacao_produto = input("Digite o novo produto: ")
        nova_quantidade = int(input("Digite a nova quantidade do produto: "))
        i = 0
        while i < len(estoque):
            item = estoque[i]
            if novo_codigo == item[0]:
                novo_cadastro = (novo_codigo, atualizacao_produto, nova_quantidade)
                estoque[i] = novo_cadastro
                print("\nProduto atualizado com sucesso!")
                print("-" * 40)
                break
            i += 1
    elif opcao == 4:
        deletar = int(input("Digite o ID do produto que você deseja apagar: "))
        i = 0
        while i < len(estoque):
            item = estoque[i]
            if deletar == item[0]:
                estoque.pop(i)
                print("\nProduto removido com sucesso!")
                print("-" * 40)
                break
            i += 1
    elif opcao == 5:
        print("Operação finalizada!")
        break
    else:
        print("Esta opção é inválida!")
        print("-" * 40)