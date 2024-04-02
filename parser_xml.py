import xml.etree.ElementTree as ET

class ParserXML:
    @staticmethod
    def cargar_maquetas(nombre_archivo):
        maquetas = []
        try:
            tree = ET.parse(nombre_archivo)
            root = tree.getroot()

            for maqueta_xml in root.findall('maqueta'):
                nombre = maqueta_xml.find('nombre').text
                filas = int(maqueta_xml.find('filas').text)
                columnas = int(maqueta_xml.find('columnas').text)

                entrada_xml = maqueta_xml.find('entrada')
                fila_entrada = int(entrada_xml.find('fila').text)
                columna_entrada = int(entrada_xml.find('columna').text)

                objetivos = []
                for objetivo_xml in maqueta_xml.find('objetivos').findall('objetivo'):
                    nombre_objetivo = objetivo_xml.find('nombre').text
                    fila_objetivo = int(objetivo_xml.find('fila').text)
                    columna_objetivo = int(objetivo_xml.find('columna').text)
                    objetivos.append((nombre_objetivo, fila_objetivo, columna_objetivo))

                estructura = maqueta_xml.find('estructura').text.strip()

                maqueta = {
                    'nombre': nombre,
                    'filas': filas,
                    'columnas': columnas,
                    'entrada': (fila_entrada, columna_entrada),
                    'objetivos': objetivos,
                    'estructura': estructura
                }
                maquetas.append(maqueta)
                
        except FileNotFoundError:
            print("El archivo XML especificado no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo XML: {e}")

        return maquetas

