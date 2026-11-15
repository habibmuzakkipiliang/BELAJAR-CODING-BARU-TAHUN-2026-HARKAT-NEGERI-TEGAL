console.log ("Hello World")


console.log ("\n --- batas --- \n")




var a = "Halo Dunia"
console.log ("A =", a)

var b = 12
console.log ("B =", b)

var c = true
console.log ("C =", c)


console.log ("\n --- batas --- \n")




// Fungsi dengan operator dasar

var x = 4
var y = 2

function tambah (x, y) {
    return x + y
}

function kurang (x, y) {
    return x - y
}

function kali (x, y) {
    return x * y
}

function bagi (x, y) {
    return x / y
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
console.log ("Bagi =", bagi (x, y))
console.log ("Modulus =", modulus (x, y)) 


console.log ("\n --- batas --- \n")




// Arrow Fungsi 

var dasar = () => {
    console.log ("Hello World")
}

dasar ()


console.log ("\n -- batas -- \n")


var der = (nama) => {
    console.log (`Halo nama ${nama} dari jakarta timur`)
}

der ("Yan")