P = int(input("Mitu inimest on? "))
hind = 12.90
toetust = 0.10
jootraha = hind * toetust
hind_koos_jootraha = hind + jootraha

maksmine = hind_koos_jootraha / P
print(f"Igaüks peab maksma {maksmine:.2f} €")