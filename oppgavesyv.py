from random import randrange  # bruk en funksjon for tilfeldighet i biblioteket 'random'

antallkast = 100000   # oek for mer noeyaktighet
antallvinn = 0        # antall ganger man har vunnet
for i in range(antallkast):
	# Simulerer to terning kast
	kast1 = randrange(1, 7)
	kast2 = randrange(1, 7)

	# Sjekker om minst en av terningene er 5 eller 6
	if kast1 == 5 or kast1 == 6 or kast2 == 5 or kast2 == 6:
		# Vi vant! Oek med en
		antallvinn += 1

# Naa har vi simulert alle kastene
print("Antall vinn:", antallvinn)
print("Antall kast:", antallkast)

# Regner ut relativ frekvens, altsaa hvor mange vinn delt paa antall kast vi gjorde
rel_frekvens = antallvinn / antallkast

# Gang relativ frekvens med 100 for aa faa i prosent
sannsynlighet = round(rel_frekvens * 100, 2) # Runder av til 2 desimaler

print("Relativ frekvens: {} / {} eller {}%".format(antallvinn, antallkast, sannsynlighet))
