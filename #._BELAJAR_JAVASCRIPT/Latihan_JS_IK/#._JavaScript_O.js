// Halo JavaScript dan Tes JavaScript

console.log ("Hello World")


console.log ("\n --- batas --- \n")




// Variabel dasar

var a = "Halo Nikson"
var b = "Halo Boge"
var c = "Halo Jojo"
var d = "Halo Kris"
var e = "Halo Isko"

console.log (a)
console.log (b)
console.log (c)
console.log (d)
console.log (e)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman JavaScript

var teks = "Halo Dunia"
var angka = 12
var desimal = 12.12
var cek = true

var tipe = `

\n Teks     : ${teks}
\n Angka    : ${angka}
\n Desimal  : ${desimal}
\n Cek      : ${cek}
`

console.log (tipe)



console.log ("\n --- batas --- \n")



// Fungsi return JavaScript dengan operator dasar

var x = 10
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

function bagi (x, y) {
    return x / y
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



// Fungsi return dengan mencari angka terkecil

function besar (a, b) {
    if (a > b) {
        return a
    }
    
    else {
        return b
    }
}

console.log ("Angka besar =", besar (10, 9))
console.log ("Angka besar =", besar (9, 10))
console.log ("Angka besar =", besar (9, 45))
console.log ("Angka besar =", besar (40, 5))

console.log ("\n --- batas --- \n")





// Fungsi return dengan mencari angka terkecil

function kecil (e, r) {

    if (e < r) {
        return e
    }

    else {
        return r
    }
}

console.log ("Kecil =", kecil (10, 4))
console.log ("Kecil =", kecil (50, 34))
console.log ("Kecil =", kecil (40, 3))


console.log ("\n --- batas --- \n")



// Fungsi return dengan nama 

function nama (halo) {
    return `Halo nama saya ${halo} dari Jakarta`
}

nama ("Habib")
nama ("Rayyan")
nama ("Fayyan")
nama ("Ron")
nama ("Ero")
nama ("Run")


console.log ("\n --- batas --- \n")