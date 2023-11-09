import tkinter as tk
from auth.loginForm import LoginForm

window = tk.Tk()

scream_width = window.winfo_screenwidth()
scream_height = window.winfo_screenheight()

x = int((scream_width/2) - (600/2))
y = int((scream_height/2) - (400/2))

window.geometry('%dx%d+%d+%d' % (600, 400, x, y))
window.state('zoomed')
window.configure(bg='gray')

lForm = LoginForm(window)

lForm.buildLoginForm()
window.mainloop()



