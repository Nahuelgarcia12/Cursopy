import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
# Redimensionar la ventana
ventana.geometry('900x600')
# Evitar redimensionar la ventana
ventana.resizable(0,0)
# Color de la ventana
ventana.configure(background='#4DBBFA')
# Modificar el titulo
ventana.title('Nuevo titulo')
#creamos la etiqueta
etiqueta = tk.Label(ventana, text='Hola esto esta programado por Nahuel')
#cambiamos el texto usando configure
etiqueta.configure(text='Hola')


#mostramos la etiqueta
etiqueta.pack(pady=30)

# Hacemos visible la ventana
ventana.mainloop()