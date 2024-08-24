import os

def listar_conteudo_diretorio():
    # Obter o diretório atual
    diretorio_atual = os.getcwd()  # Retorna o diretório de trabalho atual
    print(f"Listando arquivos e diretórios em: {diretorio_atual}")
    
    # Listar arquivos e diretórios no diretório atual
    conteudo = os.listdir(diretorio_atual)  # Lista o conteúdo do diretório atual
    
    # Exibir o conteúdo da lista
    print("Conteúdo do diretório:")
    for item in conteudo:
        print(item)

# Chamar a função para listar o conteúdo do diretório
listar_conteudo_diretorio()
