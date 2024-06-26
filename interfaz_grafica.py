import tkinter as tk
from tkinter import filedialog
import webbrowser
import graphviz
from xml_parser import cargar_archivo_xml

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto de Mecatrónica")
        self.geometry("800x700")
        self.config(bg="#2c3e50")  # Color de fondo
        self.maquetas_cargadas = []  # Lista para almacenar las maquetas
        
        self.cargar_archivo_btn = tk.Button(self, text="Cargar archivo XML", command=self.cargar_archivo, bg="#34495e", fg="white")
        self.cargar_archivo_btn.config(font=("Arial", 14))
        self.cargar_archivo_btn.pack(pady=10)
        
        self.gestion_maquetas_btn = tk.Button(self, text="Gestión de maquetas", command=self.mostrar_maquetas, bg="#34495e", fg="white")
        self.gestion_maquetas_btn.config(font=("Arial", 14))
        self.gestion_maquetas_btn.pack(pady=10)
        
        self.resolucion_maquetas_btn = tk.Button(self, text="Resolución de maquetas", command=self.resolucion_maquetas, bg="#34495e", fg="white")
        self.resolucion_maquetas_btn.config(font=("Arial", 14))
        self.resolucion_maquetas_btn.pack(pady=10)
        
        self.ayuda_btn = tk.Button(self, text="Ayuda", command=self.mostrar_ayuda, bg="#34495e", fg="white")
        self.ayuda_btn.config(font=("Arial", 14))
        self.ayuda_btn.pack(pady=10)
        
        self.reiniciar_btn = tk.Button(self, text="Reiniciar", command=self.reset, bg="#e74c3c", fg="white")
        self.reiniciar_btn.config(font=("Arial", 14))
        self.reiniciar_btn.pack(pady=10)
        
    def cargar_archivo(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
        if filename:
            self.maquetas_cargadas = cargar_archivo_xml(filename)
            if self.maquetas_cargadas:
                print("Maquetas cargadas correctamente:")
                for maqueta in self.maquetas_cargadas:
                    print(maqueta)
    
    def mostrar_maquetas(self):
        # Verifica si hay maquetas cargadas
        if self.maquetas_cargadas:
            # Itera sobre las maquetas cargadas
            for maqueta in self.maquetas_cargadas:
                # Muestra el nombre de cada maqueta
                print(f"Nombre de la maqueta: {maqueta['nombre']}")
                # Muestra otros detalles de la maqueta, como las filas, columnas, entrada y objetivos
                print(f"Filas: {maqueta['columnas']}")  # Cambiar 'columnas' por 'filas'
                print(f"Columnas: {maqueta['filas']}")  # Cambiar 'filas' por 'columnas'
                print(f"Entrada: {maqueta['entrada']}")
                print("Objetivos:")
                for objetivo in maqueta['objetivos']:
                    print(f"- Nombre: {objetivo[0]}, Fila: {objetivo[1]}, Columna: {objetivo[2]}")
                # Muestra la estructura de la maqueta
                print("Estructura:")
                print(maqueta['estructura'])
                print("=" * 30)
                # Mostrar representación gráfica de la maqueta
                self.mostrar_maqueta(maqueta)
        else:
            print("No se han cargado maquetas")
    
    def mostrar_maqueta(self, maqueta):
        # Generar la representación en lenguaje DOT de la maqueta
        dot = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
        for i in range(maqueta['columnas']):  # Cambiar 'columnas' por 'filas'
            with dot.subgraph() as s:
                s.attr(rank='same')
                for j in range(maqueta['filas']):  # Cambiar 'filas' por 'columnas'
                    node_id = f"{i}_{j}"
                    if maqueta['estructura'][j * maqueta['columnas'] + i] == '*':  # Intercambiar 'i' y 'j'
                        s.node(node_id, style="filled", fillcolor="black", shape="rectangle", width="0.3", height="0.3", fontsize="10")
                    else:
                        s.node(node_id, style="filled", fillcolor="white", shape="rectangle", width="0.3", height="0.3", fontsize="10")
                    if j > 0:
                        dot.edge(f"{i}_{j - 1}", node_id, style="invis")
                    if i > 0 and maqueta['estructura'][j * maqueta['columnas'] + (i - 1)] != '*':  # Intercambiar 'i' y 'j'
                        dot.edge(f"{i - 1}_{j}", node_id, style="invis")
                    for objetivo in maqueta['objetivos']:
                        if objetivo[1] == j and objetivo[2] == i:  # Intercambiar 'objetivo[1]' y 'objetivo[2]'
                            dot.node(node_id, label=objetivo[0], shape="rectangle", color="blue", fontsize="10", style="filled", fillcolor="blue")
        dot.node("entrada", style="filled", fillcolor="#98FB98", shape="rectangle", width="0.3", height="0.3", fontsize="10")
        dot.edge("entrada", f"{maqueta['entrada'][1]}_{maqueta['entrada'][0]}", color="green")  # Intercambiar 'entrada[0]' y 'entrada[1]'
        # Mostrar la maqueta
        dot.render('maqueta', format='png', view=True)
    
    def resolucion_maquetas(self):
        # Lógica para resolver las maquetas
        print("Resolución de maquetas")
    
    def mostrar_ayuda(self):
        ayuda_window = tk.Toplevel(self)
        ayuda_window.title("Ayuda")
        ayuda_window.geometry("400x200")
        ayuda_window.config(bg="#f0f0f0")  # Color de fondo
        
        texto_ayuda = tk.Label(ayuda_window, text="Rogelio Esteban Velasquez Castillo\n202200387", font=("Arial", 16), bg="#f0f0f0")
        texto_ayuda.pack(pady=20)
        
        enlace_label = tk.Label(ayuda_window, text="Documentación", fg="blue", cursor="hand2", font=("Arial", 14, "underline"), bg="#f0f0f0")
        enlace_label.pack(pady=5)
        enlace_label.bind("<Button-1>", lambda event: self.abrir_enlace("https://www.example.com"))
    
    def abrir_enlace(self, url):
        webbrowser.open_new(url)
    
    def reset(self):
        # Lógica para limpiar los datos y restablecer la interfaz
        print("Reiniciando la aplicación")

if __name__ == "__main__":
    app = InterfazGrafica()
    app.mainloop()
