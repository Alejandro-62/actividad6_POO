import tkinter as tk
from tkinter import messagebox
import os

ARCHIVO_CONTACTOS = "datos_contactos.txt"

def obtener_contactos():
    lista_contactos = []
    if os.path.exists(ARCHIVO_CONTACTOS):
        with open(ARCHIVO_CONTACTOS, "r") as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split("!")
                lista_contactos.append((nombre, telefono))
    return lista_contactos

def agregar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_numero.get()

    if nombre == "" or telefono == "":
        messagebox.showwarning("Aviso", "Los campos deben completarse.")
        return

    lista_contactos = obtener_contactos()

    for contacto in lista_contactos:
        if contacto[0] == nombre or contacto[1] == telefono:
            messagebox.showwarning("Aviso", "Este contacto ya está registrado.")
            return

    with open(ARCHIVO_CONTACTOS, "a") as archivo:
        archivo.write(f"{nombre}!{telefono}\n")
    
    messagebox.showinfo("Éxito", "Nuevo contacto guardado.")
    limpiar_campos()
    actualizar_lista()

def actualizar_lista():
    lista_contactos = obtener_contactos()
    lista_mostrar.delete(0, tk.END)
    for contacto in lista_contactos:
        lista_mostrar.insert(tk.END, f"{contacto[0]} - {contacto[1]}")

def modificar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_numero.get()

    if nombre == "" or telefono == "":
        messagebox.showwarning("Aviso", "Los campos deben completarse.")
        return

    lista_contactos = obtener_contactos()

    modificado = False
    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        for contacto in lista_contactos:
            if contacto[0] == nombre:
                archivo.write(f"{nombre}!{telefono}\n")
                modificado = True
            else:
                archivo.write(f"{contacto[0]}!{contacto[1]}\n")

    if modificado:
        messagebox.showinfo("Éxito", "Contacto modificado correctamente.")
    else:
        messagebox.showwarning("Aviso", "No se encontró el contacto.")
    
    limpiar_campos()
    actualizar_lista()

def eliminar_contacto():
    nombre = entrada_nombre.get()

    if nombre == "":
        messagebox.showwarning("Aviso", "Debe ingresar un nombre.")
        return

    lista_contactos = obtener_contactos()

    eliminado = False
    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        for contacto in lista_contactos:
            if contacto[0] == nombre:
                eliminado = True
            else:
                archivo.write(f"{contacto[0]}!{contacto[1]}\n")

    if eliminado:
        messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
    else:
        messagebox.showwarning("Aviso", "No se encontró el contacto.")
    
    limpiar_campos()
    actualizar_lista()

def limpiar_campos():
    entrada_nombre.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Gestión de Contactos")

etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

etiqueta_numero = tk.Label(ventana, text="Teléfono:")
etiqueta_numero.grid(row=1, column=0, padx=10, pady=10)

entrada_numero = tk.Entry(ventana)
entrada_numero.grid(row=1, column=1, padx=10, pady=10)

boton_agregar = tk.Button(ventana, text="Añadir", command=agregar_contacto)
boton_agregar.grid(row=2, column=0, padx=10, pady=10)

boton_mostrar = tk.Button(ventana, text="Ver lista", command=actualizar_lista)
boton_mostrar.grid(row=2, column=1, padx=10, pady=10)

boton_modificar = tk.Button(ventana, text="Editar", command=modificar_contacto)
boton_modificar.grid(row=3, column=0, padx=10, pady=10)

boton_eliminar = tk.Button(ventana, text="Borrar", command=eliminar_contacto)
boton_eliminar.grid(row=3, column=1, padx=10, pady=10)

lista_mostrar = tk.Listbox(ventana, width=40)
lista_mostrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

actualizar_lista()

ventana.mainloop()
