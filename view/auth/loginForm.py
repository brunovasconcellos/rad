import tkinter as tk
from tkinter import ttk
from auth.registerUser import RegisterUserForm
from dashboard.main import DashBoard

class LoginForm:
    
    def __init__(self, window):
        self.window = window
       

    def redirectToRegister(self):
        print('redirectToRegister')
        self.destroyWindow()
        rForm = RegisterUserForm(self)
        rForm.buildRegisterUserForm()

    def redirectToDashBoard(self):
        print('redirectToDashBoard')
        self.window.destroy()
        DashBoard()

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
