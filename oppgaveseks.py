from random import randint

kast = 10000 # Øk for mer nøyaktighet
antall = 0
for i in range(kast):
	terning1 = randint(1, 4) # Simulerer begge terning-kastene
	terning2 = randint(1, 6) #
	print('Terning 1:', terning1, ' Terning 2:', terning2) # Hvis du vil se verdiene
	if terning1 + terning2 == 7: # Hvis summen er 7, øk antall med en
		antall += 1

relativ_frekvens = antall / kast # Sannsynligheten, gang med 100 for prosent
print(antall, '/', kast)
print('Relativ frekvens:', relativ_frekvens)
