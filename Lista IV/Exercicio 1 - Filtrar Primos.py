def listar_primos(entrada):
    primos = []
    for elemento in entrada:
        try:
            numero = int(elemento)
        except:
            continue
        if numero < 2:
            continue
        elif numero == 2:
            primos.append(numero)
            continue
        else:
            eh_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(numero)
    return primos

entrada = [2, 3, "4", 5, "abc", 7.0, 11, "13", 17]
print(listar_primos(entrada))