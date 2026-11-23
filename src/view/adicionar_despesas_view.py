import flet as ft
from src.model.categoria import Categoria
from src.model.despesa_model import Despesa
from datetime import datetime

class AdicionarDespesasView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()


        self.pagina= pagina
        self.route = "/adicionardes"
        self.vertical_alignment="CENTER"   
        titulo= ft.Text(value="TELA DE CADASTRO CATEGORIA",weight="bold",font_family="arial")
        self.dados_usuario = pagina.session.store.get("usuario_logado")

        # Define a cor de fundo da página
        self.bgcolor = "#d3a4fa"
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.campo_descricao = ft.TextField(label="Descrição")
        self.campo_valor= ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
        self.campo_data= ft.TextField(label="Data", keyboard_type=ft.KeyboardType.DATETIME)
        categorias= Categoria().recuperar_todos(self.dados_usuario)
        opcoes = []
        
        for categoria in categorias:
            opcoes.append(ft.DropdownOption(key= categoria.get("id_categoria"), text=categoria.get("nome")))

        self.campo_categoria = ft.Dropdown(options=opcoes)

        botao_cadastrar= ft.Button(content="Cadastrar", on_click=self.incluir)

        self.controls = [titulo, self.campo_descricao, self.campo_valor, self.campo_data, self.campo_categoria, botao_cadastrar]

    def incluir(self):
        valor= self.campo_valor.value
        data= self.campo_data.value
        descricao= self.campo_descricao.value
        categoria= self.campo_categoria.value

        try:
            data = datetime.strptime(data, "%d/%m/%Y").date()
        except ValueError:
            self.pagina.show_dialog(
                ft.SnackBar(
                    ft.Text("Data inválida! Digite no formato DD/MM/AAAA"),
                    bgcolor="#ca000d"
                )
            )
            return

        #enviando para o banco de dados
        
        resultado = Despesa().incluir(categoria, valor, data, descricao, self.dados_usuario)


        if resultado == True:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro da Despesa efeituado com sucesso!"), bgcolor="#044e00"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#ca000d"))