import tkinter as tk
from tkinter import ttk


class RegisterUserForm:
    def __init__(self, loginForm):
        self.window = loginForm.window
        self.loginForm = loginForm

    def createUser(self):
        print('createUser')
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
        userPasswordEntry.pack()
        userPasswordConfirmlabel = tk.Label(self.window, text='Confirmar senha', bg='gray')
        userPasswordConfirmlabel.pack()
        userPasswordConfirmEntry = tk.Entry(self.window)
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
