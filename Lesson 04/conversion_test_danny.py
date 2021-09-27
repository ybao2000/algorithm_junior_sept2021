a = 'hello world'
a2 = a.split()
a3 = []
for i in a2:
	k = ""
	for j in i:
		k += str(ord(j) - 96)
	a3.append(int(k))
print(a3)
