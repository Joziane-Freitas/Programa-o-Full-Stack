from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
quadrados = list(map(lambda x: x**2, numeros))

# Função filter() para obter uma nova lista com números pares da lista numeros
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Função reduce() para obter a soma de todos os números da lista numeros
soma = reduce(lambda x, y: x + y, numeros)

print("Lista com o quadrado de cada número:", quadrados)
print("Lista com os números pares:", pares)
print("Soma de todos os números:", soma)
