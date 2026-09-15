import tkinter as tk

def saludar():
    # Obtener el nombre del cuadro de texto
    nombre = entrada_nombre.get()
    
    # Actualizar el Label con el saludo
    if nombre:
        label_saludo.config(text=f"¡Hola, {nombre}! Bienvenido/a")
    else:
        label_saludo.config(text="Por favor, ingresa tu nombre")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo Personalizado")
ventana.geometry("400x300")

# Crear un Label con instrucciones
label_instruccion = tk.Label(ventana, 
                             text="Ingresa tu nombre:",
                             font=("Arial", 12))
label_instruccion.pack(pady=20)

# Crear un cuadro de texto (Entry) para el nombre
entrada_nombre = tk.Entry(ventana, 
                          font=("Arial", 12),
                          width=30)
entrada_nombre.pack(pady=10)

# Crear un botón para saludar
boton_saludar = tk.Button(ventana, 
                          text="Saludar",
                          font=("Arial", 12),
                          command=saludar)
boton_saludar.pack(pady=20)

# Crear un Label para mostrar el saludo
label_saludo = tk.Label(ventana, 
                        text="",
                        font=("Arial", 14, "bold"),
                        fg="blue")
label_saludo.pack(pady=20)

# Iniciar el bucle principal
ventana.mainloop()