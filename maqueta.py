class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada, objetivos, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.entrada = entrada
        self.objetivos = objetivos
        self.estructura = estructura

    def __str__(self):
        return f"Maqueta: {self.nombre} - Filas: {self.filas}, Columnas: {self.columnas}, Objetivos: {len(self.objetivos)}"

    def obtener_estructura(self):
        matriz = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(self.estructura[i * self.columnas + j])
            matriz.append(fila)
        return matriz
