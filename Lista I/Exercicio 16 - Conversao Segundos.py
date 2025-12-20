segundos=int(input("Digite os segundos: "))
minutos=(segundos%3600) // 60
horas=segundos // 3600
segundos_restantes=segundos % 60
print(f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
