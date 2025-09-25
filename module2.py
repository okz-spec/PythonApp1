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