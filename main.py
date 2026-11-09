import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.voltar_login_view import Login

def main(page: ft.Page):

    page.window.width= 900
    page.window.height= 800
    page.title= "Cadastro de Usuário"

    tela_cadastro_usuario = CadastroUsuarioView (page)
    tela_login =  Login(page)

    def roteamento(e=None):
        page.views.clear()

        if page.route == "/cadastro":
            page.views.append(tela_cadastro_usuario)
        elif page.route == "/login":
            page.views.append(tela_login)

        page.update()

    page.on_route_change = roteamento
    roteamento()

    page.views.append(tela_cadastro_usuario)

ft.run(main)