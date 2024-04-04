import graphviz

class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada, objetivos, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.entrada = entrada
        self.objetivos = objetivos
        self.estructura = estructura

    def generar_grafo_maqueta(self):
        grafo = graphviz.Digraph(comment=self.nombre)

        for fila in range(self.filas):
            with grafo.subgraph() as sub:
                for columna in range(self.columnas):
                    nodo = f"{fila}-{columna}"
                    # Definir forma y color de acuerdo a la estructura de la maqueta
                    if self.estructura[fila][columna] == "*":
                        sub.node(nodo, shape="square", style="filled", fillcolor="black")
                    elif self.estructura[fila][columna] == "-":
                        sub.node(nodo, shape="square", style="filled", fillcolor="white")
                    else:
                        sub.node(nodo, shape="point")
                    # Definir nodo de entrada con color específico
                    if (fila, columna) == self.entrada:
                        sub.node(nodo, shape="square", style="filled", fillcolor="#98FB98")

        return grafo

    def mostrar_configuracion(self):
        grafo = self.generar_grafo_maqueta()
        return grafo.render(filename=f"maqueta_{self.nombre}", format="png", cleanup=True)
