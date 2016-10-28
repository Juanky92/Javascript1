def mm(lista):
	Suma=0
	for ele in lista:
		if ele >=0:
			Suma=Suma+ele
		else:
			print 'negativo'
	return Suma

print mm([1,2,5,-4])
