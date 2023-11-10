import tkinter as tk
from tkinter import ttk
from db.Conexao import Conexao
import bcrypt


class RegisterUserForm(Conexao):
    def __init__(self, loginForm):
        super().__init__()
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
        self.window = loginForm.window
        self.loginForm = loginForm

    def createUser(self):
        usuario = self.formItens[1].get()
        senha = self.formItens[3].get()
        confirmacao_senha = self.formItens[5].get()
        if(senha != confirmacao_senha):
            passwordErrLabel = tk.Label(self.window, text='As senhas não coincidem', fg='red', bg='gray')
            passwordErrLabel.pack(pady=10)
            self.formItens.append(passwordErrLabel)
            return
        elif(not usuario or not senha or not confirmacao_senha):
            emptyFieldErrLabel = tk.Label(self.window, text='Preencha todos os campos', fg='red', bg='gray')
            emptyFieldErrLabel.pack(pady=10)
            self.formItens.append(emptyFieldErrLabel)
            return
        else:
            self.criarCadastro(usuario, senha)
        self.destroyWindow()
        self.redirectToLoginForm()

    def redirectToLoginForm(self):
        self.destroyWindow()
        self.loginForm.buildLoginForm()


    def buildRegisterUserForm(self):
        self.window.title('Cadastro')
        usernamelabel = tk.Label(self.window, text='Nome de usuário', bg='gray')
        usernamelabel.pack()
        usernameEntry = tk.Entry(self.window)
        usernameEntry.pack()
        userPasswordlabel = tk.Label(self.window, text='Senha', bg='gray')
        userPasswordlabel.pack()
        userPasswordEntry = tk.Entry(self.window)
        userPasswordEntry.config(show='*')
        userPasswordEntry.pack()
        userPasswordConfirmlabel = tk.Label(self.window, text='Confirmar senha', bg='gray')
        userPasswordConfirmlabel.pack()
        userPasswordConfirmEntry = tk.Entry(self.window)
        userPasswordConfirmEntry.config(show='*')
        userPasswordConfirmEntry.pack()
        btUserButton = ttk.Button(self.window ,text="Criar", command=self.createUser)
        btUserButton.pack(pady=10)
        redirectToLoginButton = ttk.Button(self.window ,text="Voltar", command=self.redirectToLoginForm)
        redirectToLoginButton.pack(pady=10)
        formItens = [usernamelabel, usernameEntry, userPasswordlabel, userPasswordEntry, userPasswordConfirmlabel, userPasswordConfirmEntry, btUserButton, redirectToLoginButton]
        self.formItens = formItens

    def destroyWindow(self):
        
        for i in self.formItens:
            i.destroy()
