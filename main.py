import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.voltar_login_view import Main

def main(page: ft.Page):

    page.window.width= 900
    page.window.height= 800
    page.title= "Cadastro de Usuário"

    tela_cadastro_usuario = CadastroUsuarioView (page)
    tela_voltar_login = Main (page)

    def roteamento(e=None):
        page.views.clear()

        if page.route == "/cadastrio":
            page.views.append(tela_cadastro_usuario)
        elif page.route == "/login":
            page.views.append(tela_voltar_login)

        page.update()

    page.on_route_cange = roteamento
    roteamento()

    page.views.append(tela_cadastro_usuario)

ft.run(main)