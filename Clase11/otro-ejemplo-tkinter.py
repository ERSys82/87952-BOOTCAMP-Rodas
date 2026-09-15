import tkinter as tk

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("640x480")  # Tamaño 640x480

# Creamos un Label con un texto
etiqueta = tk.Label(ventana, 
                    text="¡Hola! Esta es mi ventana en Tkinter",
                    font=("Arial", 16))
etiqueta.pack(pady=50)  # pady añade espacio vertical

# Creamos un botón "Salir" que cierra la ventana
boton_salir = tk.Button(ventana, 
                        text="Salir",
                        font=("Arial", 12),
                        command=ventana.destroy)  # Cierra la ventana al hacer clic
boton_salir.pack()

# Iniciamos el bucle principal de la aplicación
ventana.mainloop()