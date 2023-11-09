import tkinter as tk
from db.Conexao import Conexao
import bcrypt

class EditOrDelete(Conexao):
    def __init__(self, window, list) -> None:
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
        self.window = window
        self.list = list

    def destroyWindow(self):
        for i in self.formItems:
            i.destroy()

        self.list.buildList()

    def editItem(self):
        print('editItem')
        self.destroyWindow()
    
    def deleteItem(self):
        id = self.formItems[1].get()
        self.deletar(int(id))
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
        confirmEditButton = tk.Button(self.window, text='Editar', command=self.editItem)
        confirmEditButton.pack(pady=10)
        deleteButton = tk.Button(self.window, text='Excluir', command=self.deleteItem)
        deleteButton.pack(pady=10)
        cancelButton = tk.Button(self.window, text='Cancelar', command=self.cancel)
        cancelButton.pack(pady=10)
        self.formItems = [nameLabel, nameEntry, confirmEditButton, deleteButton, cancelButton]