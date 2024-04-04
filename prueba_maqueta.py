from maqueta import Maqueta

# Definimos una maqueta de ejemplo
nombre = "Maqueta de prueba"
filas = 5
columnas = 5
entrada = (0, 0)
objetivos = {(3, 3): "A", (4, 4): "B"}
estructura = [
    "*****",
    "*---*",
    "*---*",
    "*-A-*",
    "*---*"
]

# Creamos una instancia de la maqueta
maqueta = Maqueta(nombre, filas, columnas, entrada, objetivos, estructura)

# Generamos y mostramos la configuración de la maqueta
ruta_imagen = maqueta.mostrar_configuracion()
print(f"Configuración de la maqueta guardada en: {ruta_imagen}")
