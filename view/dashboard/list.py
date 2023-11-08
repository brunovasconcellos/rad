import tkinter as tk
from tkinter import ttk
from dashboard.editOrDelete import EditOrDelete

class List:

    data = [{'id': 1, 'name': 'teste'}, {'id': 2, 'name': 'teste2'}, {'id': 3, 'name': 'teste3'}]

    def __init__(self, window):
        self.window = window
    
    def editItem(self, event):
        print('editItem')
        self.destroyWindow()
        editOrDelete = EditOrDelete(self.window, self)
        editOrDelete.buildForm()
    
    def buildList(self):
  
        columns = ("id", "name")
        listData = self.getListData()
        treeview = ttk.Treeview(self.window, columns=columns, show='headings')
        treeview.heading('id', text='ID')
        treeview.heading('name', text='Nome')

        for i in range(len(listData)):
            treeview.insert('', tk.END, values=(listData[i]['id'], listData[i]['name']))
            treeview.bind('<<TreeviewSelect>>', self.editItem)

               
        treeview.pack()
        self.treeview = treeview

    def getListData(self):
        return self.data
    
    def destroyWindow(self):
       self.treeview.destroy()