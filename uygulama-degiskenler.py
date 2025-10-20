""" 
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Sadık Turan
053221234567
info@sadikturan.com
Kocaeli

Satın Alınan Ürünler

Ürün adı: Kablosuz Mouse
Fiyatı: 550 TL

Ürün adı: Kablosuz Klavye
Fiyatı: 650 TL

Ürün adı: Dizüstü Bilgisayar
Fiyatı: 55.000 TL

"""



musteri_Ad = "Sadık"
musteri_Soyad = "Turan"
musteri_Telefon ="053221234567"
musteri_Adres = "Kocaeli"
musteri_Email = "info@sadikturan.com"

urun1_Ad = "Kablosuz Mouse"
urun1_Fiyat = 550


urun2_Ad = "Kablosuz_Klavye"
urun2_Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3_Fiyat = 55000

toplamOdenenUcret  = urun1_Fiyat + urun2_Fiyat + urun3_Fiyat
print("Toplam ödenen miktar " + str(toplamOdenenUcret))

print("Toplam kdv oranı: " + str(toplamOdenenUcret * 0.18))
