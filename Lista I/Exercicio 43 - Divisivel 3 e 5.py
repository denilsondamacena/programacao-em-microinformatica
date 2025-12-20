num=int(input("Digite um número: "))
if num % 3 == 0 and num % 5 == 0:
    print(f" O número {num} é divisível por 3 e 5.")
elif num % 3 == 0:
    print(f"O número {num} é divisível por 3 mas não por 5.")
elif num % 5 == 0:
    print(f"O número {num} não é divisível por 3 mas é por 5.")
else:
    print(f"O número {num} não é divisível por 3 e 5.")