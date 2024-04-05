import xml.etree.ElementTree as ET

def cargar_archivo_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        maquetas = []

        for maqueta_elem in root.findall('./maquetas/maqueta'):
            nombre = maqueta_elem.find('nombre').text
            filas = int(maqueta_elem.find('filas').text)
            columnas = int(maqueta_elem.find('columnas').text)
            entrada_elem = maqueta_elem.find('entrada')
            entrada_fila = int(entrada_elem.find('fila').text)
            entrada_columna = int(entrada_elem.find('columna').text)

            objetivos = []
            for objetivo_elem in maqueta_elem.findall('objetivos/objetivo'):
                objetivo_nombre = objetivo_elem.find('nombre').text
                objetivo_fila = int(objetivo_elem.find('fila').text)
                objetivo_columna = int(objetivo_elem.find('columna').text)
                objetivos.append((objetivo_nombre, objetivo_fila, objetivo_columna))

            estructura = maqueta_elem.find('estructura').text.strip()

            maqueta = {
                'nombre': nombre,
                'filas': filas,
                'columnas': columnas,
                'entrada': (entrada_fila, entrada_columna),
                'objetivos': objetivos,
                'estructura': estructura
            }

            maquetas.append(maqueta)

        return maquetas

    except Exception as e:
        print("Error al cargar el archivo XML:", e)
        return None

