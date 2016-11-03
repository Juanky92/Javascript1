def p(lista):
	c=lista
	for ele in lista:
		lista.reverse()
	return c

print p([1,2,5,4,6])
print p([6,5,4,3,2,1,0])
