import flet as ft
from src.model.categoria import Categoria
from src.model.usuario_model import Usuario

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

        self.campo_nome_categoria = ft.TextField(label="Nome da Categoria")
        botao_cadastrar = ft.Button(content="Incluir", width=250)


        self.controls = [titulo, self.campo_nome_categoria, botao_cadastrar]

    def cadastrar_categoria(self):
        nome_categoria = self.campo_nome_categoria.value

        resultado = Categoria().adicionar(nome_categoria, self.id_usuario)
        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efeituado com sucesso!"), bgcolor="#ceffcb"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#ffa0a6"))
            
        self.atualizar_lista_categoria()

    def atualizar_lista_categoria(self):
        categorias = Categoria().recuperar(self.id_usuario)


        for categoria in categorias:
            nome_categoria = categoria.get("nome")
            texto = ft.Text(value=nome_categoria)
            self.lista_categorias.append(texto)
        self.page.update()

        resultado = CategoriaView().adicionar(nome_categoria, self.login)