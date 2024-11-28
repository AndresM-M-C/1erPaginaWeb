Algoritmo sin_titulo
		Definir n, i, j Como Entero
		Escribir "Ingrese la altura del triángulo invertido: "
		Leer n
		i <- n
		Mientras i >= 1 Hacer
			j <- 1
			Mientras j <= i Hacer
				Si j = 1 O j = i O i = n Entonces
					Escribir Sin Saltar '*'
				SiNo
					Escribir Sin Saltar ' '
				FinSi
				j <- j + 1
			Fin Mientras
			Escribir ""
			i <- i - 1
		Fin Mientras
FinAlgoritmo
