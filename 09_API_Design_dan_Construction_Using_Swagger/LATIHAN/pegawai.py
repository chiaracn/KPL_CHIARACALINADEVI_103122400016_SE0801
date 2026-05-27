from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Pegawai(ABC): #class Pegawai(ABC) untuk membuat kelas abstrak yang tidak bisa diinstansiasi langsung
    def __init__(self, idPegawai, nama, alamat, noTelepon):
        self.idPegawai = idPegawai
        self.nama = nama
        self.alamat = alamat
        self.noTelepon = noTelepon
        self.statusAktif = True

    def tampilkanData(self):
        print("=== DATA PEGAWAI ===")
        print("ID           :", self.idPegawai)
        print("Nama         :", self.nama)
        print("Alamat       :", self.alamat)
        print("No Telepon   :", self.noTelepon)
        print("Status       :", "Aktif" if self.statusAktif else "Nonaktif")

    @abstractmethod
    def hitungGaji(self):
        pass

    def ubahStatus(self, status):
        self.statusAktif = status


# =========================
# KELAS TURUNAN
# =========================

class Dosen(Pegawai):
    def __init__(self, idPegawai, nama, alamat, noTelepon, nidn):
        super().__init__(idPegawai, nama, alamat, noTelepon)
        self.nidn = nidn
        self.bidangKeahlian = ""
        self.jumlahSKS = 0

    def tampilkanData(self):
        super().tampilkanData()
        print("NIDN         :", self.nidn)
        print("SKS          :", self.jumlahSKS)

    def hitungGaji(self):
        return 5000000 + (self.jumlahSKS * 100000)


class StaffAdministrasi(Pegawai):
    def __init__(self, idPegawai, nama, alamat, noTelepon, bagian):
        super().__init__(idPegawai, nama, alamat, noTelepon)
        self.bagian = bagian
        self.jamKerja = 0

    def tampilkanData(self):
        super().tampilkanData()
        print("Bagian       :", self.bagian)
        print("Jam Kerja    :", self.jamKerja)

    def hitungGaji(self):
        return 3000000 + (self.jamKerja * 50000)


class TenagaKependidikan(Pegawai):
    def __init__(self, idPegawai, nama, alamat, noTelepon, unitKerja):
        super().__init__(idPegawai, nama, alamat, noTelepon)
        self.unitKerja = unitKerja
        self.shiftKerja = ""

    def tampilkanData(self):
        super().tampilkanData()
        print("Unit Kerja   :", self.unitKerja)


class Laboran(TenagaKependidikan):
    def __init__(self, idPegawai, nama, alamat, noTelepon, unitKerja):
        super().__init__(idPegawai, nama, alamat, noTelepon, unitKerja)
        self.namaLaboratorium = ""
        self.jumlahPeralatan = 0

    def tampilkanData(self):
        super().tampilkanData()
        print("Laboratorium :", self.namaLaboratorium)
        print("Peralatan    :", self.jumlahPeralatan)

    def hitungGaji(self):
        return 3000000


class Pustakawan(TenagaKependidikan):
    def __init__(self, idPegawai, nama, alamat, noTelepon, unitKerja):
        super().__init__(idPegawai, nama, alamat, noTelepon, unitKerja)
        self.kodePerpustakaan = ""
        self.jumlahBukuDikelola = 0

    def tampilkanData(self):
        super().tampilkanData()
        print("Kode Perpus  :", self.kodePerpustakaan)
        print("Jumlah Buku  :", self.jumlahBukuDikelola)

    def hitungGaji(self):
        return 2800000


# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":

    # DOSEN
    d = Dosen("P001", "Rachel", "Jakarta", "08123456789", "12345")
    d.jumlahSKS = 10
    d.tampilkanData()
    print("Gaji:", d.hitungGaji())
    print()

    # STAFF
    s = StaffAdministrasi("P002", "Chiara", "Bandung", "08234567890", "Kaprodi")
    s.jamKerja = 25
    s.tampilkanData()
    print("Gaji:", s.hitungGaji())
    print()

    # LABORAN
    l = Laboran("P003", "Ghina", "Surabaya", "08345678901", "Lab Komputer")
    l.namaLaboratorium = "Lab AI"
    l.jumlahPeralatan = 30
    l.tampilkanData()
    print("Gaji:", l.hitungGaji())
    print()

    # PUSTAKAWAN
    p = Pustakawan("P004", "Shofi", "Yogyakarta", "08456789012", "Perpustakaan")
    p.kodePerpustakaan = "PERP01"
    p.jumlahBukuDikelola = 8000
    p.tampilkanData()
    print("Gaji:", p.hitungGaji())