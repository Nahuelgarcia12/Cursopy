import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('900x600')
ventana.resizable(0,0)
ventana.configure(background='#4DBBFA')
ventana.title('Nuevo titulo')

def mostrar():
  texto = caja_texto.get()  # recuperando el valor de la caja de texto
  print(f'Texto proporcionado: {texto}')
  # Accedemos al texto de la etiqueta
  etiqueta['text'] = texto

# Caja de texto
caja_texto = ttk.Entry(ventana, font = ('Arial', 15))
caja_texto.pack(pady=20)

# Agregamos boton
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=20)

# Agrgamos etiqueta
etiqueta = ttk.Label(ventana, text='Valor inicial')
etiqueta.pack(pady=20)

# Hacemos visible la ventana
ventana.mainloop()