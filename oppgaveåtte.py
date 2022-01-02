from random import randrange

antallplukk = 10000       # Oek for mer noeyaktighet
antallsammefarge = 0      # Antall ganger at to sokker med samme farge ble plukket

antallsokker = 4 + 2 + 6  # Blå + grå + sorte

sokker = ["blå"]*4 + ["grå"]*2 + ["sorte"]*6

# Print sokkene i skuffen
print("Sokkene i skuffen:", sokker)
print()  # Litt space etterpå er stylish

for i in range(antallplukk):
	# Simulerer de to sokk plukkene, trekker et tall fra 0 til antall sokker
	sokk1 = randrange(0, antallsokker)
	sokk2 = randrange(0, antallsokker)

	farge1 = sokker[sokk1]
	farge2 = sokker[sokk2]

	if farge1 == farge2:
		# Hvis de har samme farge, pluss variabel med en
		antallsammefarge += 1

# Nå har vi simulert alle kastene
print("Antall plukk med samme farge :", antallsammefarge)
print("Antall plukk                 :", antallplukk)

# Regner ut relativ frekvens, altsaa hvor mange vinn delt paa antall kast vi gjorde
rel_frekvens = antallsammefarge / antallplukk

# Gang relativ frekvens med 100 for å få i prosent
sannsynlighet = round(rel_frekvens * 100, 2) # Runder av til 2 desimaler

print("Sannsynlighet: {}/{}    : {}%".format(antallsammefarge, antallplukk, sannsynlighet))
