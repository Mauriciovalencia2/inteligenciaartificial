"""
Valencia Valencia Mauricio
16590524
Primero Anchura
"""
import json
JSONDATA = None
with open('base.json','r') as f:
	JSONDATA = json.load(f)
	
ini = input("Carteta donde empezara a buscar: ")
fin = input("Archivo a buscar: ")


camino=[]
 
fifo=[]
 
def buscar(inicio,valorBuscar,iteraciones):

    camino.append(inicio)
 
    if inicio==valorBuscar:
        return (True,iteraciones)
 
    fifoAdd(inicio)
 
    if len(fifo)==0:
        return (False,iteraciones)
 
    return buscar(fifo.pop(0),valorBuscar,iteraciones+1)
 
def fifoAdd(inicio):

    for k,v in JSONDATA['Base'].items():
        if v==inicio:
            fifo.append(k)
 
resultado,iteraciones=buscar(ini,fin,1)
if resultado:
    print("Ha encontrado el valor en {} iteraciones".format(iteraciones))
else:
    print("No se ha encontrado")
print("El camino que ha realizado ha sido: {}".format(camino))

