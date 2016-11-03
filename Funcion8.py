def rr(lista):
	dic={}
	for ele in lista:
		if ele%2==1:
			dic[ele]='impar'
		else:
			dic[ele]='par'
	return dic

print rr([1,3,5,4,6])
print rr([2,5,4,8,9])
