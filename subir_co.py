"""

"""
import math
 
# Cada elemento de este diccionario contiene una posicion del camino, y como 
# valor tiene una lista con el calculo del camino mas corto, y el origen del
# mismo
valores={
    "A":[math.inf,""],
    "B":[math.inf,""],
    "C":[math.inf,""],
    "D":[math.inf,""],
    "E":[math.inf,""],
    "F":[math.inf,""],
    "G":[math.inf,""],
    "H":[math.inf,""],
    "I":[math.inf,""],
    "R":[math.inf,""],
    "S":[math.inf,""],
    "T":[math.inf,""],
    "U":[math.inf,""],
    "V":[math.inf,""],
    "W":[math.inf,""],
    "X":[math.inf,""],
    "Y":[math.inf,""],
    "Z":[math.inf,""]
}
 
# aquí establecemos cada uno de los caminos en una sola dirección y el coste
# que tiene cada camino
caminos=[
	["A","B",1],
	["B","A",1],
	["A","Z",2],
	["Z","A",2],
	["Z","X",2],
	["X","Z",2],
	["X","Y",2],
	["Y","X",2],
	["Y","W",1],
	["W","Y",1],
	["W","R",1],
	["R","W",1],
	["R","T",2],
	["T","R",2],
	["T","Z",3],
	["Z","T",3],
	["W","U",2],
	["U","W",2],
	["U","V",3],
	["V","U",3],
	["V","H",3],
	["H","V",3],
	["H","I",1],
	["I","H",1],
	["G","H",2],
	["H","G",2],
	["S","G",3],
	["G","S",3],
	["S","V",2],
	["V","S",2],
	["R","S",1],
	["S","R",1],
	["S","E",4],
	["E","S",4],
	["F","E",2],
	["E","F",2],
	["G","F",3],
	["F","G",3],
	["E","D",1],
	["D","E",1],
	["C","D",2],
	["D","C",2],
	["C","B",1],
	["B","C",1],
	["D","B",2],
	["B","D",2]
]
 
def setValores(origen,destino,valor):

    if valor<valores[destino][0]:
 
        valores[destino][0]=valor
 
        valores[destino][1]=origen
        return True
    return False
 

inicio="Z"
final="I"
 
valores[inicio][0]=0
 

while True:
    cancel=True
 

    for i in caminos:
 

        if setValores(i[0],i[1],valores[i[0]][0]+i[2]):
            cancel=False

        if setValores(i[1],i[0],valores[i[1]][0]+i[2]):
            cancel=False
 
    if cancel:
        break
 
camino=[final]
 
while True:
    if camino[-1]==inicio:
        break
    camino.append(valores[camino[-1]][1])
 
print("El camino mas corto desde el punto '{}' y el punto '{}' es: {}".format(inicio, final, camino[::-1]))
