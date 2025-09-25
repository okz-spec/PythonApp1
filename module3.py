from random import *

kommide_arv = randint(1, 20)
print(f"Kommi arv laual: {kommide_arv}")

korraga = int(input("Kui palju kommi soovid ära võtta? "))

kommide_arv -= korraga
print(f"Nüüd on laual {kommide_arv} kommi.")