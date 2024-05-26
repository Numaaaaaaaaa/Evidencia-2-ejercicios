# Ejercicio 1
nombres = []
for i in range(10):
    nombre = input("Ingrese un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("¡Nombre repetido! Intente de nuevo.")
        i -= 1

print("Lista de nombres ingresados:")
print(nombres)

# Ejercicio 2
if len(nombres) >= 3:
    del nombres[2]  
if nombres:
    del nombres[-1]  

nombres.sort()
print("Lista de nombres ordenados después de eliminar el tercer y último elemento:")
print(nombres)

# Ejercicio 3
persona = {}
persona["nombre"] = input("Ingrese su nombre: ")
persona["apellido"] = input("Ingrese su apellido: ")
persona["dni"] = input("Ingrese su DNI: ")
persona["email"] = input("Ingrese su email: ")
persona["fecha_nacimiento"] = input("Ingrese su fecha de nacimiento: ")

print("Datos de la persona guardados en el diccionario:")
print(persona)

# Ejercicio 4
familia = {}
for i in range(4):
    persona = {}
    persona["nombre"] = input("Ingrese nombre de la persona: ")
    persona["apellido"] = input("Ingrese apellido de la persona: ")
    persona["dni"] = input("Ingrese DNI de la persona: ")
    persona["email"] = input("Ingrese email de la persona: ")
    persona["fecha_nacimiento"] = input("Ingrese fecha de nacimiento de la persona: ")
    familia[f"persona_{i+1}"] = persona

print("Datos de la familia guardados en el diccionario:")
print(familia)

# Ejercicio 5
n = int(input("Ingrese la cantidad de números pares que desea: "))
numeros_pares = tuple(i for i in range(2, 2*n+1, 2))

print("Los primeros", n, "números pares son:")
print(numeros_pares)
