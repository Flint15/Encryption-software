abcRu = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
morze = [".-","-...",".--","--.","-..",".",".","...-","--..","..",".---","-.-",".-..","--","-.","---",".--.",".-.","...","-","..-","..-.","....","-.-.","---.","----","--.-","-..-","-.--","-..-","..-..","..--",".-.-"]

decMessege = []

y = input("морзе или rot1")
z = input("расшифровать или зашифровать?")
x = input()

if y == "морзе":
	x = "".join(x.split())
	n = 0
	if x[n].lower() in abcRu:
		for i in x:
			decMessege.append(morze[abcRu.index(x[n].lower())])
			n+=1
	elif x[n].lower() in morze:
		for i in x:
			decMessege.append(abcRu[morze.index(x[n].lower())])
			n+=1
	print(decMessege, end= " ")

elif y == "rot1":
	x = "".join(x.split())
	n = 0
	if z == "зашифровать":
		for i in x:	
			if abcRu.index(x[n].lower()) == 32:
				decMessege.append(abcRu[0])
			else:	
				decMessege.append(abcRu[abcRu.index(x[n].lower())+1])
			n+=1
	elif z == "расшифровать":
		for i in x:
			if abcRu.index(x[n].lower()) == 0:
				decMessege.append(abcRu[32])
			else:
				decMessege.append(abcRu[abcRu.index(x[n].lower())-1])
			n+=1 				
	print(decMessege, end= " ")	

elif z == "замена":
	y = "".join(x.split())
	x = x.split() 
	h = int(len(x[0]))
	if len(y) % h != 0:
		g = (len(y) // h) + 1
	elif len(y) % h == 0:
		g = len(y) // h
	print(y,x)
	for i in range(h):		
		n = 0
		n += i
		for j in range(g):			
			if len(y) <= n:
				n = n - len(y) 
			else:	
				print(y[n],y.index(y[n]))
				decMessege.append(y[n])
				n += len(x[0])
	print(decMessege)

else:
	for i in range(33):
		n = 0
		n += i
		print(" ".join(abcRu[n:]), " ".join(abcRu[0:n]))
			


			