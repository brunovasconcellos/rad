import tkinter as tk
from tkinter import ttk
from view.dashboard.editOrDelete import EditOrDelete
from view.dashboard.create import Create
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

    def createItem(self):
        print('createItem')
        self.destroyWindow()
        create = Create(self.window, self)
        create.buildForm()
    
    def editItem(self, event):
        print('editItem')
        treeView = ''
        for i in self.elements:
            if type(i) == ttk.Treeview:
                treeView = i
                break

        if treeView == '':
            return
        
        selected_item = treeView.selection()[0]
        treeViewData = treeView.item(selected_item)['values']
        print(treeViewData)
        self.destroyWindow()
        self.destroyWindow()
        editOrDelete = EditOrDelete(self.window, self, treeViewData)
        editOrDelete.buildForm()
    
    def buildList(self):
        self.window.title('Dashboard')
        self.elements = []
        columns = ("id", "nome", "descricao")
        listData = self.getListData()
        
        if (type(listData) != str):
            treeview = ttk.Treeview(self.window, columns=columns, show='headings')
            treeview.heading('id', text='ID')
            treeview.heading('nome', text='Nome')
            treeview.heading('descricao', text='Descrição')

            for i in range(len(listData)):
                treeview.insert('', tk.END, values=(listData[i]['ID'], listData[i]['NOME'], listData[i]["DESCRICAO"]))
                treeview.bind('<<TreeviewSelect>>', self.editItem)

            treeview.pack()
            self.elements.append(treeview)

        createData: tk.Button = tk.Button(self.window, text='Criar', command=self.createItem)
        createData.pack(pady=10)
        self.elements.append(createData)

    def getListData(self):
        return self.selecionar()
    
    def destroyWindow(self):
        for i in self.elements:
            i.destroy()