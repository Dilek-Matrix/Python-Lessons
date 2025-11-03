"""
Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
Alan: Òr²
Çevre: 2Òr

Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
mil = km / 1.609344
"""

# pi = (3.14)
# r = float(input("Yarı çap: "))

# alan = pi * (r * r)  # r** 2 yüzde de yazılabilir
# cevre = 2 * pi * r
# print("Alan: " + str(alan))
# print("Çevre: " + str(cevre))


mesafeKm = input("km: ")
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)
print(mesafeKm + " km= " + str(mesafeMil) + " mil")

