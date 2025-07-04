import serial
import tkinter as tk
from threading import Thread

# Purto COM
arduino = serial.Serial('COM8', 9600, timeout=1)

ESPACIOS_TOTALES = 8

ventana = tk.Tk()
ventana.title("Estado del Estacionamiento")
ventana.attributes('-fullscreen', True)  # PANTALLA COMPLETA
ventana.configure(bg="#f2f2f2")

# Salir de pantalla completa con ESC
def salir_pantalla_completa(event=None):
    ventana.attributes('-fullscreen', False)

ventana.bind("<Escape>", salir_pantalla_completa)

# Header
header = tk.Frame(ventana, bg="#f2f2f2")
header.pack(fill="x", pady=10)

titulo = tk.Label(header, text="Espacios disponibles:", font=("Arial", 24, "bold"), bg="#f2f2f2")
titulo.pack()

contador = tk.Label(header, text="Cargando...", font=("Arial", 30), fg="blue", bg="#f2f2f2")
contador.pack()

# Contenedor de los espacios
contenedor = tk.Frame(ventana, bg="#f2f2f2")
contenedor.pack(expand=True, fill="both", padx=50, pady=50)

# Configurar el grid
filas = 2
columnas = 4

for i in range(filas):
    contenedor.rowconfigure(i, weight=1)
for j in range(columnas):
    contenedor.columnconfigure(j, weight=1)

espacios_gui = []
for i in range(ESPACIOS_TOTALES):
    fila = i // columnas
    columna = i % columnas
    espacio = tk.Label(
        contenedor,
        text="🟢 LIBRE",
        font=("Arial", 26, "bold"),
        relief="groove",
        bg="#ffffff",
        fg="green"
    )
    espacio.grid(row=fila, column=columna, padx=20, pady=20, sticky="nsew")
    espacios_gui.append(espacio)

def actualizar_estacionamiento(disponibles):
    ocupados = ESPACIOS_TOTALES - disponibles
    contador.config(text=f"{disponibles} de {ESPACIOS_TOTALES}")
    for i in range(ESPACIOS_TOTALES):
        if i < ocupados:
            espacios_gui[i].config(text="🔴 OCUPADO", fg="red")
        else:
            espacios_gui[i].config(text="🟢 LIBRE", fg="green")

def leer_arduino():
    while True:
        try:
            linea = arduino.readline().decode().strip()
            if linea.startswith("ESPACIOS:"):
                espacios = int(linea.split(":")[1])
                ventana.after(0, actualizar_estacionamiento, espacios)
        except Exception as e:
            print("Error:", e)
            continue

Thread(target=leer_arduino, daemon=True).start()

ventana.mainloop()
