def nn(lista):
	li=[]
	cont= 0
	while cont < len(lista):
		if cont%2==1:
			li.append(lista[cont])
		cont+=1
	return li

print nn([1,True,8,3,4,'Pakito',5])
