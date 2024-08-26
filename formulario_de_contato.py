import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.padding = 20
    page.spacing = 10

    # Campo de entrada para o nome
    input_nome = ft.TextField(
        label="Nome",
        hint_text="Digite seu nome",
        width=300
    )

    # Campo de entrada para o email
    input_email = ft.TextField(
        label="Email",
        hint_text="Digite seu email",
        width=300
    )

    # Campo de entrada para a mensagem
    input_mensagem = ft.TextField(
        label="Mensagem",
        hint_text="Digite sua mensagem",
        multiline=True,
        min_lines=4,
        max_lines=6,
        width=300
    )

    # Função para processar o envio do formulário
    def enviar_formulario(e):
        nome = input_nome.value.strip()
        email = input_email.value.strip()
        mensagem = input_mensagem.value.strip()

        if nome and email and mensagem:
            # Aqui, podemos adicionar lógica para processar os dados, como enviar um email ou salvar em um banco de dados
            # Por enquanto, apenas mostramos uma mensagem de confirmação
            resultado.value = f"Formulário enviado com sucesso!\nNome: {nome}\nEmail: {email}\nMensagem: {mensagem}"
            resultado.color = "green"
            input_nome.value = ""
            input_email.value = ""
            input_mensagem.value = ""
        else:
            resultado.value = "Por favor, preencha todos os campos."
            resultado.color = "red"

        page.update()

    # Botão de envio
    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        on_click=enviar_formulario
    )

    # Texto para mostrar resultado do envio
    resultado = ft.Text()

    # Adicionando os componentes à página
    page.add(
        input_nome,
        input_email,
        input_mensagem,
        botao_enviar,
        resultado
    )

# Iniciar o aplicativo Flet
if __name__ == "__main__":
    ft.app(target=main)
