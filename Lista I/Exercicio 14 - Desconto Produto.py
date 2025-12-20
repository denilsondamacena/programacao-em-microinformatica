valor=float(input("Digite o valor do produto: "))
desconto=float(input("Digite o desconto: "))
valor_desconto=valor*(desconto/100)
novo_valor=valor-valor_desconto
print(f"O valor do desconto é R${valor_desconto} e novo preço do produto é R${novo_valor}")