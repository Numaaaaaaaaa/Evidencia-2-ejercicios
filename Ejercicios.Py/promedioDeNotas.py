def calcular_promedio(notas):
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio
if __name__ == "__main__":
    notas = [85.0, 90.5, 78.0, 92.0, 88.5]
    
    promedio = calcular_promedio(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")