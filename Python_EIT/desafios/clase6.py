#tkinter
import tkinter as tk
def ingresar_usuario():
    nombre = caja_nombre.get()
    print('Accedio al sistema ' + nombre)

def cerrar_lop():
    ventana.destroy()

ventana = tk.Tk()
ventana.configure(width=400, height=300)
ventana.title('Pantalla principal')

etiqueta_nombre = tk.Label(text='Ingresa tu nombre: ')
etiqueta_nombre.place(x=20, y=30)

caja_nombre = tk.Entry()
caja_nombre.place(x=20, y=50,width=250, height=25)

boton_ingreso = tk.Button(text='ingresar', command=ingresar_usuario)
boton_ingreso.place(x=110, y=150, width=80, height=30)

boton_salir = tk.Button(text='salir', command=cerrar_lop)
boton_salir.place(x=290, y=150, width=80, height=30)

ventana.mainloop()