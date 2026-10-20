from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(categoria: str, login: str)-> int:
        conexao, cursor = Conexao().conectar()
        
        if not conexao:
            print ("Erro ao tentar adicionar!")
            return None