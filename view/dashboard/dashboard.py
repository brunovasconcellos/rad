import tkinter as tk
from view.dashboard.list import List

class DashBoard:
   def __init__(self) -> None:
      window = tk.Tk()
      window.geometry('1024x720')
      window.state('zoomed')
      window.configure(bg='gray')

      list = List(window)

      list.buildList()

      window.mainloop()