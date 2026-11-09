function run (a) {

    if (a >= 8) {
        console.log (`Besar, angka a = ${a}`)
    }

    else {
        console.log (`kecil, angka a = ${a}`)
    }
}

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


console.log ("\n --- batas --- \n")




function er (b) {

    if (b >= 8) {
        console.log (`besar, angka b = ${b}`)
    }

    else if (b >= 5) {
        console.log (`sedang, angka b = ${b}`)
    }

    else {
        console.log (`kecil, angka b = ${b}`)
    }
}

er (10)
er (9)
er (8)
er (7)
er (6)
er (5)
er (4)
er (3)
er (2)
er (1)


console.log ("\n ---- batas --- \n")




function er (y) {

    if (y >= 8) {
        console.log (`besar, angka y = ${y}`)
    }

    else if (y >= 5) {
        console.log (`sedang, angka y = ${y}`)
    }

    else {
        console.log (`kecil, angka y = ${y}`)
    }
}

er (10)
er (9)
er (8)
er (7)
er (6)
er (5)
er (4)
er (3)


console.log ("\n -- batas -- \n")




function der (u) {

    var cek = true

    if (u >= 8) {
        if (cek) {
            console.log (`besar, angka u = ${u}`)
        }

        else {
            console.log (`sedang, angka u = ${u}`)
        }
    }

    else {
        console.log (`kecil, angka u = ${u}`)
    }
}

der (10)
der (9)
der (8)
der (7)
der (6)
der (5)
der (4)
der (3)
der (2)
der (1)


console.log ("\n --- batas --- \n")





function der (o) {

    var cek = true

    if (o >= 8) {
        if (cek) {
            console.log (`besar, angka o = ${o}`)
        }

        else if (o >= 5) {
            console.log (`sedang, angka o = ${o}`)
        }
    }

    else {
        console.log (`kecil, angka o = ${o}`)
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
der (1)


console.log ("\n --- batas --- \n")



function fer (k) {

    var cek = true

    if (k >= 8) {
        if (cek) {
            console.log (`besar, angka k = ${k}`)
        }

        else if (k >= 5) {
            console.log (`sedang, angka k = ${k}`)
        }

        else {
            console.log (`kecil, angka k = ${k}`)
        }
    }

    else {
        console.log (`paling kecil, angka k = ${k}`)
    }
}

fer (10)
fer (9)
fer (8)
fer (6)
fer (5)
fer (4)
fer (2)
fer (1)


console.log ("\n --- batas --- \n")



function usia_jkt48 (i) {

    var cek = true

    if (i >= 15 && i <= 20) {
        if (cek) {
            console.log (`sudah cukup usia nya, usia = ${i}`)
        }

        else if (i > 20) {
            console.log (`sudah oke usia kamu, usia = ${i}`)
        }
    }

    else {
        console.log (`Paling kecil usia kamu, usia = ${i}`)
    }
}

usia_jkt48 (10)
usia_jkt48 (9)
usia_jkt48 (45)
usia_jkt48 (12)
usia_jkt48 (11)
usia_jkt48 (10)
usia_jkt48 (4)
usia_jkt48 (4)
usia_jkt48 (7)


console.log ("\n --- batas --- \n")




// Array dasar

var dasar = [
    "Gracie JKT48",
    "Michie JKT48",
    "Aralie JKT48",
    "Fritzy JKT48",
    "Ekin JKT48",
]

dasar.push ("Freya JKT48")
dasar.push ("Eli JKT48")
dasar.push ("Elin JKT48")

for (i = 0; i < dasar.length; i++) {
    console.log (dasar [i])
}