# dicionário para armazenar os alunos e suas matrículas
alunos = {}

#  adicionar um aluno ao dicionário
def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite o número de matrícula do aluno: ')
    alunos[matricula] = nome

# remover um aluno do dicionário
def remover_aluno():
    matricula = input('Digite o número de matrícula do aluno que deseja remover: ')
    if matricula in alunos:
        del alunos[matricula]
        print('Aluno removido com sucesso!')
    else:
        print('Aluno não encontrado.')

# visualizar todos os alunos do dicionário
def visualizar_alunos():
    print('Lista de alunos:')
    for matricula, nome in alunos.items():
        print(f'Matrícula: {matricula} - Nome: {nome}')

# Loop contínuo para execução do programa
while True:
    print('\nEscolha uma opção:')
    print('1 - Adicionar aluno')
    print('2 - Remover aluno')
    print('3 - Visualizar alunos')
    print('4 - Sair')

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        remover_aluno()
    elif opcao == '3':
        visualizar_alunos()
    elif opcao == '4':
        break
    else:
        print('Opção inválida. Tente novamente.')