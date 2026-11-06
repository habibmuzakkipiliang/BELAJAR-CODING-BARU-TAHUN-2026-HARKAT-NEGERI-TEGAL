print ("Selamat datang di Game Store")

harga_diamond = 2000

jumlah_diamond = int (input ("Masukkan jumlah diamond = "))
bayar = int (input ("Masukkan uang yang dibayarkan = "))

total_bayar = harga_diamond * jumlah_diamond 

kembalian = bayar - total_bayar

total = f"""
- Total bayar   : {total_bayar}
- Kembalian     : {kembalian}
"""

print (total)
