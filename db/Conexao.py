import sqlite3 as sql
import pandas as pd
import bcrypt
from io import BytesIO



class Conexao():
    def __init__(self):
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
    def criarConexao(self):
        try:
            conn = sql.connect("projeto.db")
            return conn
        except Exception as e:
            return f"O seguinte erro aconteceu {e}"
        
    def criarCursor(self):
        try:
            cursor = self.conexao.cursor()
            return cursor
        except Exception as e:
            return f"O seguinte erro aconteceu {e}"
    
    def criarCadastro(self, login, senha):
        try:
            cadastro = []
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                login VARCHAR(255),
                                senha VARCHAR(255))""")
            senha_bytes = bytes(senha, encoding='utf8')
            senha_hash = bcrypt.hashpw(senha_bytes, self.salt)
            
            
            self.cursor.execute("INSERT INTO cadastro(login, senha) VALUES(?, ?)", (login, senha_hash,))
            self.conexao.commit()
            print("Cadastro feito com sucesso.")
        except Exception as e:
            return f"O seguinte erro aconteceu {e}"
        
    def login(self, login, senha):
        
            confirm = self.cursor.execute("SELECT senha FROM cadastro WHERE login = ?", (login,))
            confirm = confirm.fetchone()
            senha = (bytes(senha, encoding='utf8'))
            if bcrypt.checkpw(senha, confirm[0]):
                print("Login feito com sucesso.")
            else:
                print("não ok")
        
    def inserir(self, valores:list):        
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                cpf TEXT,
                                idade INTEGER)""")
            
            self.cursor.execute("INSERT INTO pessoa(nome, cpf, idade) VALUES(?, ?, ?)", valores)
            self.conexao.commit()
        except Exception as e:
            return f"O seguinte erro aconteceu {e}"
        
    def selecionar(self):
        try:
            res = self.cursor.execute("SELECT * FROM cadastro")
            res = res.fetchall()
            return res
        except Exception as e:
            return f"O seguinte erro aconteceu {e}"
    
    def deletar(self, id:int):
        try:
            self.cursor.execute("DELETE FROM cadastro WHERE id = ?", id)
            self.conexao.commit()
        except Exception as e:
            return f"O seguinte erro aconteceu {e}"
        
    def fecharConexao(self):
        return self.conexao.close()
        
    

db = Conexao()
db.criarConexao()
db.criarCursor()
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
#db.criarCadastro(login, senha)
db.login(login, senha)
#db.inserir(["felipe","0000000",26])
#db.deletar(0)
#df = pd.DataFrame(db.selecionar())
#print(df.to_string())
db.fecharConexao()

