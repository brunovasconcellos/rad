import tkinter as tk
from db.Conexao import Conexao
import bcrypt

class Create(Conexao):
    def __init__(self, window, list) -> None:
        super().__init__()
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
        self.window = window
        self.list = list

    def destroyWindow(self):
        for i in self.formItems:
            i.destroy()

        self.list.buildList()

    def createItem(self):
        nome = self.formItems[1].get()
        descricao = self.formItems[3].get()
        self.inserir([nome, descricao])
        self.destroyWindow()
    
    def cancel(self):
        print('cancel')
        self.destroyWindow()
        

    def buildForm(self):
        print('buildForm')
        nameLabel = tk.Label(self.window, text='Nome', bg='gray')
        nameLabel.pack()
        nameEntry = tk.Entry(self.window)
        nameEntry.pack()
        descriptionLabel = tk.Label(self.window, text='Descrição', bg='gray')
        descriptionLabel.pack()
        descriptionEntry = tk.Entry(self.window)
        descriptionEntry.pack()
        confirmButton = tk.Button(self.window, text='Criar', command=self.createItem)
        confirmButton.pack(pady=10)
        cancelButton = tk.Button(self.window, text='Cancelar', command=self.cancel)
        cancelButton.pack(pady=10)
        self.formItems = [nameLabel, nameEntry, descriptionLabel, descriptionEntry, confirmButton, cancelButton]