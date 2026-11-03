import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView


def main(page: ft.Page):
    tela_cadastro_usuario = CadastroUsuarioView (page)
    page.add(tela_cadastro_usuario)

ft.run(main)