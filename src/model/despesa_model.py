from src.database.conexao import Conexao


class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(id_categoria: str, valor: float, data: str, descricao: str, login:str)-> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO CONECTAR")
            return None

        try:
            cursor.execute("INSERT INTO tb_despesas (id_categoria, valor, data, descricao, login) VALUES (%s, %s, %s, %s, %s, %s)", [id_categoria, valor, data, descricao, login])


            id_despesa = cursor.lastrowid

            conexao.commit()
            conexao.close()

            return id_despesa
        
        except Exception as e:
            print (f"ERRO AO INSERIR: {e}")
            return None
        
    @staticmethod
    def recuperar_todos(login: str) -> list:
        conexao, cursor = Conexao().conectar()

        if conexao == None :
            print("Erro em conexão!")
            return False

        try:
            cursor.execute("""
                            SELECT id_categoria, valor, data, descricao, login
                            FROM tb_despesas
                            WHERE login = %s
                            """, [login])

            resultado = cursor.fetchall()
            conexao.close()
            return resultado
        
        except Exception as e:
            print(f"ERRO AO RECUPERAR: {e}")
            return None
        
        
    @staticmethod
    def recuperar_categoria(login: str, id_categoria:str) -> list:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro em conexão!")
            return None

        try:
            cursor.execute("""
                            SELECT id_categoria, valor, data, descricao, login
                            FROM tb_despesas
                            WHERE login = %s,
                            AND id_categoria = %s;
                            """, [login, id_categoria])

            resultado = cursor.fetchall()
            conexao.close()
            return resultado
        
        except Exception as e:
            print(f"ERRO AO RECUPERAR DADOS: {e}")
            return None
        

    @staticmethod
    def excluir(id_despesa: int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro em conexão!")
            return None
        
        try:
            cursor.execute("SELECT id_despesa FROM tb_despesas WHERE id_despesa= %s;", [id_despesa])

            conexao.commit()
            conexao.close()

            return True
        
        except Exception as e:
            print(f"ERRO AO EXCLUIR: {e}")
            return False
        

    @staticmethod
    def alterar(id_despesa:int, id_categoria: int, descricao: str, valor: float, data: str, login: str) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro em conexão!")
            return False
        
        try:
            cursor.execute("UPDATE tb_despesas SET id_categoria = %s, descricao = %s, valor = %s, data = %s  WHERE id_despesas= %s AND login = %s;", [id_categoria, descricao, valor, data, id_despesa, login])

            conexao.commit()
            conexao.close()

            return True
        
        except Exception as e:
            print(f"ERRO AO EXCLUIR: {e}")
            return False
        

            
        