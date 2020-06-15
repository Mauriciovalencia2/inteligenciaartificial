global N 
N = 4 ## N es igual a 4 reinas

##imprimir el talero de la matriz con la solucion
def imprimeSolucion(Tablero): 
	for i in range(N): 
		for j in range(N): 
			print (Tablero[i][j], end = ' ') 
		print()

##Funcion de utilidad para verificar si una reina se puede colocar
def seguridad(Tablero, fila, columna): 

##verifica la fila en el lado izquierdo
	for i in range(columna): 
		if Tablero[fila][i] == 1: 
			return False
##verifica la diagonal superior en el lado izquierdo
	for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)): 
		if Tablero[i][j] == 1: 
			return False
##verifica la diagonal inferior en el lado izquierdo
	for i, j in zip(range(fila, N, 1), range(columna, -1, -1)): 
		if Tablero[i][j] == 1: 
			return False
	return True


def resolverNreinas(Tablero, columna): 
##si todas las reinas han sido colocadas devuelve verdadero
	if columna >= N: 
		return True
# Considera esta columna e intenta colocar esta reina en todas las filas una por una
	for i in range(N): 

		if seguridad(Tablero, i, columna): 
#Coloca a esta reina en el tablero [i][columna]
			Tablero[i][columna] = 1
#recurrir a colocar el resto de las reinas
			if resolverNreinas(Tablero, columna + 1) == True: 
				return True
# Si coloca a la reina en el tablero [i] [columna] no conduce a una solución, entonces reina del tablero [i] [columna]
			Tablero[i][columna] = 0
			
# si la reina no se puede colocar en ninguna fila en esta columna columna luego devuelve falso
	return False

# Esta función resuelve el problema de N Queen usando
# Retroceso. Utiliza principalmente solveNQUtil () para
# resolver el problema. Devuelve falso si las reinas
# no se puede colocar, de lo contrario devuelve verdadero y
# colocación de reinas en forma de 1s.
# tenga en cuenta que puede haber más de uno
# soluciones, esta función imprime uno de los
# soluciones viables.
def resuelveNQ(): 
	Tablero = [ [0, 0, 0, 0], 
				[0, 0, 0, 0], 
				[0, 0, 0, 0], 
				[0, 0, 0, 0] 
			] 

	if resolverNreinas(Tablero, 0) == False: 
		print ("La solucion no existe")
		return False

	imprimeSolucion(Tablero) 
	return True

resuelveNQ() 
