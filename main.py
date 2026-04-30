from lectura_datos import *
from reportes import *

# 1. Cargar datos al inicio
ruta = "prueba.csv"
datos = leer_datos(ruta)

#print(len(datos))

analizador = AnalizadorEncuesta(datos) # 'datos' contiene lo que leyó leer_datos[cite: 3]

# ==============================================================================
# REPORTES 1 AL 5 - Karla
# ==============================================================================
print("\n" + "="*70)
print("REPORTES 1 - 5".center(70,"-"))
print("="*70)


# ==============================================================================
# REPORTES 6 AL 10 - Nicole
# ==============================================================================
print("\n" + "="*70)
print("REPORTES 6 - 10".center(70,"-"))
print("="*70)

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

# ==============================================================================
# REPORTES 11 AL 15 - Jonathan
# ==============================================================================
print("\n" + "="*70)
print("REPORTES 11 - 15".center(70,"-"))
print("="*70)


# ==============================================================================
# REPORTES 16 AL 20 - Eunice
# ==============================================================================
print("\n" + "="*70)
print("REPORTES 16 - 20".center(70,"-"))
print("="*70)

# Reporte 16. Comida con mejor satisfacción promedio.
print("\n16. Comida con mejor satisfacción promedio")
print(analizador.comida_mejor_satisfaccion())