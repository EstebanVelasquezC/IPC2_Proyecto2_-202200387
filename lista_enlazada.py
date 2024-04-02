class ListaEnlazada:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None

    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def esta_vacia(self):
        return self.primer_nodo is None

    def agregar_al_final(self, dato):
        nuevo_nodo = self.Nodo(dato)
        if self.esta_vacia():
            self.primer_nodo = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo

    def __str__(self):
        if self.esta_vacia():
            return "Lista vacía"
        else:
            nodos = []
            nodo_actual = self.primer_nodo
            while nodo_actual:
                nodos.append(str(nodo_actual.dato))
                nodo_actual = nodo_actual.siguiente
            return " -> ".join(nodos)


