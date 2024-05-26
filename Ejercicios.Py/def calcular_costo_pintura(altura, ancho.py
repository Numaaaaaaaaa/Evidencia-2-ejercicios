def calcular_costo_pintura(altura, ancho, costo_por_m2):
    area = altura * ancho
    costo_total = area * costo_por_m2
    return costo_total

if __name__ == "__main__":
    # Datos específicos
    altura = 5
    ancho = 17
    costo_por_m2 = 50.0
    
    costo_total = calcular_costo_pintura(altura, ancho, costo_por_m2)
    print(f"El costo total de la mano de obra para pintar la pared es: ${costo_total:.2f}")
