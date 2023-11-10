import tkinter as tk
from tkinter import ttk
from view.auth.registerUser import RegisterUserForm
from view.dashboard.dashboard import DashBoard
from db.Conexao import Conexao
import bcrypt

class LoginForm(Conexao):
    
    def __init__(self, window):
        super().__init__()
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
        self.window = window
       

    def redirectToRegister(self):
        print('redirectToRegister')
        self.destroyWindow()
        rForm = RegisterUserForm(self)
        rForm.buildRegisterUserForm()

    def redirectToDashBoard(self):
        usuario = self.formItens[1].get()
        senha = self.formItens[3].get()
        try:
            if self.login(usuario, senha):
                self.window.destroy()
                DashBoard()
            else:
                errorLabel = tk.Label(self.window, text='Usuário ou senha incorretos', fg='red', bg='gray')
                errorLabel.pack(pady=10)
                self.formItens.append(errorLabel)
        except Exception as e:
            errorLabel = tk.Label(self.window, text='Usuário ou senha incorretos', fg='red', bg='gray')
            errorLabel.pack(pady=10)
            self.formItens.append(errorLabel)

    def buildLoginForm(self):
        self.window.title('Login')
        usernamelabel = tk.Label(self.window, text='Nome de usuário', bg='gray')
        usernamelabel.pack()
        usernameEntry = tk.Entry(self.window)
        usernameEntry.pack()
        userPasswordlabel = tk.Label(self.window, text='Senha', bg='gray')
        userPasswordlabel.pack()
        userPasswordEntry = tk.Entry(self.window)
        userPasswordEntry.config(show='*')
        userPasswordEntry.pack()
        btnLogin = ttk.Button(self.window ,text="Entrar", command=self.redirectToDashBoard)
        btnLogin.pack(pady=10)
        btnRegisterButton = ttk.Button(self.window ,text="Cadastre-se", command=self.redirectToRegister)
        btnRegisterButton.pack(pady=10)
        formItens = [usernamelabel, usernameEntry, userPasswordlabel, userPasswordEntry, btnLogin, btnRegisterButton]
        self.formItens = formItens
        

    def destroyWindow(self):
        for i in self.formItens:
            i.destroy()
