console.log ("Hello World")


console.log ("\n --- batas --- \n")



// Biodata Habib Muzakki

var nama = "Habib Muzakki"
var akrab = "Habib"
var kelas = "1B"
var jurusan = "D4 Teknik Informatika"
var fakultas = "Sekolah Vokasi"
var coding = "HTML, CSS, JavaScript dan Python dan TypeScript"
var hobi = "JKT48 dan suka dengan Oshi JKT48 yang cantik-cantik amat"
var usia = "19 tahun"
var asal_daerah = "Kota Serang, Banten"
var marga = "Piliang"
var suku = "Minangkabau"


var biodata = `
\n Nama lengkap     : ${nama}
\n Nama panggilan   : ${akrab}
\n Asal daerah      : ${asal_daerah}
\n Kelas            : ${kelas}
\n Jurusan          : ${jurusan}
\n Fakultas         : ${fakultas}
\n Coding           : ${coding}
\n Hobi             : ${hobi}
\n Usia kamu        : ${usia}
\n Marga            : ${marga}
\n Suku daerah      : ${suku}
`
console.log (biodata)

console.log ("\n --- batas --- \n")



// Variabel dasar

var hun = "Halo Dunia"
console.log (hun)

var jun = "Halo dunia yang sangat cantik dan indah"
console.log (jun)

var dun = "Halo Dunia Internasional kita"
console.log (dun)

var fer = "Halo Kita adalah orang baru disini"
console.log (fer)

var der = "Halo Kita Baik"
console.log (der)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "Halo Dunia"
var angka = 12
var desimal = 12.12
var cek = true

var tipe_data = `
\n Teks        : ${teks}
\n Angka       : ${angka}
\n Desimal     : ${desimal}
\n Cek         : ${cek}

`

console.log (tipe_data)

console.log ("\n --- batas --- \n")



// Cek tipe data pemrograman

console.log ("Teks =", typeof (teks))
console.log ("Angka =", typeof (angka))
console.log ("Desimal =", typeof (desimal))
console.log ("Cek =", typeof (cek))


console.log ("\n --- batas --- \n")



// Fungsi return dengan operasi dasar

var x = 10
var y = 5

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




// Fungsi return dalam rumus bangun datar

var s = 9

function persegi (s, s) {
    return s * s
}

function keliling_persegi (s, s) {
    return 4 * s
}

console.log ("Luas persegi =", persegi (s, s))
console.log ("Keliling persegi =", keliling_persegi (s, s))


console.log ("\n --- batas --- \n")



// Fungsi return dengan lingkaran

var phi = 3.14
var r = 8

function luas_lingkaran (phi, r) {
    return phi * r * r
}

function keliling_lingkaran (phi, r) {
    return 2 * phi * r
}


console.log ("Luas lingkaran =", luas_lingkaran (phi, r))
console.log ("Keliling lingkaran =", keliling_lingkaran (phi, r))


console.log ("\n --- batas --- \n")



// Fungsi return dengan persegi panjang 

var p = 9
var l = 3

function persegi_panjang (p, l) {
    return p * l
}

function kel_persegi_panjang  (p, l) {
    return 2 * (p + l)
}


console.log ("Luas persegi panjang =", persegi (p, l))
console.log ("Kelilig persegi panjang =", kel_persegi_panjang (p, l))


console.log ("\n --- batas --- \n")


// Percabangan dasar

var e = 9

if (e >= 7) {
    console.log (`besar, angka e = ${e}`)
}

else {
    console.log (`kecil, angka kecil = ${e}`)
}


console.log ("\n --- batas --- \n")



// Percabangan lanjutan 

var f = 3

if (f >= 8) {
    console.log (`besar, angka f = ${f}`)
}

else if (e >= 5) {
    console.log (`sedang, angka e = ${e}`)
}

else {
    console.log (`kecil, angka e = ${e}`)
}


console.log ("\n --- batas --- \n")