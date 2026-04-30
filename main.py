from lectura_datos import *
from reportes import *

# 1. Cargar datos al inicio
ruta = "prueba.csv"
datos = leer_datos(ruta)

print(len(datos))