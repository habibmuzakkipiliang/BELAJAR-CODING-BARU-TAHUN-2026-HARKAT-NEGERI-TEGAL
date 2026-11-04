# variabel 

a = "Halo Dunia"
print ("A =", a)

b = "Halo For"
print ("B =", b)

c = 12
print ("C =", c)

d = True
print ("D =", d)


print ("\n --- batas --- \n")



# Fungsi dengan error handling

def run (a):

    try:
        if a < 0:
            raise ("gagal")

        if a >= 8:
            print (f"Besar, angka a = {a}")

        else:
            print (f"Kecil, angka a = {a}")

    except:
        print (f"Gak boleh minus, angka a = {a}")

run (10)
run (9)
run (4)
run (3)
run (1)
run (2)
run (-12)
run (-45)
run (-3)
run (-5)
run (-0) 


print ("\n --- batas --- \n")




# Error Handling

def hun (k):

    try:
        if k < 0:
            raise ("Gagal")

        if k >= 8:
            print (f"Besar, angka k = {k}")

        elif k >= 5:
            print (f"Sedang, angka k = {k}")

        else:
            print (f"Kecil, angka k = {k}")

    except:
        print (f"Gak boleh angka k = {k}")

hun (-10)
hun (-4)
hun (-3)
hun (-2)
hun (-1)
