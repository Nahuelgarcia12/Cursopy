import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1140CF')
ventana.title('Login')

#creamos estilo
estilos =ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#B5B1B1',
                  foreground='white',fieldbackground='black')
estilos.configure('TFrame', background='black')

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

#agregamos el frame
frame=ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

#titulo
etiqueta= ttk.Label(frame,text='login',font=('arial',22))
etiqueta.grid(row=0,column=0,columnspan=2)

#usuario
usuario_etiqueta=ttk.Label(frame,text='usuario')
usuario_etiqueta.grid(row=1,column=0,sticky=tk.W,padx=5,pady=20)

usuario_caja_texto=ttk.Entry(frame)
usuario_caja_texto.grid(row=1,column=1,sticky=tk.E,padx=5,pady=5)

password_etiqueta=ttk.Label(frame,text='password')
password_etiqueta.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)

password_caja_texto=ttk.Entry(frame,show='*')
password_caja_texto.grid(row=2,column=1,sticky=tk.E,padx=5,pady=5)

#boton
login_boton=ttk.Button(frame,text='enviar')
login_boton.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

frame.grid(row=0,column=0)

def validar(event):
    usuario=usuario_caja_texto.get()
    password = password_caja_texto.get()
    # unico usuario valido, user=root y password=admin
    if usuario=='root' and password=='admin':
        showinfo(title='login',message='login sucessful')
    else:
        showerror(title='login',message='login failed')

#asociar eventos al boton de login
login_boton.bind('<Return>',validar) #presionar tecla enter
login_boton.bind('<Button-1>',validar) #click izquierdo del mouse
ventana.mainloop()