import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.voltar_login_view import Login
from src.view.principal_tela_view import PrincipalUsuarioView
from src.view.categoria_view import CategoriaView
from src.view.adicionar_despesas_view import AdicionarDespesasView
from src.view.todas_despesas_view import TodasDespesasView
from src.view.despesas_por_categoria_view import DespesaPorCategoriaView


def main(page: ft.Page):
    page.window.width= 900
    page.window.height= 800
    page.title= "Cadastro de Usuário"

    def navegacao(componente):
        item_clicado = componente.control.selected_index
        if item_clicado == 0:
            page.navigate("/categoria")
        elif item_clicado == 1:
            page.navigate("/adicionar_despesas")
        elif item_clicado == 2:
            page.navigate("/todas_despesas")
        elif item_clicado == 3:
            page.navigate("/despesas_categoria")
        elif item_clicado == 4:
            page.navigate("/login")


    barra_navegacao = ft.NavigationBar(destinations=[ft.NavigationBarDestination(icon=ft.Icons.CIRCLE, label="Categoria"),
    ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Adicionar Despesa"),
    ft.NavigationBarDestination(icon=ft.Icons.ADD_ALERT_ROUNDED, label="Todas Despesas"), 
    ft.NavigationBarDestination(icon=ft.Icons.SIGNAL_CELLULAR_ALT_SHARP, label="Despesas por Categoria"),
    ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, label="Sair")], on_change=navegacao)


    def roteamento(e=None):
        page.views.clear()

        if page.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView (page)
            tela_login =  Login(page)
            page.views.append(tela_cadastro_usuario)

        elif page.route == "/login":
            tela_principal = PrincipalUsuarioView(page)
            tela_principal.navigation_bar = barra_navegacao
            page.views.append(tela_login)

        elif page.route == "/principal":
            page.views.append(tela_principal)

        elif page.route == "/categoria":
            categoria = CategoriaView(page)
            categoria.navigation_bar = barra_navegacao
            page.views.append(categoria)

        elif page.route == "/adicionar_despesas":
            adicionar_despesas= AdicionarDespesasView(page)
            adicionar_despesas.navigation_bar = barra_navegacao
            page.views.append(adicionar_despesas)

        elif page.route == "/todas_despesas":
            todas_despesas = TodasDespesasView(page)
            todas_despesas.navigation_bar = barra_navegacao
            page.views.append(todas_despesas)

        elif page.route == "/despesas_categoria":
            despesas_categoria = DespesaPorCategoriaView(page)
            despesas_categoria.navigation_bar = barra_navegacao
            page.views.append(despesas_categoria)



        page.update()

    page.on_route_change = roteamento
    roteamento()

    page.views.append("/login")

ft.run(main)