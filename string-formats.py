# string concat
ad ="Dilek"
soyad ="İnce"
yas = 49

# msj = "My name is " + ad + " " + soyad + "." + "I'm " + str(yas) + " years old."
# print(msj)  # My name is Dilek İnce. I'm 49 years old.

# string format

# msj= "My name is {} {}. I'm {} years old.".format(ad, soyad, yas)
# Yine aynı çıktıyı verir. My name is Dilek İnce.I'm 49 years old.
msj = "My name is {0} {1}. I'm {2} years old.".format(ad, soyad, yas)
# My name is Dilek İnce. I'm 49 years old.

# takma isimler de kullanabiliriz
# msj = "My name is {a} {s}. I'm {y} years old.".format(a=ad, s=soyad, y=yas)
# My name is Dilek İnce. I'm 49 years old.


# f-string
msj= f"My name is {ad} {soyad}. I'm {yas} years old."  # My name is Dilek İnce. I'm 49 years old.

print(msj)