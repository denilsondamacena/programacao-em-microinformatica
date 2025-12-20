def paginacao(lista_grande, tamanho_pagina):
    if tamanho_pagina <= 0:
        return ["Erro: O tamanho da página deve ser maior que zero."]

    tamanho_total = len(lista_grande)
    indices_de_inicio = range(0, tamanho_total, tamanho_pagina)
    paginas = [
        lista_grande[inicio : inicio + tamanho_pagina]
        for inicio in indices_de_inicio
    ]
    return paginas
lista_dados = list(range(22))
TAMANHO_PAGINA = 5
lista_de_paginas = paginacao(lista_dados, TAMANHO_PAGINA)
num_paginas_calculado = len(lista_de_paginas)

print(f"Lista original (tamanho {len(lista_dados)}): {lista_dados}")
print(f"Tamanho da Página: {TAMANHO_PAGINA}")
print("-" * 50)

for i, pagina in enumerate(lista_de_paginas):
    print(f"PÁGINA {i + 1} (Tamanho {len(pagina)}): {pagina}")

print("-" * 50)
print(f"Total de Páginas geradas: {num_paginas_calculado}")