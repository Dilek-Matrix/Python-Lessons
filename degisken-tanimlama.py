# 2000 + 2000 * %18

urunA_Fiyat = 4000
urunB_Fiyat = 3000
kdv_Orani = 0.20

print(urunA_Fiyat + (urunA_Fiyat * kdv_Orani))  # ürün A
print(urunB_Fiyat + (urunB_Fiyat * kdv_Orani))  # ürün B

urunToplami = urunA_Fiyat + urunB_Fiyat
print(urunToplami + (urunToplami * kdv_Orani))