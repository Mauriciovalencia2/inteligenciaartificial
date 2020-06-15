"""
Valencia Valencia Mauricio
16590524
Primero Profundidad
"""
import json
JSONDATA = None
with open('base.json','r') as f:
	JSONDATA = json.load(f)

ini = input("Carteta donde empezara a buscar: ")
fin = input("Archivo a buscar: ")

camino=[]
 
def buscar(inicio,valorBuscar):

    camino.append(inicio)
 
    if inicio==valorBuscar:
        return valorBuscar
 
    for k,v in JSONDATA['Base'].items():
 
        if v==inicio:
 
            result=buscar(k,valorBuscar)
 
            if result:
                return result
 
    camino.pop()

    return 0
 
result=buscar(ini,fin)

if result:
    print(camino)
else:
    print("Ruta NO encontrada")
