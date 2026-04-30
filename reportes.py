#Definimos la clase que se encargará de procesar toda la información
class AnalizadorEncuesta:
    # El constructor recibe la lista de objetos que creamos al leer el CSV
    def __init__(self, lista_objetos):
        
        self.encuestados = lista_objetos # Esta es la lista 'datos' del main

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

# ==============================================================================
# REPORTES 16 AL 20 - Eunice
# ==============================================================================

# Reporte 16. Comida con mejor satisfacción promedio.
    def comida_mejor_satisfaccion(self):
    
        datos_comidas = {}  # Diccionario para agrupar
    
        # Recorremos los objetos
        for p in self.encuestados:
        
            comida = p.comida_preferida
        
            # Promedio de satisfacción
            satisfaccion = (p.producto + p.servicio) / 2
        
        # Si no existe la comida
        if comida not in datos_comidas:
            datos_comidas[comida] = [0, 0]  # suma, cantidad
        
        # Acumulamos
        datos_comidas[comida][0] += satisfaccion
        datos_comidas[comida][1] += 1
    
        # Buscar mejor
        mejor_comida = ""
        mejor_promedio = 0
    
        for comida, valores in datos_comidas.items():
            suma = valores[0]
            cantidad = valores[1]
            promedio = suma / cantidad
        
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_comida = comida
    
        return mejor_comida