kurs = "Python ile Programlama"

print(kurs[0])  # P
print(kurs[0-1])  # a

adet = len(kurs)

print(adet)  #22
print(kurs[adet-1])

print(kurs[0:6])   # Python
print(kurs[:6])     # Python
print(kurs[11:22])  # Programlama
print(kurs[11:len(kurs)])   # Programlama
print(kurs[11:adet])     # Programlama
print(kurs[5:])        # n ile Programlama yani stop indeksini yazmasak da sonuna kadar devam eder
print(kurs[11:])        # Programlama
print(kurs[-11:-1])   # Programlam
print(kurs[-11:])        # Programlama

# adım sayısı

print(kurs[0:20:1])  # Python ile Programla 0'dan başla 20 ye kadar birer kere yaz demiş olduk
print(kurs[0:20:2])    # Pto l rgal : 1 harf atlayarak yazar.
print(kurs[0:20:3])  # Pto l rgal : 2 harf atlyarak yazar.

print(kurs[::])  # Python ile Programlama : start ve stop indekslerini yazmasak da olduğu gibi yazar
print(kurs[::1]) # Python ile Programlama : 1 yazdığımızda da aynen yazar
print(kurs[::2])  # Python ile Programlama : 1'er 1'er gitme 2'şer 2'şer git dediğimizde birini alır birini almaz
print(kurs[::-1]) #  amalmargorP eli nohtyP : ters çevirmiş oluruz
