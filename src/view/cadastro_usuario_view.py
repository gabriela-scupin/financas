import flet as ft

class CadastroUsuarioView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.bgcolor= "#e4e0e3" 

        self.horizontal_alignment= ft.CrossAxisAlignment.CENTER

        campo_usuario = ft.TextField(label= "Novo Usuário",
                                     border_color= "#000000",
                                     border_radius=8,
                                     border_width=1)

        campo_senha = ft.TextField(label= "Senha",
                                     border_color= "#000000",
                                     border_radius=8,
                                     border_width=1, password= True, can_reveal_password=True)
        
        subtitulo = ft.Text(value="Preencha os dados abaixo", size=30, weight="bold",
                          font_family="Georgia", color="#000000")

        botao_cadastrar= ft.Button(content="CADASTRAR" , width=200)

        botao_voltar= ft.Button(content="VOLTE PARA O LOGIN", width=200)

        self.controls=[subtitulo, campo_usuario, campo_senha, botao_cadastrar, botao_voltar]
