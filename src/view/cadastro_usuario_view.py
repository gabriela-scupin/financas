import flet as ft

class CadastroUsuarioView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        titulo = ft.Text(value="Cadastro de Usuário")

        page.controls=[titulo]