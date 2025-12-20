numero_str=(input("Digite um número: "))
base=int(input("Qual a base de origem 2, 8, 10 ou 16: "))
while True:
    try:
        if base == 2 or base == 8 or base == 10 or base == 16:
            if base == 2:
                numero_decimal = int(numero_str, 2)
                print(f"Binário: {bin(numero_decimal)[2:]}\n" f"Octal: {oct(numero_decimal)[2:]}\n"
                      f"Decimal: {numero_decimal}\n" f"Hexadecimal: {hex(numero_decimal)[2:]}")
                break
            elif base == 8:
                numero_decimal = int(numero_str, 8)
                print(f"Binário: {bin(numero_decimal)[2:]}\n" f"Octal: {oct(numero_decimal)[2:]}\n"
                      f"Decimal: {numero_decimal}\n" f"Hexadecimal: {hex(numero_decimal)[2:]}")
                break
            elif base == 16:
                numero_decimal = int(numero_str, 16)
                print(f"Binário: {bin(numero_decimal)[2:]}\n" f"Octal: {oct(numero_decimal)[2:]}\n"
                      f"Decimal: {numero_decimal}\n" f"Hexadecimal: {hex(numero_decimal)[2:]}")
                break
            else:
                numero_decimal = int(numero_str)
                print(f"Binário: {bin(numero_decimal)[2:]}\n" f"Octal: {oct(numero_decimal)[2:]}\n"
                      f"Decimal: {numero_decimal}\n" f"Hexadecimal: {hex(numero_decimal)[2:]}")
                break
        else:
            print("Base inválida! O valor da base deve ser: 2, 8, 10 ou 16.")
            break
    except ValueError:
        print("O número digitado não corresponde a uma das bases informadas.")
        break