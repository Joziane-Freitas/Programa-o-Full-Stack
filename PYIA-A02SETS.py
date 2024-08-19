# Solicitar informações do contato
nome = input("Digite o nome do contato: ")
telefone = input("Digite o número de telefone: ")
email = input("Digite o endereço de email: ")

# Armazenar as informações em um dicionário
contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}

# Exibir o conteúdo do dicionário
print("\nInformações do contato:")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")
