import csv

# Clase para guardar los datos de cada encuestado
class Encuestado:
    # Constructor de la clase (se ejecuta cuando creamos un objeto)
    def __init__(self, d):
        self.id = d["id"]
        self.comida_preferida = d["preferencias"]["comida_preferida"]
        self.frecuencia = d["preferencias"]["frecuencia"]
        self.gasto = d["consumo"]["gasto"]
        self.producto = d["experiencia"]["producto"]
        self.servicio = d["experiencia"]["servicio"]
        self.recomendacion = d["nps"]["recomendacion"]
        self.calificacion_general = d["nps"]["general"]
        self.precio = d["experiencia"]["precio"]
        self.tiempo_entrega = d["experiencia"]["tiempo de entrega"] 
        self.volveria = d["nps"]["volveria"]

# Función para transformar cada fila del CSV en un diccionario organizado
def recorrer_datos(fila):
    # Retornamos un diccionario con estructura ordenada
    return {
        # Convertimos el id a entero
        "id": int(fila["id"]),
        
        # Agrupamos datos de preferencias
        "preferencias": {
            "comida_preferida": fila["comida_preferida"],  # texto
            "frecuencia": fila["frecuencia_consumo"],      # texto
        },
        
        # Agrupamos datos de consumo
        "consumo": {
            "gasto": float(fila["gasto_promedio"])  # convertimos a decimal
        },
        
        # Agrupamos datos de experiencia
        "experiencia": {
            "producto": int(fila["satisfaccion_producto"]),  # entero
            "servicio": int(fila["satisfaccion_servicio"]),  # entero
            "tiempo de entrega": fila["tiempo_entrega"],     # texto
            "precio": fila["precio_percepcion"],             # texto
        },
        
        # Agrupamos datos de NPS
        "nps": {
            "recomendacion": int(fila["recomendaria_nps"]),  # entero
            
            # Convertimos "Sí"/"No" a True o False
            "volveria": fila["volveria_comprar"].strip().lower() in ["sí", "si"],
            
            "general": int(fila["calificacion_general"]) # entero
        }
    }

# Función para leer el archivo CSV
def leer_datos(nombre_archivo):
    # Uso de listas para almacenar los 20,000 registros.
    lista_encuestados = []
    
    try:
        # Abrimos el archivo en modo lectura con codificación latin-1
        with open(nombre_archivo, mode='r', encoding='latin-1') as archivo:
            
            # DictReader convierte cada fila en un diccionario automáticamente
            lector = csv.DictReader(archivo)

            # Recorremos cada fila del archivo
            for fila in lector:

                # Transformamos la fila en un diccionario estructurado
                registro = recorrer_datos(fila)

                # Creamos un objeto de tipo Encuestado usando ese diccionario
                encuestado = Encuestado(registro)

                # Guardamos el objeto en la lista
                lista_encuestados.append(encuestado)

    # Si el archivo no existe, mostramos un error
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    
    # Retornamos la lista de encuestados ya procesada
    return lista_encuestados