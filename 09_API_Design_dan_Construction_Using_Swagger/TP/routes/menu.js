const express = require('express');
const router = express.Router();

/**
 * @swagger
 * /menu:
 *   get:
 *     summary: Ambil semua kategori menu
 *     description: Menampilkan daftar semua kategori menu yang tersedia
 *     responses:
 *       200:
 *         description: Daftar kategori berhasil diambil
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 kategori_tersedia:
 *                   type: array
 *                   items:
 *                     type: string
 *                   example: ["bakmi", "rames"]
 */

router.get('/', (req, res) => {
    const kategori = ["bakmi", "rames"];

    res.status(200).json({
        kategori_tersedia: kategori
    });
});

module.exports = router;