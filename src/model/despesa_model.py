from src.database.conexao import Conexao


class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(id_categoria: str, valor: float, data: str, descricao: str)-> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO INCLUIR!")
            return None
        
        try:
            cursor.execute("INSERT INTO tb_despesas (id_categoria, valor, data, descricao) VALUES (%s, %s, %s, %s, %s)", [id_categoria, valor, data, descricao])

            
        