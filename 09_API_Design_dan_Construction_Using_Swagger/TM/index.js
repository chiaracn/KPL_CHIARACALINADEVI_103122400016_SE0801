import express from "express";

const app = express();
app.use(express.json());

const PORT = 3000;

// fungsi buat angka tetap dari nama
function generateNumber(nama) {
    let hash = 0;

    for (let i = 0; i < nama.length; i++) {
        hash += nama.charCodeAt(i);
    }

    // range 1 - 100
    return (hash % 100) + 1;
}

app.post("/", (req, res) => {
    const { nama, tebakan } = req.body;

    if (!nama || !tebakan) {
        return res.status(400).json({
            jawaban: "nama dan tebakan wajib diisi"
        });
    }

    const angkaBenar = generateNumber(nama);

    if (tebakan === angkaBenar) {
        return res.json({
            jawaban: `Benar sekali! Tebakannya adalah ${angkaBenar}.`
        });
    } else if (tebakan > angkaBenar) {
        return res.json({
            jawaban: "Tebakanmu terlalu tinggi!"
        });
    } else {
        return res.json({
            jawaban: "Tebakanmu terlalu rendah!"
        });
    }
});

app.listen(PORT, () => {
    console.log(`Server jalan di http://localhost:${PORT}`);
});