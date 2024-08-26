import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.padding = 20
    page.spacing = 10

    
    tarefas = []

    
    input_tarefa = ft.TextField(
        hint_text="Digite o nome da tarefa",
        expand=True
    )

    
    def adicionar_tarefa(e):
        if input_tarefa.value.strip() != "":
            tarefa = input_tarefa.value.strip()
            tarefas.append(tarefa)
            input_tarefa.value = ""  # Limpa o campo de entrada após adicionar a tarefa
            atualizar_lista()

    
    def atualizar_lista():
        lista_view.controls.clear()
        for tarefa in tarefas:
            lista_view.controls.append(ft.Text(tarefa))
        page.update()

    
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar Tarefa",
        on_click=adicionar_tarefa
    )

    
    lista_view = ft.Column()

    
    page.add(
        ft.Row(
            controls=[input_tarefa, botao_adicionar],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        lista_view
    )


if __name__ == "__main__":
    ft.app(target=main)
