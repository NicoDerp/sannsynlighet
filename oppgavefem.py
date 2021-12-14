from random import randint

antallkast = 10000 # Øk for mer nøyaktighet
myntsum = 0
for i in range(antallkast):
	s = sum([randint(0,1) for _ in range(3)]) # Antall kronestykker som ble mynt ut av de tre kronestrykkene
	if s==2: # Sjekker om 2 ut av 3 kronestykker ble mynt
		myntsum += 1

relativ_frekvens = myntsum / antallkast # Sannsynligheten
print("Antall kast:", antallkast)
print("Relativ frekvens:", relativ_frekvens)
