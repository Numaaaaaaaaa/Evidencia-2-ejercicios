def calcular_puntos(partidos_ganados, partidos_empatados, partidos_perdidos):
    puntos_totales = (partidos_ganados * 3) + (partidos_empatados * 1)
    return puntos_totales

if __name__ == "__main__":
    
    partidos_ganados = 7
    partidos_empatados = 4
    partidos_perdidos = 3
    
    puntos_totales = calcular_puntos(partidos_ganados, partidos_empatados, partidos_perdidos)
    print(f"La cantidad total de puntos acumulados es: {puntos_totales}")
