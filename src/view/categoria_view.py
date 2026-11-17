import flet as ft

class CategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()


        self.pagina= pagina
        self.route = "/categoria"
        self.vertical_alignment="CENTER"   
        titulo= ft.Text(value="PAGINA PRINCIPAL(VOU FORMATAR DEPOIS!!!)",weight="bold",font_family="arial")
        # Define a cor de fundo da página
        self.bgcolor = "#B2F7B2"
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        campo_nome_categoria = ft.TextField(label="Nome da Categoria")
        botao_cadastrar = ft.Button(content="Incluir", width=250)

        self.controls = [titulo, campo_nome_categoria, botao_cadastrar]