// Error Handling

try {
    var y = 10 + 10
    console.log (y)
}

catch (Error) {
    console.log ("Error")
}

finally {
    console.log ("Selesai")
}

console.log ("\n --- batas --- \n")



// Error Handling 1

try {
    var t = 10 + d
    console.log (t)
}

catch (Error) {
    console.log ("error")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --h- \n")




// Error Handling 3

try {
    var k = 10 + m
    console.log (k)
}

catch (Error) {
    console.log ("Error")
}

finally {
    console.log ("Selesai")
}

console.log ("\n --- batas --- \n")



// Fungsi Error Handling

function er (a) {

    try {

        if (a < 0) {
            throw ("Gagal")
        }

        if (a >= 8) {
            console.log (`Besar, angka a = ${a}`)
        }

        else {
            console.log (`Kecil, angka a = ${a}`)
        }
    }

    catch (Error) {
        console.log (`Gak boleh minus, angka a = ${a}`)
    }
}

er (10)
er (9)
er (6)
er (4)
er (2)
er (-1)
er (-23)
er (-23)
er (56)
er (-12)
er (-45)
er (-56)


console.log ("\n --- batas --- \n")



// Fungsi dengan error handling

function pn (f) {

    try {
        if (a < 0) {
            throw ("Minus")
        }

        if (a >= 8) {
            console.log (`Besar, angka a = ${a}`)
        }

        else if (a >= 5) {
            console.log (`Sedang, angka a = ${a}`)
        }

        else {
            console.log (`Kecil, angka a = ${a}`)
        }
    }

    catch (Error) {
        console.log (`Gak boleh minus, angka a = ${a}`)
    }
}


pn (10)
pn (-3)
pn (-3)
pn (-2)
pn (1)
pn (3)
pn (5)
pn (6)
pn (-12)


console.log ("\n --- batas --- \n")



