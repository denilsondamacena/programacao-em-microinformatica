temperatura=float(input("Digite a temperatura do corpo: "))

if temperatura <= 35:
    print("Hipotermia")
elif temperatura <= 37.5:
    print("Normal")
elif temperatura <= 39.5:
    print("Febre")
elif temperatura <= 41:
    print("Febre alta")
else:
    print("Hipertermia")