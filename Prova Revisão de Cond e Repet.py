# email e senha definidos
email_cadastrado = 'usuario@mail.com'
senha_cadastrada = '102030'

# Solicitando email e senha do usuário
email_digitado = input('Digite seu email: ')
senha_digitada = input('Digite sua senha: ')

# Verificando se o email e senha digitados são iguais aos cadastrados
while email_digitado != email_cadastrado or senha_digitada != senha_cadastrada:
    print('Email ou senha incorretos. Tente novamente.')
    email_digitado = input('Digite seu email: ')
    senha_digitada = input('Digite sua senha: ')

print('Login realizado com sucesso!')