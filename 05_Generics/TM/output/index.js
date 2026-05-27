/**
 * Mengubah angka menjadi "Fizz", "Buzz", "FizzBuzz", atau angka itu sendiri
 * @param {number} value - bilangan bulat
 * @returns {string|number} hasil konversi
 */
function zzzzOrNum(value) {
    if (value % 3 === 0 && value % 5 === 0) {
        return "FizzBuzz";
    } else if (value % 3 === 0) {
        return "Fizz";
    } else if (value % 5 === 0) {
        return "Buzz";
    } else {
        return value;
    }
}

/**
 * Mengubah array angka menjadi hasil FizzBuzz
 * @param {number[]} sequence - array berisi bilangan bulat
 * @returns {(string|number)[]} array hasil fizzbuzz
 */
function fizzBuzz(sequence) {
    const newSequence = sequence.map((e) => zzzzOrNum(e));
    return newSequence;
}

module.exports = {
    fizzBuzz: fizzBuzz,
    zzzzOrNum: zzzzOrNum,
};