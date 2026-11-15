print ("""
=====================================================================================

USIA MASUK DAN JOIN JKT48 TAHUN 2026 

======================================================================================

""")

status = str (input ("Masukkan jenjang pendidikan atau kerja atau nikah kamu  = "))
usia = int (input ("Masukkan usia kamu sekarang ini (15 - 19) = "))

if status == "Nikah":
    if usia >= 13 and usia <= 19:
        print (f"Usia dan status sudah mencukupi persyaratan, usia = {usia} dan status = {status}")

    else:
        print (f"kamu sudah mencukupi usia, tapi belum mencukupi kerja, usia = {usia} dan status = {status}")

elif status == "Kerja":
    if usia >= 13 and usia <= 18:
        print (f"Usia dan status sudah cukup, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi, usia = {usia} dan status = {status}")

elif status == "Mahasiswa":
    if usia >= 13 and usia <= 18:
        print (f"Usia sudah mencukupi dan sudah mencukupi status nya, usia = {usia} dan status = {status}")

    else:
        print (f"Belum mencukupi usia dan status nya, usia = {usia} dan status = {status}")

elif status == "SMA atau MAN":
    if usia >= 13 and usia <= 19:
        print (f"usia kamu sudah tercapai dan status sudah oke, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi, usia = {usia} dan status = {status}")


elif status == "SMP":
    if usia >= 13 and usia <= 19:
        print (f"usia sudah mencukupi dan status nya juga oke, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi saat ini, usia = {usia} dan status = {status}")

elif status == "SD":
    if usia >= 13 and usia <= 18:
        print (f"Usia sudah mencukupi dan status juga oke, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi, usia = {usia} dan status = {status}")

else:
    print ("Input invalid")


print ("\n --- batas --- \n")




print ("""
======================================================================================

USIA MASUK DAN JOIN JKT48 

======================================================================================

""")

usia = int (input ("Masukkan usia kamu sekarang = "))
cek = True

if usia >= 13 and usia <= 18:
    if cek:
        print (f"Sudah lebih dari cukup, usia = {usia}")

    elif usia > 18:
        print (f"Sudah pas dan boleh gabung ke JKT48, usia = {usia}")

else:
    print (f"Usia belum cukup, usia = {usia}")


print ("\n --- batas --- \n")





print ("""
=====================================================================================

USIA PRODUKTIF MANUSIA

======================================================================================

""")

usia = int (input ("Masukkan usia kamu = "))
cek = True

if usia >= 15 and usia <= 55:
    if cek:
        print (f"Sudah masuk usia produktif, usia = {usia}")

    elif usia > 55:
        print (f"Sudah tua dan pensiun, usia = {usia}")

else:
    print (f"Masih belum produktif dan masih kecil, usia = {usia}")


print ("\n --- batas --- \n")



print ("""
======================================================================================

Percabangan Sudah Kuliah

======================================================================================
""")

usia = int (input ("Masukkan usia kamu sekarang = "))
cek = True

if usia >= 18 and usia <= 25:
    if cek:
        print (f"Sudah boleh kuliah, usia = {usia}")

    elif usia > 25:
        print (f"sudah kerja, usia = {usia}")

else:
    print (f"Masih kecil usianya, usia = {usia}")


print ("\n --- batas --- \n")