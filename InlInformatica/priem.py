#Opgave 9 en 10 (Huiswerk LE 9 + 10)

def is_priem(x):
	priem = True;
	#voor 0 en 1
	if x < 2:
		priem = False

	#voor alle andere getallen
	for i in range(2, int(x / 2)):
		if x % i == 0:
			priem = False 
			break

	return priem

def priemreeks(aantal):
	print("1e priemgetal: " + str(2))
	getal = 3
	gevonden = 2
	while gevonden <= aantal:
		if is_priem(getal):
			print (str(gevonden) + "e priemgetal: "+ str(getal))
			gevonden += 1
		getal += 2

#testen van de functie is priem
print ("Test van is_priem\n")
for i in range(50):
	print(str(i) + ": " + str(is_priem(i)))

#testen priemreeks
print ("\n\nTest van priemreeks\n")
priemreeks(100)
				