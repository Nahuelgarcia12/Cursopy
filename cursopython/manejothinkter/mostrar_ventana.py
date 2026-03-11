import tkinter

# Creamos una ventana
ventana = tkinter.Tk()

# Redimensionar la ventana
ventana.geometry('1000x600')

# Evitar redimensionar la ventana
ventana.resizable(0,0)

# Color de la ventana
ventana.configure(background='#1134F0')

# Modificar el titulo
ventana.title('Nuevo titulo')

# Hacemos visible la ventana
ventana.mainloop()