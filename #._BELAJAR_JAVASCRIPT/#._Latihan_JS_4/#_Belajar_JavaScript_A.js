console.log ("Hello World")


console.log ("\n --- batas --- \n")



// variabel dasar

var pagi = "Halo Pagi hari"
var siang = "Halo Siang hari"
var malam = "Halo malam hari"
var sore = "Halo Sore hari"


console.log (pagi)
console.log (siang)
console.log (malam)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "Halo Dunia"
var angka = 12
var desimal = 23.23
var cek = true

var tipe = `
\n Teks     : ${teks}
\n Angka    : ${angka}
\n Desimal  : ${desimal}
\n Cek      : ${cek}


`

console.log (tipe)


console.log ("\n --- batas --- \n")



// Cek tipe data pemrograman

console.log ("Teks =", typeof (teks))
console.log ("Angka =", typeof (angka))
console.log ("Desimal =", typeof (desimal))
console.log ("Cek =", typeof (cek))


console.log ("\n --- batas --- \n")



// Fungsi return dengan operator dasar

var x = 10
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
console.log ("Pangkat =", pangkat (x, y))
console.log ("Modulus =", modulus (x, y))


console.log ("\n --- batas --- \n")



// Biodata Habib Muzakki

var namaLengkap = "Habib Muzakki"
var namaPanggilan = "Habib"
var asalDaerah = "Kota Serang"
var codingSaya = "HTML, CSS, JavaScript dan Python"
var asalSekolah = "MAN 2 KOTA SERANG"
var jurusanKuliah = "D4 Vokasi Teknik Informatika"
var fakultasKuliah = "Sekolah Vokasi"
var kelasKuliah = "1B"


var profil = `
\n Nama lengkap     : ${namaLengkap}
\n Nama panggilan   : ${namaPanggilan}
\n Asal daerah      : ${asalDaerah}
\n Coding saya      : ${codingSaya}
\n Asal sekolah     : ${asalSekolah}
\n Jurusan kuliah   : ${jurusanKuliah}
\n Fakultas         : ${fakultasKuliah}
\n Kelas kuliah     : ${kelasKuliah}

`


console.log ("\n --- batas --- \n")



// Switch Case dengan lampu lalu lintas

var lampu_lintas = "Merah"

switch (lampu_lintas) {

    case "Merah":
        console.log ("Warna merah")
        break

    case "Kuning":
        console.log ("Warna kuning")
        break

    case "Hijau":
        console.log ("Warna hijau")
        break

    default:
        console.log ("Input tidak valid")
}


console.log ("\n --- batas --- \n")



// Switch Case dengan angka 

var angka = 5

switch (angka) {

    case 1:
        console.log (1)
        break

    case 2:
        console.log (2)
        break

    case 3:
        console.log (3)
        break

    case 4:
        console.log (4)
        break

    case 5:
        console.log (5)
        break

    case 6:
        console.log (6)
        break

    case 7:
        console.log (7)
        break

    case 8:
        console.log (8)
        break

    default:
        console.log ("Input tidak valid")
}


console.log ("\n ---- batas --- \n")



// Percabangan Nested

var angka = 10
var cek = true

if (angka >= 6) {
    if (cek == true) {
        console.log (`Angka oke, angka = ${angka}`)
    }

    else {
        console.log (`Angka kurang oke, angka = ${angka}`)
    }
}

else {
    console.log (`Angka belum oke, angka = ${angka}`)
}


console.log ("\n --- batas --- \n")



// Percabangan dasar

var angka = 10

if (angka >= 5) {
    console.log (`Besar, angka pertama = ${angka}`)
}

else {
    console.log (`Kecil, angka pertama = ${angka}`)
}

console.log ("\n --- batas --- \n")




// Percabangan lanjutan 

var angka_1= -19

if (angka_1 > 0) {
    console.log (`Angka positif, angka random = ${angka_1}`)
}

else if (angka_1 < 0) {
    console.log (`Angka negatif, angka random = ${angka_1}`)
}

else {
    console.log (`Angka nol, angka random = ${angka_1}`)
}


console.log ("\n --- batas --- \n")




// Percabangan Lanjutan 2

var angka_2 = 10

if (angka_2 >= 8) {
    console.log (`Angka besar, angka 2 = ${angka_2}`)
}

else if (angka_2 >= 5) {
    console.log (`Angka setengah, angka 2 = ${angka_2}`)
}

else {
    console.log (`Angka nol, angka = ${angka_2}`)
}


console.log ("\n --- batas --- \n")




// Percabangan Prakiraan cuaca

var cuaca = "cerah"
var suhu = 32

if (cuaca == "cerah") {
    if (suhu > 30) {
        console.log (`Cuaca cerah, suhu = ${suhu} dan cuaca = ${cuaca}`)
    }

    else {
        console.log (`Jangan keluar rumah, cuaca = ${cuaca} dan suhu = ${suhu}`)
    }
}

else if (cuaca == "hujan") {
    if (suhu < 30) {
        console.log (`Bawa payung, suhu = ${suhu} dan cuaca = ${cuaca}`)
    }

    else {
        console.log (`Jangan keluar rumah, cuaca = ${cuaca} dan suhu = ${suhu}`)
    }
}

else if (cuaca == "berawan") {
    if (suhu < 30) {
        console.log (`Boleh keluar rumah nih, sambil jalan-jalan, suhu = ${suhu} dan cuaca = ${cuaca}`)
    }

    else {
        console.log (`Jangan keluar rumah, cuaca = ${cuaca} dan suhu = ${suhu}`)
    }
}

else {
    console.log (`Input tidak valid, suhu = ${suhu} dan cuaca = ${cuaca}`)
}


console.log ("\n --- batas --- \n")



// Percabangan Usia nonton film dan genre film

var genre = "keluarga"
var usia = 19

if (genre == "keluarga") {
    if (usia >= 2 && usia <= 20) {
        console.log (`Boleh nonton film, usia = ${usia} dan genre film = ${genre}`)
    }

    else {
        console.log (`Jangan nonton film, usia = ${usia} dan genre film = ${genre}`)
    }
}

else if (genre == "komedi") {
    if (usia >= 10 && usia <= 19) {
        console.log (`Boleh nonton film komedi, genre film = ${genre} dan usia = ${usia}`)
    }

    else {
        console.log (`Jangan nonton film komedi, usia = ${usia} dan genre film = ${genre}`)
    }
}

else if (genre == "romantis") {
    if (usia >= 18 && usia <= 25) {
        console.log (`Boleh nonton film, genre film = ${genre} dan usia = ${usia}`)
    }

    else {
        console.log (`Jangan nonton dulu, usia = ${usia} dan genre film = ${genre}`)
    }
}

else if (genre == "kartun") {
    if (usia >= 2 && usia <= 10) {
        console.log (`Boleh nonton film kartun, usia = ${usia} dan genre film = ${genre}`)
    }

    else {
        console.log (`Jangan nonton film kartun, usia = ${usia} dan genre film = ${genre}`)
    }
}

else if (genre == "action") {
    if (usia >= 20 && usia <= 30) {
        console.log (`Boleh nonton film, usia = ${usia} dan genre film = ${genre}`)
    }

    else {
        console.log (`Jangan nonton dulu, usia = ${usia} dan genre film = ${genre}`)
    }
}

else {
    console.log (`Input tidak valid, usia = ${usia} dan genre film = ${genre}`)
}


console.log ("\n --- batas --- \n")



// Percabangan jenjang pendidikan dan usia 

var pendidikan = "kuliah"
var usia = 19

if (pendidikan == "tk") {
    if (usia >= 4 && usia <= 6) {
        console.log (`masuk TK, usia = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan tk, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }
}

else if (pendidikan == "sd") {
    if (usia >= 6 && usia <= 12) {
        console.log (`masuk sd, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan sd, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }
}

else if (pendidikan == "smp") {
    if (usia >= 13 && usia <= 15) {
        console.log (`masuk smp, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan smp, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }
}

else if (pendidikan == "sma") {
    if (usia >= 16 && usia <= 18) {
        console.log (`masuk sma, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan sma, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }
}


else if (pendidikan == "kuliah") {
    if (usia >= 19 && usia <= 22) {
        console.log (`masuk kuliah, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan anak kuliahan, usia = ${usia} dan pendidikan = ${pendidikan}`)
    }
}

else {
    console.log (`Input tidak valid, usia = ${usia} dan pendidikan = ${pendidikan}`)
}


console.log ("\n --- batas --- \n")



// Percabangan Pemilihan usia manusia dan status nya

var usia = 19
var statuk = "remaja"

if (statuk == "bayi") {
    if (usia >= 1 && usia <= 2) {
        console.log (`usia bayi, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia bayi, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "balita") {
    if (usia >= 2 && usia <= 4) {
        console.log (`usia balita, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia balita, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "anak-anak") {
    if (usia >= 5 && usia <= 12) {
        console.log (`usia anak-anak, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia anak-anak, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "remaja") {
    if (usia >= 13 && usia <= 19) {
        console.log (`masuk usia remaja, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia remaja, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "dewasa") {
    if (usia >= 19 && usia <= 26) {
        console.log (`masuk usia dewasa, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia dewasa, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "dewasa matang") {
    if (usia >= 27 && usia <= 40) {
        console.log (`masuk usia dewasa matang, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia dewasa matang, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "tua") {
    if (usia >= 40 && usia <= 60) {
        console.log (`masuk usia tua, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan masuk usia tua, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "tua banget") {
    if (usia >= 60 && usia <= 70) {
        console.log (`masuk usia tua banget, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia tua banget, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else {
    console.log (`Input tidak valid, usia = ${usia} dan statuk = ${statuk}`)
}


console.log ("\n --- batas --- \n")



// For dasar 

for (a = 0; a < 20; a++) {
    console.log (`urutan ke - ${a}`)
}

console.log ("\n --- batas --- \n")



// For dasar 1

for (b = 1; b < 30; b++) {
    console.log (`urutan ke - ${b}`)
}

console.log ("\n --- batas --- \n")



// For dasar 3

for (y = 0; y < 70; y++) {
    console.log ("Aku suka sama Gracie JKT48 cantik dan imut")
}


console.log ("\n --- batas --- \n")



// For dasar 3

for (a = 0; a < 80; a++) {
    console.log ("Aku suka dan fans dengan JKT48")
}

console.log ("\n --- batas --- \n")