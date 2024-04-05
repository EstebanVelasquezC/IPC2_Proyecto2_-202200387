import graphviz as gv

def mostrar_configuracion_maqueta_graphviz(maqueta):
    # Crear un objeto Graph
    graph = gv.Graph()

    # Agregar nodos para cada posición
    for fila in range(maqueta['filas']):
        for columna in range(maqueta['columnas']):
            # Obtener el caracter de la estructura
            caracter = maqueta['estructura'][fila * maqueta['columnas'] + columna]

            # Asignar un color al nodo
            if caracter == '*':
                color = 'black'
            elif caracter == '-':
                color = 'white'
            else:
                color = 'lightblue'

            # Agregar el nodo al grafo
            x = columna * 20
            y = fila * 20
            graph.node(f'{fila},{columna}', width=20, height=20, color=color, pos=(x, y))

    # Eliminar las aristas
    graph.edges([])

    # Etiquetar los nodos con la letra del objetivo si corresponde
    for objetivo in maqueta['objetivos']:
        fila, columna = objetivo[1], objetivo[2]
        graph.node(f'{fila},{columna}', label=objetivo[0], pos=(columna * 20, fila * 20))

    # Etiquetar la entrada
    fila, columna = maqueta['entrada'][0], maqueta['entrada'][1]
    graph.node(f'{fila},{columna}', label='Entrada', color='green', pos=(columna * 20, fila * 20))

    # Cambiar el color de fondo
    graph.attr('bgcolor', '#f0f0f0')

    # Generar la imagen PNG
    graph.render('maqueta.png')

    # Mostrar la imagen en el canvas
    # ...

