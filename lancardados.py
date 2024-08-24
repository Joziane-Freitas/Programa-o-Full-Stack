import random

def lancar_dados():
    dado1 = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 para o primeiro dado
    dado2 = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 para o segundo dado
    total = dado1 + dado2         # Soma os resultados dos dois dados
    return total

# Exemplo de uso da função
resultado = lancar_dados()
print(f"O resultado do lançamento dos dados é: {resultado}")
