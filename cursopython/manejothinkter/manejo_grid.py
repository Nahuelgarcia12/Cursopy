import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('900x600')
ventana.resizable(0,0)
ventana.configure(background='#4DBBFA')
ventana.title('Nuevo titulo')

#configurar grid
#configuracion columna
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
# configuracion fila
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)


# manejo de grid
boton1=ttk.Button(ventana, text='boton1')
boton2=ttk.Button(ventana, text='boton2')
boton3=ttk.Button(ventana, text='boton3')
# publicar usando grid horizontal
# boton1.grid(row=0, column=0)
# boton2.grid(row=0, column=1)
# boton3.grid(row=0, column=2)
# publicar usando grid  vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)
# publicar usando grid  diagonal
boton1.grid(row=0, column=0,sticky=tk.NW) # uso de coordenadas
boton2.grid(row=1, column=1,padx=20,pady=20) #uso de pad (ubica al boton tanto pixeles como le indiques)
boton3.grid(row=2, column=2,ipadx=20,ipady=20) #uso de ipad(expanded boton)
ventana.mainloop()
# Hacemos visible la ventana
ventana.mainloop()