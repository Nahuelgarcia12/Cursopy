import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('900x600')
ventana.resizable(0,0)
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

# configuramos el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam') # tema oscuro
estilos.configure('Treeview', background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30)
estilos.map('Treeview', background=[('selected','#3a86ff')])

# Definimos las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabeceros a la tabla
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas
tabla.column('Id', width=80, anchor=tk.CENTER)
tabla.column('Nombre', width=120, anchor=tk.W)
tabla.column('Edad', width=120, anchor=tk.W)

# Cargar datos a la tabla
#datos = ((1, 'Alexandra', 25), (2, 'Matias', 32))
datos = ((1, 'Alexandra', 25), (2, 'Matias', 32)) + ((3, 'Alex', 28), (4, 'Martina', 33)) + ((5, 'Alejandra', 20), (6, 'Nicolas', 23)) + ((7, 'Alejo', 50), (8, 'Mariano', 38)) + ((9, 'Alberto', 65), (10, 'Mora', 32)) + ((11, 'Alma', 29), (12, 'Maria', 22))
for persona in datos:
  tabla.insert(parent='', index=tk.END, values=persona)

tabla.grid(row=0, column=0, sticky=tk.NSEW)

# agregar un scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# Mostrar registro seleccionado
def mostrar_seleccionado(event):
  print('Ejecutando metodo mostrar_seleccionado')
  elemento_seleccionado = tabla.selection()[0]  # item seleccionado - elemento
  elemento = tabla.item(elemento_seleccionado) # item
  persona = elemento['values'] # tupla de persona
  print(persona)
  showinfo(title='Persona seleccionada', message=f'Persona: {persona}')

# asociar el evento select de  la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_seleccionado)


ventana.mainloop()