// Hello World

console.log ("Hello World")

console.log ("\n --- batas --- \n")


// Biodata pribadi

let nama : string = "Habib Muzakki"
let akrab : string = "Habib"
let kelas : string = "1B"
let jurusan : string = "D4 Teknik Informatika"
let fakultas : string = "Sekolah Vokasi"
let hobi : string = "JKT48"

let biodata_lengkap = `
\n Nama lengkap     : ${nama}
\n Nama panggilan   : ${akrab}
\n Kelas            : ${kelas}
\n Jurusan          : ${jurusan}
\n Fakultas         : ${fakultas}
\n Hobi             : ${hobi}

`

console.log (biodata_lengkap)

console.log ("\n --- batas --- \n")



// Variabel dasar

var a : string = "Halo dunia pagi ku yang indah"
var b : string = "Halo JKT48"
var c : string = "Halo Pagi ku"
var d : string = "Halo Fans JKT48"
var e : string = "Halo Indonesia"
var fun : string = "Halo Bukittinggi"
var fer : string = "Halo Festival Tahunan"
var ger : string = "Halo Yundai"

console.log (a)
console.log (b)
console.log (c)
console.log (d)
console.log (e)
console.log (fun)
console.log (ger)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

let teks : string = "Halo Dunia"
let angka : number = 12
let desimal : number = 31.12
let cek : boolean = true

let tipe_awal = `
\n Teks     : ${teks}
\n Angka    : ${angka}
\n Desimal  : ${desimal}
\n Cek      : ${cek}

`

console.log (tipe_awal)


console.log ("\n --- batas --- \n")



// Cek tipe data pemrograman

console.log ("Teks =", typeof (teks))
console.log ("Angka =", typeof (angka))
console.log ("Desimal =", typeof (desimal))
console.log ("Cek =", typeof (cek))


console.log ("\n --- batas --- \n")



// Fungsi return dengan operator dasar

let x : number = 10
let y : number = 5

function tambah (x : number, y : number) {
    return x + y
}

function kurang (x : number, y : number) {
    return x - y
}

function kali (x : number, y : number) {
    return x * y
}

function pangkat (x : number, y : number) {
    return x ** y
}

function modulus (x : number, y : number) {
    return x % y
}

function bagi (x : number, y : number) {
    return x / y
}


console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Bagi =", bagi (x, y))
console.log ("Pangkat =", pangkat (x, y))


console.log ("\n --- batas --- \n")


