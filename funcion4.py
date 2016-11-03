def mm(num):
	h=''
	d=''
	if num <=10:
		h='Hola'
	else:
		d='Adios'
	return h or d
print mm(5)
print mm(15)
print mm(2)
print mm(45)
print mm(8)
