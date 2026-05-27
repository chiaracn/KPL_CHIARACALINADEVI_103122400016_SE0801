function tambahPengitung(terkini, jumlah) {

    // validasi input harus angka
    if (typeof terkini !== "number" || typeof jumlah !== "number") {
        throw new Error("Input harus berupa angka");
    }

    return terkini + jumlah;
}

export { tambahPengitung };