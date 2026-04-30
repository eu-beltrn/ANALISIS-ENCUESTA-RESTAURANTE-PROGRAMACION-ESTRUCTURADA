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


# REPORTES 11 AL 15 - Jonathan¿
print("\n" + "="*70)
print("REPORTES 11-15 (Jonathan)".center(70,"-"))
print("="*70)

# Reporte 11. Distribución de tiempo de entrega.
print(f"\n11. Distribución de tiempo de entrega:")
for tiempo, total in analizador.distribucion_tiempo_entrega().items():
    print(f"   - {tiempo}: {total} encuestados")

# Reporte 12. Porcentaje de clientes que volverían a comprar. 
print(f"\n12. Porcentaje de clientes que volverían a comprar: {analizador.porcentaje_volverian_comprar():.2f}%")

# Reporte 13. Cálculo del NPS general. 
print(f"\n13. Cálculo del NPS general: {analizador.calculo_nps_general():.2f}")

# Reporte 14. Cantidad de promotores, pasivos y detractores. 
print(f"\n14. Cantidad de promotores, pasivos y detractores:")
for segmento, cantidad in analizador.conteo_promotores_pasivos_detractores().items():
    print(f"   - {segmento}: {cantidad} clientes")

# Reporte 15. NPS por tipo de comida. 
print(f"\n15. NPS por tipo de comida:")
for comida, nps in analizador.nps_por_tipo_comida().items():
    print(f"   - {comida}: {nps:.2f} NPS")