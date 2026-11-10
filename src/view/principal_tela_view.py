import flet as ft
class PrincipalUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()


        self.pagina= pagina
        self.route = "/principal"
        dados_usuario= self.page.session.get("usuario_logado")
        nome_usuario= dados_usuario.get("login")
        self.vertical_alignment="CENTER"   
        titulo= ft.Text(value=f"""SEJA MUITO BEM-VINDO(A)!

É uma alegria ter você aqui! ❤️

Preparamos este espaço com muito carinho para oferecer a você a melhor experiência. Esperamos que se sinta à vontade, aproveite cada momento e encontre tudo o que procura.

Sua presença é muito especial para nós!

Entre, fique à vontade e sinta-se em casa! 🥰

Seja muito bem-vindo(a) {nome_usuario}! 💖""",weight="bold",font_family="arial")
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER


        self.controls = [titulo]