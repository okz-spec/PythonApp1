# - Ülesanne 1
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print("Tere, maailm!")

nimi = input("Sisesta oma nimi: ")

print(f"Tere, maailm! Tervitan sind {nimi}")

vanus = int(input("Kui vana sa oled? "))

print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")