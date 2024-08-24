# Lista para armazenar as tarefas
tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status})")

def marcar_como_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print(f"Tarefa '{tarefas[indice]['nome']}' marcada como concluída.")
    else:
        print("Índice de tarefa inválido.")

def exibir_tarefas_por_prioridade(prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada.")
        return

    for tarefa in tarefas_filtradas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{tarefa['nome']} - {tarefa['descricao']} (Categoria: {tarefa['categoria']}, Status: {status})")

def exibir_tarefas_por_categoria(categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa na categoria '{categoria}' encontrada.")
        return

    for tarefa in tarefas_filtradas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Status: {status})")

def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas por Prioridade")
    print("5. Exibir Tarefas por Categoria")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa (baixa, média, alta): ")
            categoria = input("Categoria da tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            indice = int(input("Digite o índice da tarefa a ser marcada como concluída: ")) - 1
            marcar_como_concluida(indice)
        
        elif opcao == "4":
            prioridade = input("Digite a prioridade para filtrar as tarefas (baixa, média, alta): ")
            exibir_tarefas_por_prioridade(prioridade)
        
        elif opcao == "5":
            categoria = input("Digite a categoria para filtrar as tarefas: ")
            exibir_tarefas_por_categoria(categoria)
        
        elif opcao == "6":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()


