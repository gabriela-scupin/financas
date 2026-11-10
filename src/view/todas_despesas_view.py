import flet as ft
class TodasDespesasView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()


        self.pagina= pagina
        self.route = "/todasdespesas"
        self.vertical_alignment="CENTER"   
        titulo= ft.Text(value="PAGINA PRINCIPAL(VOU FORMATAR DEPOIS!!!)",weight="bold",font_family="arial")
        # Define a cor de fundo da página
        self.bgcolor = "#f7f8aa"
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER


        self.controls = [titulo]