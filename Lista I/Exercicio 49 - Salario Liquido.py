salario_bruto = float(input("Digite o valor do salário: R$ "))
horas_trabalhada = int(input("Digite a quantidade de horas trabalhadas no mês: "))
hora_extra = int(input("Digite a quantidade de horas extras: "))

if salario_bruto <= 1100:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2204:
    inss = salario_bruto * 0.09
elif salario_bruto <= 3305:
    inss = salario_bruto * 0.12
elif salario_bruto <= 6433:
    inss = salario_bruto * 0.14
else:
    inss = 752

if salario_bruto <= 1904:
    irrf = 0
elif salario_bruto <= 2826:
    irrf = salario_bruto * 0.075
elif salario_bruto <= 3751:
    irrf = salario_bruto * 0.15
elif salario_bruto <= 4664:
    irrf = salario_bruto * 0.22
else:
    irrf = salario_bruto * 0.27

vt = salario_bruto * 0.06
valor_hora = salario_bruto / horas_trabalhada
acrescimo_he = hora_extra * (valor_hora * 1.5)
salario_liquido = salario_bruto - inss - irrf - vt + acrescimo_he

print(f"\nSalário Bruto: {salario_bruto} \nDesconto INSS: {inss:.2f} \nDesconto IRRF: {irrf:.2f} \nDesconto Vale Transporte: {vt:.2f}" 
f"\nValor de horas extras: {vt:.2f} \nSalário líquido (a receber): R$ {salario_liquido:.2f}")