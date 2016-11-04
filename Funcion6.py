def Sumar(lista):
	Sumar=0
	for ele in lista:
		Sumar+=ele
	return Sumar
def Restar(lista):
	Restar=0
	for ele in lista:
		Restar=-ele-Restar
	return Restar

print Restar([8,5])
