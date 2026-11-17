# Error Handling

try:
    a = 10 + 10
    print (a)

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Oke")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")



# Error Handling 2

try:
    a = 10 / 0
    print (a)

except ZeroDivisionError:
    print ("gagal")

else:
    print ("oke")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")



# Error Handling 2

try:
    h = 20 / 0
    print (h)

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Oke")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")




# Fungsi dengan Error Handling

def fun (f):

    try:
        if f < 0:
            raise ("Gagal")

        if f >= 8:
            print (f"besar, angka a = {f}")

        else:
            print (f"kecil, angka a = {f}")

    except:
        print (f"Gak boleh minus, angka a = {f}")

fun (-10)
fun (10)
fun (-4)
fun (-3)
fun (12)


print ("\n --- batas --- \n")



# Error Handling 3

def run (r):

    try:
        if a < 0:
            raise ("Gagal")

        if a >= 8:
            print (f"Besar, angka a = {a}")

        elif a >= 5:
            print (f"Sedang, angka a = {a}")

        else:
            print (f"Kecil, angka a = {a}")

    except:
        print (f"Gak boleh minus, angka a = {a}")

run (10)
run (9)
run (6)
run (3)
run (2)
run (-1)
run (-3)
run (-4)
run (-5)
run (-6)

print ("\n --- batas --- \n")