import flet as ft
from src.model.usuario_model import Usuario

class Main(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route= "/login"
        self.bgcolor= "#e4e0e3" 

        self.horizontal_alignment= ft.CrossAxisAlignment.CENTER
        self.vertical_alignment= ft.CrossAxisAlignment.CENTER

        campo_login = ft.Text(value= "login")

        self.controls =  [campo_login]