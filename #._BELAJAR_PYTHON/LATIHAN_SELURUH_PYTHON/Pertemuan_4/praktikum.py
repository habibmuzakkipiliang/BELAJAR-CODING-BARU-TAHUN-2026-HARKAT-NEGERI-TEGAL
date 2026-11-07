a = 10 + 5 * 2 ** 2
b = (10 + 5) * 2 ** 2
c = ((10 + 5) * 2) ** 2

print (a)
print (b)
print (c)



a = 10
b = 5

print (a == b)
print (a != b)
print (a >= b)
print (a <= b)


print (5 < 7 or 3 == 3)
print (5 < 7 or 3 != 3)


print (5 < 7) 
print (not 5 < 7)



total = 20
total += 5
print (total)




x = 1001
y = x

print (x == x)
print (x is y)
print (x is not y)




angka = [2, 3, 5, 9, 7]

print (5 in angka)
print (8 in angka)



print ("Selamat datang di Toko Buah Segar")
kg_apel = int (input ("Berapa kilo apel yang mau di beli"))
harga_per_kg = 20000
total = harga_per_kg * kg_apel

lebih_dari_50rb = total > 50000

print (f"Berapa yang dibeli {kg_apel} kg")
print (f"Total harga {total}")
print (f"apakah lebih dari cukup Rp 50.0000 ? {lebih_dari_50rb}")