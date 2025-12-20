pessoas = []
while True:
    print("Menu:\n1. Cadastrar nova pessoa \n2. Buscar pessoa por nome \n3. Sair")
    print("-" * 40)
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Por favor, digite novamente.")
        continue
    if opcao == 1:
        nome = input("Digite o nome: ")
        while True:
            try:
                idade = int(input("Digite a idade: "))
                break
            except ValueError:
                print("Você deve inserir apenas números para idade.")
        cidade = input("Digite a cidade: ")
        cadastro = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}
        pessoas.append(cadastro)
        print("Pessoa cadastrada com sucesso!")
    elif opcao == 2:
        busca = input("Digite o nome que deseja buscar no banco de dados: ")
        encontrado = False
        i = 0
        while i < len(pessoas):
            pessoa = pessoas[i]
            if busca.lower() == pessoa['Nome'].lower():
                print("Pessoa encontrada!")
                print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")
                encontrado = True
                break
            i += 1
        if not encontrado:
            print("Este nome não está no banco de dados.")
    elif opcao == 3:
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida! Digite novamente.")