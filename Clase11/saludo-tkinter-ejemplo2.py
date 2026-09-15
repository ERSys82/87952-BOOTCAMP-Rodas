import tkinter as tk


# ============================================
# FUNCIONES PURAS (100% puras, sin tocar GUI)
# ============================================

def validar_nombre(nombre: str) -> bool:
    """Verifica si el nombre es válido."""
    return bool(nombre.strip())


def generar_mensaje_saludo(nombre: str) -> str:
    """Genera el mensaje de saludo."""
    if validar_nombre(nombre):
        return f"¡Hola, {nombre.strip()}! Bienvenido/a"
    return "Por favor, ingresa tu nombre"


def generar_color_saludo(nombre: str) -> str:
    """Devuelve el color según si el nombre es válido."""
    return "blue" if validar_nombre(nombre) else "red"


def procesar_saludo_completo(nombre: str) -> dict:
    """Función pura que procesa todo y devuelve resultados."""
    return {
        "mensaje": generar_mensaje_saludo(nombre),
        "color": generar_color_saludo(nombre),
        "es_valido": validar_nombre(nombre)
    }


# ============================================
# FUNCIONES DE GUI (necesariamente impuras)
# ============================================

def crear_ventana() -> tk.Tk:
    """Crea y configura la ventana principal."""
    ventana = tk.Tk()
    ventana.title("Saludo Personalizado")
    ventana.geometry("400x300")
    return ventana


def crear_widgets(ventana: tk.Tk) -> tuple:
    """Crea todos los widgets y los devuelve."""
    # Label de instrucciones
    label_instruccion = tk.Label(
        ventana,
        text="Ingresa tu nombre:",
        font=("Arial", 12)
    )
    label_instruccion.pack(pady=20)

    # Entry para el nombre
    entrada_nombre = tk.Entry(
        ventana,
        font=("Arial", 12),
        width=30
    )
    entrada_nombre.pack(pady=10)

    # Label para el saludo
    label_saludo = tk.Label(
        ventana,
        text="",
        font=("Arial", 14, "bold")
    )
    label_saludo.pack(pady=20)

    return entrada_nombre, label_saludo


def actualizar_saludo_gui(entrada: tk.Entry, label: tk.Label) -> None:
    """Lee el nombre y actualiza el label (usa función pura internamente)."""
    nombre = entrada.get()
    
    # Llama a la función PURA para procesar
    resultado = procesar_saludo_completo(nombre)
    
    # Actualiza la GUI (efecto secundario)
    label.config(text=resultado["mensaje"], fg=resultado["color"])


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    # Crear ventana
    ventana = crear_ventana()
    
    # Crear widgets
    entrada_nombre, label_saludo = crear_widgets(ventana)
    
    # Botón que usa la función de GUI
    boton_saludar = tk.Button(
        ventana,
        text="Saludar",
        font=("Arial", 12),
        command=lambda: actualizar_saludo_gui(entrada_nombre, label_saludo)
    )
    boton_saludar.pack(pady=20)
    
    # Iniciar bucle principal
    ventana.mainloop()


if __name__ == "__main__":
    main()