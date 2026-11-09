// Hello World

console.log ("Hello World")


console.log ("\n --- batas --- \n")



// variabel

var a = "Hello World"
console.log ("A =", a)

var b = "Halo Fun"
console.log ("B =", b)

var c = 12
console.log ("C =", c)

var d = true
console.log ("D =", d)


console.log ("\n --- batas --- \n")



// operasi dasar

var x = 8
var y = 4

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

function modulus (x, y) {
    return x % y
}

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Modulus =", modulus (x, y))


console.log ("\n --- batas --- \n")




// Operasi perbandingan

console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


console.log ("\n --- batas --- \n")



// Operasi logika

console.log ("Hasil =", x < y && x > y)
console.log ("Hasil =", x > y || x < y)
console.log ("Hasil =", ! (x < y))
console.log ("Hasil =", ! (x > y))


console.log ("\n --- batas --- \n")



// Fungsi dasar dengan percabangan dasar

function un (a) {

    if (a >= 5) {
        console.log (`Besar, angka a = ${a}`)
    }

    else {
        console.log (`Kecil, angka a = ${a}`)
    }
} 

un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (2)
un (1)


console.log ("\n --- batas --- \n")



// Fungsi dasar dengan percabangan lanjutan

function ju (b) {

    if (b >= 8) {
        console.log (`Besar, angka b = ${b}`)
    }

    else if (b >= 5) {
        console.log (`Sedang, angka b = ${b}`)
    }

    else {
        console.log (`Kecil, angka b = ${b}`)
    }
} 

ju (10)
ju (9)
ju (8)
ju (7)
ju (6)
ju (5)
ju (4)
ju (3)
ju (2)
ju (1)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan nested

function df (h) { 

    cek = true

    if (h >= 8) {
        if (cek) {
            console.log (`Besar, angka h = ${h}`)
        }

        else {
            console.log (`Sedang, angka h = ${h}`)
        }
    }

    else {
        console.log (`Kecil, angka h = ${h}`)
    }
}

df (10)
df (9)
df (8)
df (7)
df (6)
df (5)
df (4)
df (3)
df (2)
df (1)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan nested 

function ij (g) {

    if (g >= 8) {
        if (cek) {
            console.log (`Besar, angka g = ${g}`)
        }

        else if (g >= 5) {
            console.log (`Sedang, angka g = ${g}`)
        }

        else {
            console.log (`Kecil, angka g = ${g}`)
        }
    }
}

ij (10)
ij (9)
ij (8)
ij (7)
ij (6)
ij (5)
ij (4)
ij (3)
ij (2)
ij (1)


console.log ("\n --- batas --- \n")