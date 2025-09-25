arvud = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. arv: "))
# - Ülesanne 2
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print("Vanus on tüüp:", type(vanus))
print("Eesnimi on tüüp:", type(eesnimi))
print("Pikkus on tüüp:", type(pikkus))
print("Kas käib koolis on tüüp:", type(kas_käib_koolis))

kas_käib_koolis = False

if isinstance(kas_käib_koolis, bool):
    print("Muuttuja 'kas_käib_koolis' on boolean tüüpi.")
else:
    print("Muuttuja 'kas_käib_koolis' ei ole boolean tüüpi.")