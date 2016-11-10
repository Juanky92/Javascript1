def hh(rango):
	li=[]
	cont=0
	while cont <= rango:
		if cont%2==0:
			li.append(cont)
		cont+=1
	return li

print hh(10)
print hh(16)
print hh(50)
