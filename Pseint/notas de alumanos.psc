Algoritmo CalcularRendimiento
    Definir num_estudiantes, suma Como Entero
    Definir promedio, nota Como Real
    suma <- 0
    
    Escribir "Ingrese el número de estudiantes: "
    Leer num_estudiantes
    
    Para i = 1 Hasta num_estudiantes Hacer
        Escribir "Ingrese la nota del estudiante ", i, ": "
        Leer nota
        suma <- suma + nota
    FinPara
    
    promedio <- suma / num_estudiantes
    
    Si promedio > 8 Entonces
        Escribir "Rendimiento elevado"
    Sino
        Si promedio >= 6 Entonces
            Escribir "Rendimiento aceptable"
        Sino
            Escribir "Rendimiento bajo"
        FinSi
    FinSi
FinAlgoritmo
