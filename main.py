import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView


def main(page: ft.Page):

    page.window.width= 900
    page.window.height= 800
    page.title= "Cadastro de Usuário"

    tela_cadastro_usuario = CadastroUsuarioView (page)
    page.views.append(tela_cadastro_usuario)

ft.run(main)