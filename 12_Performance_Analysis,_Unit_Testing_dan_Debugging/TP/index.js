function main() {
    const data = [
        "123",
        456,
        "hello",
        78.9,
        true
    ];

    for (let i = 0; i < data.length; i++) {
        const result = processData(data[i]);
        console.log(`Item ${i + 1}: ${data[i]} -> ${result}`);
    }
}

function processData(data) {

    // Jika tipe data string
    if (typeof data === "string") {

        // cek apakah string angka
        if (!isNaN(data)) {
            return `Number: ${Number(data) * 2}`;
        }

        // string biasa
        return `Teks: ${data.toLowerCase()} (panjangnya: ${data.length})`;
    }

    // Jika tipe data number
    if (typeof data === "number") {
        return `Number: ${data * 2}`;
    }

    // Jika tipe data boolean
    if (typeof data === "boolean") {
        return `Boolean: ${data}`;
    }

    // Selain itu
    return "Tipe data tidak dikenali";
}

main();