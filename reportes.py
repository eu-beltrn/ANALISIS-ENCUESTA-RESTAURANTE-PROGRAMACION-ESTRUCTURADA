# ==============================================================================
# REPORTES 1 AL 5 - Karla
# ==============================================================================

# ==============================================================================
# REPORTES 6 AL 10 - Nicole
# ==============================================================================
#Definimos la clase que se encargará de procesar toda la información
class AnalizadorEncuesta:
    # El constructor recibe la lista de objetos que creamos al leer el CSV
    def __init__(self, lista_objetos):
        
        self.encuestados = lista_objetos # Esta es la lista 'datos' del main

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

# ==============================================================================
# REPORTES 16 AL 20 - Eunice
# ==============================================================================
