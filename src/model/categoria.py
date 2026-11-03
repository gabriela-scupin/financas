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
        

        try:
            cursor.execute("INSERT INTO tb_categoria (nome, login) VALUES (%s, %s)", [categoria, login])
            id_categoria = cursor.lastrowid
                
            conexao.commit()
            conexao.close()

            return id_categoria
        

        except Exception as e:
            print(f"ERRO: {e}")
            return None
        
    @staticmethod
    def excluir(id_categoria: int)-> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao excluir")
            return None
        
        cursor.execute("DELETE FROM tb_categoria where id_categoria = %s", [id_categoria])

        resultado = cursor.fetchone()

        conexao.close()
        
        return resultado
    
    @staticmethod
    def recuperar_todos(login: str) -> list[dict]:
        conexao, cursor = Conexao().conectar()

        if not conexao :
            print("Erro em conexão!")
            return None

        try:
            cursor.execute("""
                            SELECT id_categoria, nome , id_usuario
                            FROM tb_categorias
                            WHERE login = %s
                            """, [login])

            categoria = cursor.fetchall()
            conexao.close()
            return categoria
        except Exception as e:
            print(f"ERRO AO RECUPERAR: {e}")
            return None