// Hello World

console.log ("Hello World")


console.log ("\n --- batas --- \n")



// Variabel

var a = "Halo Dunia"
console.log ("A =", a)

var b = "Halo Fun"
console.log ("B =", b)

var c = 12
console.log ("C =", c)

var d = 12.21
console.log ("D =", d)

var e = true
console.log ("E =", e)


console.log ("\n --- batas --- \n")



// Operator dasar

var x = 9
var y = 3

function tambah (x, y) {
    return x + y
}

function kurang (x, y) {
    return x - y
}

function kali (x, y) {
    return x * y
}

function pangkat (x, y) {
    return x ** y
}

function bagi (x, y) {
    return x / y
}

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y)) 
console.log ("Bagi =", bagi (x, y))


console.log ("\n --- batas --- \n")



// Operator perbandingan

console.log ("Hasil =", x < y)
console.log ("Hasil =", x > y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


console.log ("\n --- batas --- \n")




// Operator Logika

console.log ("Hasil =", x > y && x < y)
console.log ("Hasil =", x < y || x > y)
console.log ("Hasil =", ! (x < y))
console.log ("Hasil =", ! (x > y))


console.log ("\n --- batas --- \n")


// Fungsi dengan percabangan dasar

function df (a) {
    
    if (a >= 8) {
        console.log (`Besar, angka a = ${a}`)
    }
    
    else {
        console.log (`Kecil, angka a = ${a}`)
    }
}

df (10)
df (9)
df (8)
df (7)
df (6)
df (5)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan dasar

function der (f) {

    if (f >= 8) {
        console.log (`Besar, angka f = ${f}`)
    }

    else {
        console.log (`Kecil, angka f = ${f}`)
    }
}

der (10)
der (9)
der (8)
der (7)
der (5)
der (4)
der (3)
der (2)
der (1)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan lanjutan

function df (g) {

    if (g >= 8) {
        console.log (`Besar, angka g = ${g}`)
    }

    else if (g >= 5) {
        console.log (`Sedang, angka g = ${g}`)
    }

    else {
        console.log (`Kecil, angka g = ${g}`)
    }
}

df (10)
df (9)
df (8)
df (7)
df (6)
df (5)
df (4)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan nested 1

function der (j) {

    cek = true

    if (j >= 8) {
        if (cek) {
            console.log (`Besar, angka j = ${j}`)
        }

        else {
            console.log (`Sedang, angka j = ${j}`)
        }
    }

    else {
        console.log (`Kecil, angka j = ${j}`)
    }
}

der (10)
der (9)
der (8)
der (7)
der (6)
der (5)
der (4)
der (2)
der (3)
der (1)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan nested 2

function fer (k) {

    cek = true

    if (k >= 8) {
        if (cek) {
            console.log (`Besar, angka k = ${k}`)
        }

        else if (k >= 5) {
            console.log (`Sedang, angka k = ${k}`)
        }
    }

    else {
        console.log (`Kecil, angka k = ${k}`)
    }
}

fer (10)
fer (9)
fer (8)
fer (7)
fer (5)
fer (6)
fer (4)
fer (3)
fer (2)
fer (1)


console.log ("\n --- batas --- \n")




// fungsi dengan percabangan nested 5

function ger (l) {

    cek = true

    if (l >= 8) {
        if (cek) {
            console.log (`Besar, angka l = ${l}`)
        }

        else if (l >= 5) {
            console.log (`Kecil, angka l = ${k}`)
        }

        else {
            console.log (`Kecil, angka l = ${l}`)
        }
    }

    else {
        console.log (`Angka biasa, angka l = ${l}`)
    }
}

ger (10)
ger (9)
ger (8)
ger (7)
ger (6)
ger (5)
ger (4)
ger (3)
ger (3)
ger (2)
ger (1)


console.log ("\n --- batas --- \n")