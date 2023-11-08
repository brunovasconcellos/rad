import tkinter as tk
from tkinter import ttk


class RegisterUserForm:
    
    def __init__(self, loginForm):
        self.window =loginForm.window
        self.loginForm = loginForm

    def redirectToLoginForm(self):
        self.destroyWindow()
        self.loginForm.buildLoginForm()


    def buildRegisterUserForm(self):
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
        btUserButton = ttk.Button(self.window ,text="Criar", command=self.redirectToLoginForm)
        btUserButton.pack(pady=10)

        formItens = [usernamelabel, usernameEntry, userPasswordlabel, userPasswordEntry, userPasswordConfirmlabel, userPasswordConfirmEntry, btUserButton]
        self.formItens = formItens

    def destroyWindow(self):
        for i in self.formItens:
            i.destroy()
