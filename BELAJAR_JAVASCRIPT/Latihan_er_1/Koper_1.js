// Hello Worlde

console.log ("Hello World")


console.log ("\n --- batAS ---- \n")



// Variabel dasar

var a = "Halo Dunia"
console.log ("A =", a)

var b = 12
console.log ("B =", b)

var c =  12.12
console.log ("C =", c)


console.log ("\n --- batas --- \n")




// fungsi operator dasar

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

function modulus (x, y) {
    return x % y
}

function bagi (x, y) {
    return x / y
}


console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Bagi =", bagi (x, y))
console.log ("Modulus =", modulus (x, y))


console.log ("\n --- batas --- \n")




// Tipe data pemrograman

var teks = "Halo Dunia"
var angka = 12
var desimal = 1221.1
var cek = true

var tu = `
- Teks      : ${teks}
- Angka     : ${angka}
- Desimal   : ${desimal}
- Cek       : ${cek}

`

console.log (tu)

console.log ("\n --- btaas --- \n")




// Percabangan dasar

var f = 9

if (f >= 7) {
    console.log (`besar, angka f = ${f}`)
}

else {
    console.log (`kecil, angka f = ${f}`)
}


console.log ("\n --- batas --- \n")




// Percabangan lanjutan

var r = 3

if (r >= 6) {
    console.log (`Besar, angka r = ${r}`)
}

else if (r >= 5) {
    console.log (`Sedang, angka r = ${r}`)
}

else {
    console.log (`kecil, angka r = ${r}`)
}


console.log ("\n --- batas --- \n")




// Percabangan nested 1

var k = 3
var cek = true

if (k >= 7) {
    if (cek) {
        console.log (`Besar, angka k = ${k}`)
    }

    else {
        console.log (`Sedang, angka k = ${k}`)
    }
}

else {
    console.log (`Kecil, angka k = ${k}`)
}

console.log ("\n --- batas --- \n")



// Fungsi dasar dengan percabangan dasar

function er (k) {

    if (k >= 8) {
        console.log (`besar, angka k = ${k}`)
    }

    else {
        console.log (`kecil, angka k = ${k}`)
    }
}

er (10)
er (9)
er (5)
er (3)
er (2)
er (1)

console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan lanjutan

function ok (e) {

    if (e >= 8) {
        console.log (`besar, angka e = ${e}`)
    }

    else if (e >= 5) {
        console.log (`sedang, angka e = ${e}`)
    }

    else {
        console.log (`kecil, angka e = ${e}`)
    }
}

ok (10)
ok (9)
ok (8)
ok (7)
ok (5)
ok (4)
ok (3)
ok (2)
ok (1)

console.log ("\n --- batas ---- \n")