import csv

#Clase para guardar los datos de encuestado
class Encuestado:
    #Creación del constructor
    def __init__(self, d):
        self.id = d["id"]
        self.comida_preferida = d["preferencias"]["comida_preferida"]
        self.frecuencia = d["preferencias"]["frecuencia"]
        self.gasto = d["consumo"]["gasto"]
        self.producto = d["experiencia"]["producto"]
        self.servicio = d["experiencia"]["servicio"]
        self.recomendacion = d["nps"]["recomendacion"]

#Función para transformar filas en diccionarios anidados
def recorrer_datos(fila):
        #Retornamos el diccionario
        return {
            "id": int(fila["id"]),
            "preferencias": {
                "comida_preferida": fila["comida_preferida"],
                "frecuencia": fila["frecuencia_consumo"],
            },
            "consumo":{
                "gasto": float(fila["gasto_promedio"])
            },
            "experiencia": {
                "producto": int(fila["satisfaccion_producto"]),
                "servicio": int(fila["satisfaccion_servicio"]),
                "tiempo de entrega": fila["tiempo_entrega"],
                "precio": fila["precio_percepcion"],
            },
            "nps": {
                "recomendacion": int(fila["recomendaria_nps"]),
                "volveria": fila["volveria_comprar"].strip().lower() in ["sí", "si"],
                "general": int(fila["calificacion_general"])
            }
        }

#Funcion para leer el archivo CSV
def leer_datos(nombre_archivo):
    lista_encuestados = []
    try:
        with open(nombre_archivo, mode='r', encoding='latin-1') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:

                registro = recorrer_datos(fila)

                encuestado = Encuestado(registro)

                lista_encuestados.append(encuestado)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    return lista_encuestados
