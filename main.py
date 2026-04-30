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
print("REPORTES 1 - 5 (Karla)".center(70,"-"))
print("="*70)


# ==============================================================================
# REPORTES 6 AL 10 - Nicole
# ==============================================================================
print("\n" + "="*70)
print("REPORTES 6 - 10 (Nicole)".center(70,"-"))
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
print("REPORTES 11-15 (Jonathan)".center(70,"-"))
print("="*70)

# Reporte 11
print(f"\n11. Distribución de tiempo de entrega:")
for tiempo, total in analizador.distribucion_tiempo_entrega().items():
    print(f"   - {tiempo}: {total} encuestados")

# Reporte 12
print(f"\n12. Porcentaje de clientes que volverían a comprar: {analizador.porcentaje_volverian_comprar():.2f}%")

# Reporte 13
print(f"\n13. Cálculo del NPS general: {analizador.calculo_nps_general():.2f}")

# Reporte 14
print(f"\n14. Cantidad de promotores, pasivos y detractores:")
for segmento, cantidad in analizador.conteo_promotores_pasivos_detractores().items():
    print(f"   - {segmento}: {cantidad} clientes")

# Reporte 15
print(f"\n15. NPS por tipo de comida:")
for comida, nps in analizador.nps_por_tipo_comida().items():
    print(f"   - {comida}: {nps:.2f} NPS")


# ============================================================================== 
# REPORTES 16 AL 20 - Eunice
# ==============================================================================
print("\n" + "="*70)
print("REPORTES 16 - 20 (Eunice)".center(70,"-"))
print("="*70)

# Reporte 16. Comida con mejor satisfacción promedio
print("\n16. Comida con mejor satisfacción promedio")
print(analizador.comida_mejor_satisfaccion())

# Reporte 17. Comida con menor satisfacción promedio.
print("\n17. Comida con menor satisfacción promedio")
print(analizador.comida_menor_satisfaccion())

# Reporte 18. Relación entre precio percibido y recomendación.
print("\n18. Relación entre precio y recomendación")
for precio, promedio in analizador.relacion_precio_recomendacion().items():
    print(f"   - {precio}: {promedio:.2f}")

# Reporte 19. Relación entre tiempo de entrega y satisfacción.
print("\n19. Relación entre tiempo de entrega y satisfacción")
for tiempo, promedio in analizador.relacion_tiempo_satisfaccion().items():
    print(f"   - {tiempo}: {promedio:.2f}")

# Reporte 20. Perfil predominante del consumidor.
print("\n20. Perfil predominante del consumidor")
perfil = analizador.perfil_predominante()
for clave, valor in perfil.items():
    print(f"   - {clave}: {valor}")