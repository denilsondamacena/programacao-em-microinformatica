cpf_original = None
cpf_valido = False
entrada_valida = False
while not entrada_valida:
    try:
        cpf_input = input("Digite o CPF (apenas números, 11 dígitos): ")        
        cpf_num = int(cpf_input)
        if len(cpf_input) != 11:
            print("ERRO: O CPF deve ter exatamente 11 dígitos.")
            continue        
        if cpf_input == "00000000000" or \
           cpf_input == "11111111111" or \
           cpf_input == "22222222222" or \
           cpf_input == "33333333333" or \
           cpf_input == "44444444444" or \
           cpf_input == "55555555555" or \
           cpf_input == "66666666666" or \
           cpf_input == "77777777777" or \
           cpf_input == "88888888888" or \
           cpf_input == "99999999999":
            print("ERRO: CPF inválido (dígitos repetidos).")
            continue
        cpf_original = cpf_input
        entrada_valida = True

    except ValueError:
        print("ERRO: O CPF deve conter apenas números.")
    except Exception as e:
        print(f"ERRO inesperado na entrada: {e}")

if cpf_original is not None:
    
    d1 = int(cpf_original[0])
    d2 = int(cpf_original[1])
    d3 = int(cpf_original[2])
    d4 = int(cpf_original[3])
    d5 = int(cpf_original[4])
    d6 = int(cpf_original[5])
    d7 = int(cpf_original[6])
    d8 = int(cpf_original[7])
    d9 = int(cpf_original[8])
    
    soma_dv1 = (d1 * 10) + (d2 * 9) + (d3 * 8) + (d4 * 7) + (d5 * 6) + \
               (d6 * 5) + (d7 * 4) + (d8 * 3) + (d9 * 2)
    
    resto_dv1 = soma_dv1 % 11
    
    dv1_esperado = 0
    if resto_dv1 < 2:
        dv1_esperado = 0
    else:
        dv1_esperado = 11 - resto_dv1

        dv1_real = int(cpf_original[9])

    soma_dv2 = (d1 * 11) + (d2 * 10) + (d3 * 9) + (d4 * 8) + (d5 * 7) + \
               (d6 * 6) + (d7 * 5) + (d8 * 4) + (d9 * 3) + (dv1_esperado * 2)          
    resto_dv2 = soma_dv2 % 11
    dv2_esperado = 0
    if resto_dv2 < 2:
        dv2_esperado = 0
    else:
        dv2_esperado = 11 - resto_dv2
    dv2_real = int(cpf_original[10])
    if dv1_real == dv1_esperado and dv2_real == dv2_esperado:
        cpf_valido = True
    else:
        cpf_valido = False
print("---------------------------------------")
if cpf_original is not None:
    if cpf_valido:
        print(f"✅ O CPF {cpf_original} é VÁLIDO.")
    else:
        print(f"❌ O CPF {cpf_original} é INVÁLIDO.")
        print(f"  DVs fornecidos: {dv1_real}{dv2_real}")
        print(f"  DVs esperados: {dv1_esperado}{dv2_esperado}")
else:
    print("Processamento encerrado devido a erros na entrada.")
print("---------------------------------------")