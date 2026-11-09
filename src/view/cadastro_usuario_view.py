import flet as ft
from src.model.usuario_model import Usuario
from src.view.voltar_login_view import Login

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina: ft.Page):
        super().__init__()
        self.route = "/cadastro"
        self.bgcolor= "#e4e0e3" 

        self.pagina = pagina

        self.horizontal_alignment= ft.CrossAxisAlignment.CENTER
        self.vertical_alignment= ft.CrossAxisAlignment.CENTER

        self.campo_usuario = ft.TextField(label= "Novo Usuário",
                                     border_color= "#000000",
                                     border_radius=8,
                                     border_width=1)

        self.campo_senha = ft.TextField(label= "Senha",
                                     border_color= "#000000",
                                     border_radius=8,
                                     border_width=1, password= True, can_reveal_password=True)
        
        subtitulo = ft.Text(value="CRIE UMA CONTA", size=30, weight="bold",
                          font_family="Georgia", color="#000000")

        botao_cadastrar= ft.Button(content="CADASTRAR" , width=200, on_click=self.cadastrar)

        botao_voltar= ft.Button(content=ft.Text(value="CLIQUE AQUI SE JA TEM UMA", text_align="CENTER"), width=200, on_click=self.ir_login)

        self.controls=[subtitulo, self.campo_usuario, self.campo_senha, botao_cadastrar, botao_voltar]

    
    def cadastrar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value

        resultado = Usuario().cadastrar(usuario,senha)

        if resultado == True:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro realizado!"), bgcolor="#414141"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao tentar cadastrar!"), bgcolor="#830000"))

    async def ir_login(self):
        await self.pagina.push_route("/login")