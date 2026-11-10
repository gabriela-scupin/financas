import flet as ft
class PrincipalUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()


        self.pagina= pagina
        self.route = "/principal"
        self.vertical_alignment="CENTER"   
        titulo= ft.Text(value="PAGINA PRINCIPAL(VOU FORMATAR DEPOIS!!!)",weight="bold",font_family="arial")
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER


        self.controls = [titulo]