# pip install flet

# Título do Chat
# Botão para iniciar Chat
#     Popup
#         Bem-vindo ao Chat
#         Escreva seu nome
#         Entrar no chat

# Chat
#     Pessoa entrou no Chat
#     Mensagens do usuário
# Campo para enviar mensagem
# Botão de enviar
import flet as ft

def main(pagina):
    titulo = ft.Text("chatName")

    nome_usuario = ft.TextField(label="Escreva seu nome")

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem-vindo ao chatName"),
        content=nome_usuario
        )

    def iniciar_chat(eventoClique):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main)

    