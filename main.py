from lectura_datos import *
from reportes import *

# 1. Cargar datos al inicio
ruta = "prueba.csv"
datos = leer_datos(ruta)

#print(len(datos))



#Reportes 6-10
analizador = AnalizadorEncuesta(datos) # 'datos' contiene lo que leyó leer_datos[cite: 3]

print("6. Promedio de gasto por comida:")
for comida, promedio in analizador.reporte_6().items():
    print(f"   - {comida}: ${promedio:.2f}")

# Reportes 7 
print(f"7. Satisfacción promedio producto: {analizador.reporte_7():.2f}")

#Reporte 8
print(f"8. Satisfacción promedio servicio: {analizador.reporte_8():.2f}")

# Reporte 9 
print(f"9. Calificación general promedio: {analizador.reporte_9():.2f}")

# Reporte 10 
print("10. Distribución de percepción de precios:")
for nivel, total in analizador.reporte_10().items():
    print(f"   - {nivel}: {total} encuestados")