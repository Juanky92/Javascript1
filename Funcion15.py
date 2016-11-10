def comparar(num1,num2):
	if num1==num2:
		c=0
	elif num1>num2:
		c=1
	else:
		c=-1
	return c
	
print comparar(2,1)
print comparar(1,2)
print comparar(2,2)
