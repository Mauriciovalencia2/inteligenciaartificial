import copy

t = [ [ 1, 0, 1], 
	  [ 0, 0, 0], 
	  [ 2, 0, 2] 
		] 
for i in range(3):
	for j in range (3):
		print(t[i][j], end= ' ')
	print()	
print()

k = copy.deepcopy(t)

for a in range(4):
		
	if t[0][0] != 0:
		k[1][2]=copy.deepcopy(t[0][0])
		k[0][0]=copy.deepcopy(t[1][2])
		
	if t[0][1] != 0:
		k[2][2]=copy.deepcopy(t[0][1])
		k[0][1]=copy.deepcopy(t[2][2])

	if t[0][2] != 0:
		k[2][1]=copy.deepcopy(t[0][2])
		k[0][2]=copy.deepcopy(t[2][1])
				
	if t[1][0] != 0:
		k[0][2]=copy.deepcopy(t[1][0])
		k[1][0]=copy.deepcopy(t[0][2])
		
	if t[1][2] != 0:
		k[2][0]=copy.deepcopy(t[1][2])
		k[1][2]=copy.deepcopy(t[2][0])

	if t[2][0] != 0:
		k[0][1]=copy.deepcopy(t[2][0])
		k[2][0]=copy.deepcopy(t[1][2])

	if t[2][1] != 0:
		k[0][0]=copy.deepcopy(t[2][1])
		k[2][1]=copy.deepcopy(t[0][0])
								
	if t[2][2] != 0:
		k[1][0]=copy.deepcopy(t[2][2])
		k[2][2]=copy.deepcopy(t[1][0])
		
	t = copy.deepcopy(k)
		
	for i in range(3):
		for j in range (3):
			print(k[i][j], end= ' ')
		print()
	print()

