arvud = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. arv: "))
    arvud.append(arv)

summa = sum(arvud)
jagatud = int(input("Sisesta arv, millele jagada summa: "))
jagatis = summa // jagatud
jääk = summa % jagatud

print(f"Arvude summa on {summa}")
print(f"Jagatud {jagatud} arvuga: täisarvuline osa = {jagatis}, jääk = {jääk}")