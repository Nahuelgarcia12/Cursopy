import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

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

def saludar(nombre):
    mensaje = f'Saludos..{nombre}'
    print(mensaje)
    showinfo(title='mensaje', message=mensaje)

#botones
boton1=ttk.Button(ventana,text='enviar',command=  lambda : saludar('Nahuel'))
boton1.pack(pady=50)



# Hacemos visible la ventana
ventana.mainloop()