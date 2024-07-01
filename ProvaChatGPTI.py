# Solicita ao usuário o número de alunos
num_alunos = int(input('Informe o número de alunos: '))

notas_gerais = []

# Informações sobre cada aluno
for i in range(num_alunos):
    nome_aluno = input(f'Informe o nome do aluno {i+1}: ')
    notas = []
    
    # Solicita as 3 notas do aluno
    for j in range(3):
        nota = float(input(f'Informe a nota {j+1} do aluno {nome_aluno}: '))
        notas.append(nota)
    
    # Calcula a média do aluno
    media = sum(notas) / len(notas)
    
    # Verifica se o aluno foi aprovado ou reprovado
    situacao = 'Aprovado' if media >= 7.0 else 'Reprovado'
    
    # Exibe as informações do aluno
    print(f'\nAluno: {nome_aluno}')
    print(f'Notas: {notas}')
    print(f'Média: {media}')
    print(f'Situação: {situacao}\n')
    
    # Adiciona a média do aluno à lista de notas gerais
    notas_gerais.append(media)

# Calcula a média geral da turma
media_geral = sum(notas_gerais) / len(notas_gerais)
print(f'Média geral da turma: {media_geral}')
