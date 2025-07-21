# ui/dialogs.py
# Pide al usuario el tamaño del laberinto y el número de obstáculos mediante ventanas emergentes

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def pedir_parametros():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    # Ventana para ingresar el tamaño del laberinto
    n = simpledialog.askinteger("Tamaño", "Tamaño del laberinto:", minvalue=5, maxvalue=30)
    if n is None:
        messagebox.showinfo("Cancelado", "Se canceló la ejecución.")
        root.destroy()
        exit()

    # Ventana para ingresar el número de obstáculos
    num_obs = simpledialog.askinteger("Obstáculos", "Número de obstáculos:", minvalue=0, maxvalue=n*n - 2)
    if num_obs is None:
        messagebox.showinfo("Cancelado", "Se canceló la ejecución.")
        root.destroy()
        exit()

    root.destroy()   
    return n, num_obs

# Muestra un cuadro de mensaje emergente al usuario
def mostrar_mensaje(mensaje):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Información", mensaje)  # Muestra el mensaje
    root.destroy()