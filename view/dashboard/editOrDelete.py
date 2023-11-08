import tkinter as tk

class EditOrDelete:
    def __init__(self, window, list) -> None:
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
        print('deleteItem')
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