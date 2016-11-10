def mayor(num1,num2):
	if num1 < num2:
		c=num2
	elif num1 == num2:
		c=0
	else:
		c=num1
	return c
	
print mayor(1,5)
print mayor(2,2)
print mayor(7,8)
print mayor (9,9)
