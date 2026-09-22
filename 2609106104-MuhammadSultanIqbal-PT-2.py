harga_merchandise = [45000, 50000, 60000, 75000, 90000, 120000]

merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

biaya_bungkus_kado = 7500

total_harga = (
    merchandise_1
    + merchandise_2
    + merchandise_3
    + merchandise_4
    + merchandise_5
    + merchandise_6
    + biaya_bungkus_kado)

rata_rata = total_harga / len(harga_merchandise)

nim = 104

bolean = nim > rata_rata

kurs_usd = 15500
total_harga_usd = total_harga / kurs_usd

slice_negatif = harga_merchandise[-5:-2]

print("========= HASIL PERHITUNGAN MERCHANDISE =========")
print("Harga Merchandise 1 : Rp", merchandise_1)
print("Harga Merchandise 2 : Rp", merchandise_2)
print("Harga Merchandise 3 : Rp", merchandise_3)
print("Harga Merchandise 4 : Rp", merchandise_4)
print("Harga Merchandise 5 : Rp", merchandise_5)
print("Harga Merchandise 6 : Rp", merchandise_6)
print("Biaya Bungkus Kado  : Rp", biaya_bungkus_kado)
print("-------------------------------------------------")
print("Total Harga (IDR)   : Rp", total_harga)
print("Rata-rata           :", rata_rata)
print("NIM                 :", nim)
print("Status (NIM > Avg)  :", bolean)
print("-------------------------------------------------")
print("List Merchandise    :", harga_merchandise)
print("Total Harga (USD)   : $", round(total_harga_usd, 2))
print("Slice Negatif (-5:-2):", slice_negatif)
print("=================================================")