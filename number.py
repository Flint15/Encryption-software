abcRu = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
x = input()
y = input()
x = "".join(x.split())
x = x.lower()
y = y.lower()
z = []
if len(x)%len(y) == 0:
	y = y*len(x[:int(len(x)//len(y))])
elif len(x)%len(y) != 0:
	y = y*len(x[:int(len(x)//len(y))])+y[:len(x)%len(y)]
for i in range(len(x)):
	if (abcRu.index(x[i])+abcRu.index(y[i])) <= len(abcRu): 
		z.append(abcRu[1+(abcRu.index(x[i])+abcRu.index(y[i]))])
	elif (abcRu.index(x[i])+abcRu.index(y[i])) >= len(abcRu):
		n = abcRu.index(x[i])+abcRu.index(y[i])
		z.append(abcRu[1+n-len(abcRu)])
print("".join(z))