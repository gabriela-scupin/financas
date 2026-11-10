import flet as ft
from src.model.usuario_model import Usuario

class Login(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.route= "/login"
        self.bgcolor= "#e4e0e3" 

        self.horizontal_alignment= ft.CrossAxisAlignment.CENTER
        self.vertical_alignment= ft.CrossAxisAlignment.CENTER

        self.campo_usuario = ft.TextField(label= "Faça login",
                                     border_color= "#000000",
                                     border_radius=8,
                                     border_width=1)

        self.campo_senha = ft.TextField(label= "Senha",
                                     border_color= "#000000",
                                     border_radius=8,
                                     border_width=1, password= True, can_reveal_password=True)
        
        subtitulo = ft.Text(value="ENTRE NA CONTA JA EXISTENTE", size=30, weight="bold",
                          font_family="Georgia", color="#000000")

        botao_cadastrar= ft.Button(content="ENTRAR" , width=200, on_click= self.logar)

        botao_voltar= ft.Button(content=ft.Text(value="VOLTE PARA O CADASTRO", text_align="CENTER"), width=200)

        self.controls=[subtitulo, self.campo_usuario, self.campo_senha, botao_cadastrar, botao_voltar]

    async def ir_principal(self):
        await self.page.push_route("/principal")
    async def ir_cadastro(self):
        await self.page.push_route("/cadastro")

    async def logar(self):
        usuario = self.campo_usuario.value
        senha= self.campo_senha.value

        resultado = Usuario().verificar(usuario,senha)

        if resultado :
            await self.ir_principal()
            self.page.show_dialog(ft.SnackBar(ft.Text("Login realizado com sucesso!"),
                                                bgcolor="#1f992a"))
            self.page.session.set("usuario_logado", resultado.get("usuario"))
                                                
        else:
            
            self.page.show_dialog(ft.SnackBar(ft.Text("Insira as credencias para realiar o login!"),
                                                bgcolor="#b91414"))

