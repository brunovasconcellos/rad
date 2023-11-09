import tkinter as tk
from tkinter import ttk
from view.dashboard.editOrDelete import EditOrDelete
from db.Conexao import Conexao
import bcrypt

class List(Conexao):

    data = [{'id': 1, 'name': 'teste'}, {'id': 2, 'name': 'teste2'}, {'id': 3, 'name': 'teste3'}]

    def __init__(self, window):
        super().__init__()
        self.conexao = self.criarConexao()
        self.cursor = self.criarCursor()
        self.salt = bcrypt.gensalt()
        self.window = window
    
    def editItem(self, event):
        print('editItem')
        self.destroyWindow()
        editOrDelete = EditOrDelete(self.window, self)
        editOrDelete.buildForm()
    
    def buildList(self):
        self.window.title('Dashboard')
        columns = ("id", "nome", "descricao")
        listData = self.getListData()
        treeview = ttk.Treeview(self.window, columns=columns, show='headings')
        treeview.heading('id', text='ID')
        treeview.heading('nome', text='Nome')
        treeview.heading('descricao', text='Descrição')

        for i in range(len(listData)):
            treeview.insert('', tk.END, values=(listData[i]['ID'], listData[i]['NOME'], listData[i]["DESCRICAO"]))
            treeview.bind('<<TreeviewSelect>>', self.editItem)

               
        treeview.pack()
        self.treeview = treeview

    def getListData(self):
        return self.selecionar()
    
    def destroyWindow(self):
       self.treeview.destroy()