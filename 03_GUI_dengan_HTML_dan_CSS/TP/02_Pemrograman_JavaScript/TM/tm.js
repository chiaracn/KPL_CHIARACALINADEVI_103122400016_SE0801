function fizzBuzz(arr) {
    let hasil = "";

    for (let i = 0; i < arr.length; i++) {
        let angka = arr[i];

        if (angka % 14 === 0) {
            hasil += "FizzBuzz ";
        } else if (angka % 2 === 0) {
            hasil += "Fizz ";
        } else if (angka % 7 === 0) {
            hasil += "Buzz ";
        } else {
            hasil += angka + " ";
        }
    }

    return hasil.trim();
}

const input = [3, 10, 14, 21, 28, 31, 42];

const output = fizzBuzz(input);

console.log(output);