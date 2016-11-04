def we(lista):
	mayor=lista[0]
	for ele in lista:
		if mayor < ele:
			mayor=ele
	return mayor
	
print we([2,5,4,6])
