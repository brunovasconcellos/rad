import tkinter as tk
from db.Conexao import Conexao
import bcrypt

class EditOrDelete(Conexao):
    def __init__(self, window, list, treeViewData) -> None:
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
        self.window = window
        self.list = list
        self.treeViewData = treeViewData

    def destroyWindow(self):
        for i in self.formItems:
            i.destroy()

        self.list.buildList()

    def editItem(self):
        id = self.treeViewData[0]
        desc = self.formItems[1].get()
        nome = self.formItems[3].get()

        if (nome == '' or desc == ''):
            label = tk.Label(self.window, text='Preencha todos os campos', fg='red', bg='gray')
            label.pack(pady=10)
            self.formItems.append(label)
            return

        self.editar(desc, nome, id)
        self.destroyWindow()
    
    def deleteItem(self):
        id = self.treeViewData[0]
        self.deletar(id)
        self.destroyWindow()

    def cancel(self):
        print('cancel')
        self.destroyWindow()
        

    def buildForm(self):
        print('buildForm')
        nameLabel = tk.Label(self.window, text='Nome', bg='gray')
        nameLabel.pack()
        nameEntry = tk.Entry(self.window)
        nameEntry.insert(0, self.treeViewData[1])
        nameEntry.pack()
        descriptionLabel = tk.Label(self.window, text='Descrição', bg='gray')
        descriptionLabel.pack()
        descriptionEntry = tk.Entry(self.window)
        descriptionEntry.insert(0, self.treeViewData[2])
        descriptionEntry.pack()
        confirmEditButton = tk.Button(self.window, text='Editar', command=self.editItem)
        confirmEditButton.pack(pady=10)
        deleteButton = tk.Button(self.window, text='Excluir', command=self.deleteItem)
        deleteButton.pack(pady=10)
        cancelButton = tk.Button(self.window, text='Cancelar', command=self.cancel)
        cancelButton.pack(pady=10)
        self.formItems = [nameLabel, nameEntry, descriptionLabel, descriptionEntry, confirmEditButton, deleteButton, cancelButton]