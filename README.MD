# Monitor de Estado de Estacionamiento

Este proyecto es una aplicación en Python que muestra en una interfaz gráfica el estado de los espacios de estacionamiento. Se conecta a un Arduino vía puerto serial para recibir datos en tiempo real sobre la cantidad de espacios disponibles y ocupados.

---

## Características

- Interfaz en pantalla completa con opción para salir con la tecla ESC.
- Visualización en tiempo real del estado de cada espacio de estacionamiento.
- Indicación visual (color y emoji) para espacios libres y ocupados.
- Se conecta a Arduino que envía datos a través del puerto COM.

---

## Requisitos

- Python 3.x
- Librerías:
  - `pyserial` (para comunicación serial)
  - `tkinter` (normalmente incluido en Python)
  
Para instalar `pyserial`, usa:
```bash  
pip install pyserial  