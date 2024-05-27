def tabla_de_multiplicar(numero):
    if 1 <= numero <= 10:
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero}x{i}={resultado}")
    else:
        print("Por favor, ingrese un número entre 1 y 10.")
numero = 7
tabla_de_multiplicar(numero)
