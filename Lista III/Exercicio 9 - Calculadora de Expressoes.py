expressao_str = input("Digite a expressão: ")
tokens = expressao_str.split(' ')
numeros = []
operadores = []
contador_tokens = 0
tamanho_tokens = 0
try:
    tamanho_tokens = len(tokens)
except:
    pass
while contador_tokens < tamanho_tokens:
    token = tokens[contador_tokens]
    try:
        numero = float(token)
        numeros.append(numero)
    except ValueError:
        if token == '+' or token == '-' or token == '*' or token == '/':
            operadores.append(token)
        else:
            print("\nERRO: Expressão inválida. Use apenas números e os operadores +, -, *, /.")
            numeros = []
            operadores = []
            contador_tokens = tamanho_tokens
            break

    contador_tokens = contador_tokens + 1

if not numeros or len(numeros) != len(operadores) + 1:
    if numeros or operadores:
        print("\nERRO: Formato da expressão incorreto. Certifique-se de que a ordem é Número Operador Número...")
        numeros = []
        operadores = []

novos_numeros = []
novos_operadores = []

contador_prio = 0
tamanho_op = 0

if operadores:
    tamanho_op = len(operadores)
    if len(numeros) > 0:
        novos_numeros.append(numeros[0])
    while contador_prio < tamanho_op:
        op = operadores[contador_prio]
        num_b = numeros[contador_prio + 1]
        if op == '*' or op == '/':
            num_a = novos_numeros.pop()
            resultado_prio = 0
            if op == '*':
                resultado_prio = num_a * num_b
            elif op == '/':
                try:
                    resultado_prio = num_a / num_b
                except ZeroDivisionError:
                    print("\nERRO: Divisão por zero não é permitida.")
                    novos_numeros = []
                    novos_operadores = []
                    contador_prio = tamanho_op
                    break
            novos_numeros.append(resultado_prio)
        else:
            novos_operadores.append(op)
            novos_numeros.append(num_b)
        contador_prio = contador_prio + 1
    numeros = novos_numeros
    operadores = novos_operadores
resultado_final = None
if numeros:
    resultado_final = numeros[0]
    contador_soma = 0
    tamanho_op_final = len(operadores)
    while contador_soma < tamanho_op_final:
        op = operadores[contador_soma]
        num_b = numeros[contador_soma + 1]
        if op == '+':
            resultado_final = resultado_final + num_b
        elif op == '-':
            resultado_final = resultado_final - num_b
        contador_soma = contador_soma + 1
print("-------------------------------------------------------")
if resultado_final is not None and not (not numeros and operadores):
    print(f"Resultado de '{expressao_str}':")
    print(f"👉 {resultado_final}")
else:
    if numeros or operadores:
         print("Não foi possível calcular devido a um erro na estrutura da expressão.")
    else:
         print("Cálculo cancelado devido a uma entrada inválida.")
print("-------------------------------------------------------")