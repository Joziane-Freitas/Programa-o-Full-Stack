def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def verificar_situacao(media):
    if media < 7:
        return 'Reprovado'
    elif media == 10:
        return 'Parabéns, sua média é 10'
    else:
        return 'Aprovado'

# Entrada de notas
notas = []
while True:
    nota = float(input('Digite a nota (ou digite -1 para sair): '))
    if nota == -1:
        break
    notas.append(nota)

# Calcular média
media = calcular_media(notas)

# Verificar situação
situacao = verificar_situacao(media)

print('Média:', media)
print('Situação:', situacao)
