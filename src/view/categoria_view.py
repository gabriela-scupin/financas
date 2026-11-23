import flet as ft
from src.model.categoria import Categoria
from src.model.usuario_model import Usuario

class CategoriaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/categoria"
        self.bgcolor ="#FFEEFA"
        self.horizontal_alignment ="center"
        self.vertical_alignment = "center"


        self.dados_usuario = pagina.session.store.get("usuario_logado")
        
        titulo = ft.Text(value="Página Categoria",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#7A0047")
        self.campo_nome_categoria = ft.TextField(label=" Nome da Categoria",
                                            border_color="#9E6084",
                                            width= 250)
        botao_cadastrar = ft.Button(content="Incluir",
                                    bgcolor="#FFEEFA",
                                    color="#7A0047",
                                    width=250, on_click=self.cadastrar_categoria)
        
        self.controls =[titulo,
                        self.campo_nome_categoria,
                        botao_cadastrar]
    def cadastrar_categoria(self):
        nome_categoria = self.campo_nome_categoria.value


        resultado = Categoria().adicionar(nome_categoria, self.dados_usuario)
        
        if resultado == True:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efeituado com sucesso!"), bgcolor="#044e00"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#ca000d"))

            