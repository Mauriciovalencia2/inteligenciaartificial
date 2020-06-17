import queue

def Lab():
	lab =[["#","#", "O", "#", "#", "#", "#", "#", "#"],
	["#"," ", " ", " ", " ", " ", " ", " ", "#"],
	["#"," ", "#", "#", " ", "#", "#", " ", "#"],
	["#"," ", "#", " ", " ", " ", "#", " ", "#"],
	["#"," ", "#", "#", "#", " ", "#", " ", "#"],
	["#"," ", "#", " ", "#", " ", "#", " ", "#"],
	["#"," ", "#", " ", "#", " ", "#", "#", "#"],
	["#"," ", " ", " ", " ", " ", " ", " ", "#"],
	["#","#", "X", "#", "#", "#", "#", "#", "#"]]

	return lab

def printlaberinto(lab, path=""):
	for x, pos in enumerate(lab[0]):
		if pos == "O":
			start = x
	x = start
	y = 0
	pos = set()
	for mov in path:
		if mov == "I":
			x -= 1

		elif mov == "D":
			x += 1

		elif mov == "Abajo":
			y -= 1

		elif mov == "A":
			y += 1
		pos.add((y, x))

	for y, row in enumerate(lab):
		for x, col in enumerate(row):
			if (y, x) in pos:
				print("+ ", end="")
			else:
				print(col + " ", end="")
		print()
def valid(lab, movimientos):
	for x, pos in enumerate(lab[0]):
		if pos == "O":
			start = x
	x = start
	y = 0
	for mov in movimientos:
		if mov == "I":
			x -= 1

		elif mov == "D":
			x += 1

		elif mov == "Abajo":
			y -= 1

		elif mov == "A":
			y += 1

		if not(0 <= x < len(lab[0]) and 0 <= y < len(lab)):
			return False
		elif (lab[y][x] == "#"):
			return False
	return True
def findEnd(lab, movimientos):
	for x, pos in enumerate(lab[0]):
		if pos == "O":
			start = x
	x = start
	y = 0
	for mov in movimientos:
		if mov == "I":
			x -= 1
		elif mov == "D":
			x += 1
		elif mov == "Abajo":
			y -= 1
		elif mov == "A":
			y += 1
	if lab[y][x] == "X":
		print("Ruta a seguir " + movimientos+" ")
		printlaberinto(lab, movimientos)
		return True
	return False

x = queue.Queue()
x.put("")
add = ""
lab  = Lab()

while not findEnd(lab, add): 
	add = x.get()

	for j in ["I", "D", "Arriba", "Abajo"]:
		put = add + j
		if valid(lab, put):
			x.put(put)
