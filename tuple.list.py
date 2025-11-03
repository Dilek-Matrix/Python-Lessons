demet = (20.26, 'Anadolu', 26+4j)
print("demet[1] = ", demet[1])  # demet[1] =  Anadolu

print("demet[0:3] = ", demet[0:3])  # demet[0:3] =  (20.26, 'Anadolu', (26+4j))

demet[1] = "Eskişehir"
print(demet)  # TypeError: 'tuple' object does not support item assignment, hata verir çünkü tuple eleman eklenemez.
