import math

N = float(input("Sisesta maatüki pikkus N (m): "))
M = float(input("Sisesta maatüki laius M (m): "))

diagonaal = math.sqrt(N**2 + M**2)
print(f"Ristkülikukujulise maatüki diagonaal on {diagonaal:.2f} m")