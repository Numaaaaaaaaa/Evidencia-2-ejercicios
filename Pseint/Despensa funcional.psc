Proceso DespensaJubilados
    Definir unidadesDeLeche como entero
    Definir esJubilado como logico
    Definir montoParcial, montoAPagar como real
	
    Escribir "Ingrese la cantidad de unidades de leche compradas:"
    Leer unidadesDeLeche
	
    Escribir "¿Es usted jubilado? (Sí/No):"
    Leer respuesta
    Si respuesta == "Sí" Entonces
        esJubilado = Verdadero
    Sino
        esJubilado = Falso
    FinSi
	
    montoParcial = unidadesDeLeche * 1000
	
    Si unidadesDeLeche > 24 Entonces
        Si esJubilado Entonces
            montoAPagar = montoParcial * 0.75
        Sino
            montoAPagar = montoParcial * 0.85
        FinSi
    Sino
        Si unidadesDeLeche > 12 Entonces
            Si esJubilado Entonces
                montoAPagar = montoParcial * 0.80
            Sino
                montoAPagar = montoParcial * 0.90
            FinSi
        Sino
            Si esJubilado Entonces
                montoAPagar = montoParcial * 0.90
            Sino
                montoAPagar = montoParcial
            FinSi
        FinSi
    FinSi
	
    Escribir "El total a pagar es:", montoAPagar
FinProceso
