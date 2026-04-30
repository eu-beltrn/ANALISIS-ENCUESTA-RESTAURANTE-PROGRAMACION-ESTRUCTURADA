#Definimos la clase que se encargará de procesar toda la información
class AnalizadorEncuesta:
    # El constructor recibe la lista de objetos que creamos al leer el CSV
    def __init__(self, lista_objetos):
        
        self.encuestados = lista_objetos # Esta es la lista 'datos' del main

    def _contar_elementos(self, lista):
        """Recibe cualquier lista y devuelve un diccionario con el conteo."""
        conteo = {}
        for item in lista:
            conteo[item] = conteo.get(item, 0) + 1
        return conteo

    def _calcular_nps(self, lista_calificaciones):
        """Recibe una lista de lista_calificaciones (0-10) y aplica la fórmula NPS."""
        if not lista_calificaciones: return 0
        # suma y cuenta las calificaciones
        promotores = sum(1 for n in lista_calificaciones if n >= 9)
        detractores = sum(1 for n in lista_calificaciones if n <= 6)
        return ((promotores - detractores) / len(lista_calificaciones)) * 100
# ==============================================================================
# REPORTES 1 AL 5 - Karla
# ==============================================================================

# ==============================================================================
# REPORTES 6 AL 10 - Nicole
# ==============================================================================
    def reporte_6(self):
        acum, cont = {}, {}
        for e in self.encuestados:
            acum[e.comida_preferida] = acum.get(e.comida_preferida, 0) + e.gasto
            cont[e.comida_preferida] = cont.get(e.comida_preferida, 0) + 1
        return {c: acum[c] / cont[c] for c in acum}

    def reporte_7(self):
        return sum(e.producto for e in self.encuestados) / len(self.encuestados)

    def reporte_8(self):
        return sum(e.servicio for e in self.encuestados) / len(self.encuestados)

    def reporte_9(self):
        # Ahora usamos el atributo del objeto
        return sum(e.calificacion_general for e in self.encuestados) / len(self.encuestados)

    def reporte_10(self):
        conteo = {}
        for e in self.encuestados:
            conteo[e.precio] = conteo.get(e.precio, 0) + 1
        return conteo
# ==============================================================================
# REPORTES 11 AL 15 - Jonathan
# ==============================================================================
# Reporte 11. Distribución de tiempo de entrega.
    def distribucion_tiempo_entrega(self):
        """11. Distribución de tiempo de entrega"""
        # Extraemos solo los tiempos en una lista y se los pasamos a _contar_elementos
        tiempos = [e.tiempo_entrega for e in self.encuestados]
        return self._contar_elementos(tiempos)

    # Reporte 12. Porcentaje de clientes que volverían a comprar. 
    def porcentaje_volverian_comprar(self):
        """12. Porcentaje de clientes que volverían a comprar"""
        if not self.encuestados: return 0
        # Sumamos 1 solo si e.volveria es verdadero
        votos_si = sum(1 for e in self.encuestados if e.volveria)
        return (votos_si / len(self.encuestados)) * 100

    # Reporte 13. Cálculo del NPS general. 
    def calculo_nps_general(self):
        """13. Cálculo del NPS general"""
        # Extraemos todas las calificaciones de recomendación y se las pasamos a _calcular_nps
        calificaciones = [e.recomendacion for e in self.encuestados]
        return self._calcular_nps(calificaciones)

    # Reporte 14. Cantidad de promotores, pasivos y detractores. 
    def conteo_promotores_pasivos_detractores(self):
        """14. Cantidad de promotores, pasivos y detractores"""
        calificaciones = [e.recomendacion for e in self.encuestados]
        return {
            "Promotores": sum(1 for n in calificaciones if n >= 9),
            "Pasivos": sum(1 for n in calificaciones if 7 <= n <= 8),
            "Detractores": sum(1 for n in calificaciones if n <= 6)
        }

    # Reporte 15. NPS por tipo de comida. 
    def nps_por_tipo_comida(self):
        """15. NPS por tipo de comida"""
        # 1. Agrupamos las calificaciones de recomendación separadas por comida
        grupos = {}
        for e in self.encuestados:
            # .setdefault() crea la lista si no existe, y luego agrega la calificacion
            grupos.setdefault(e.comida_preferida, []).append(e.recomendacion)
            
        # 2. Reutilizamos _calcular_nps para calcular el NPS para cada grupo
        nps_comidas = {}
        for comida, calificaciones in grupos.items():
            nps_comidas[comida] = self._calcular_nps(calificaciones)
            
        return nps_comidas

# ==============================================================================
# REPORTES 16 AL 20 - Eunice
# ==============================================================================
