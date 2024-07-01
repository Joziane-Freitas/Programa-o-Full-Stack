numeros = []

for i in range(10):
    numero = int(input('Digite um valor: '))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

soma_pares = sum(pares)
soma_impares = sum(impares)

quantidade_pares = len(pares)
quantidade_impares = len(impares)

print('Números pares:', pares)
print('Números ímpares:', tuple(impares))
print('Quantidade de números pares:', quantidade_pares)
print('Quantidade de números ímpares:', quantidade_impares)
print('Soma dos números pares:', soma_pares)
print('Soma dos números ímpares:', soma_impares)