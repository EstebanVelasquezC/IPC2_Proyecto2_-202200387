from parser_xml import ParserXML
from maqueta import Maqueta

def encontrar_camino(maqueta):
    estructura = maqueta.obtener_estructura()
    entrada = maqueta.entrada
    objetivos = maqueta.objetivos

    camino = []
    fila_actual, columna_actual = entrada
    for objetivo in objetivos:
        nombre_objetivo, fila_objetivo, columna_objetivo = objetivo
        # Algoritmo para encontrar el camino al próximo objetivo
        # (Puedes implementar este algoritmo aquí)

        # Agregamos el camino al objetivo actual al camino total
        camino.append((nombre_objetivo, fila_objetivo, columna_objetivo))

    return camino

def main():
    nombre_archivo = 'entrada.xml'
    maquetas_xml = ParserXML.cargar_maquetas(nombre_archivo)
    
    maquetas = []
    for maqueta_xml in maquetas_xml:
        maqueta = Maqueta(maqueta_xml['nombre'], maqueta_xml['filas'], maqueta_xml['columnas'],
                          maqueta_xml['entrada'], maqueta_xml['objetivos'], maqueta_xml['estructura'])
        maquetas.append(maqueta)
    
    for maqueta in maquetas:
        print(maqueta)
        print("Estructura:")
        for fila in maqueta.obtener_estructura():
            print(''.join(fila))
        print()
    
    for maqueta in maquetas:
        print(f"Camino para la maqueta {maqueta.nombre}:")
        camino = encontrar_camino(maqueta)
        print(camino)
        print()

if __name__ == "__main__":
    main()
