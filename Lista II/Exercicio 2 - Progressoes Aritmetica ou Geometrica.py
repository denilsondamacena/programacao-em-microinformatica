def progressao_aritmetica(a1, r, n_termos):
    return [a1 + i * r for i in range(n_termos)]
print("----- Progressão Aritmética -----")
print()
print(f"Progressão Aritmética 1: {progressao_aritmetica(2, 3, 5)}")  
print(f"Progressão Aritmética 2: {progressao_aritmetica(10, -2, 6)}")    
print(f"Progressão Aritmética 3: {progressao_aritmetica(0.5, 1.5, 4)}")  
print("="*50)
def progressao_geometrica(a1, q, n_termos):
    return [a1 * (q ** i) for i in range(n_termos)]
print("----- Progressão Geométrica -----")
print()
print(f"Progressão Geométrica 1: {progressao_geometrica(1, 2, 6)}")   
print(f"Progressão Geométrica 2: {progressao_geometrica(100, 0.5, 5)}")  
print(f"Progressão Geométrica 3: {progressao_geometrica(3, 10, 3)}")     