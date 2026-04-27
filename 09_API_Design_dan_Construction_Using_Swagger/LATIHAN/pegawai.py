from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Pegawai(ABC): #abstractclass
    def __init__(self, idPegawai, nama):
        self.idPegawai = idPegawai
        self.nama = nama
        self.alamat = ""
        self.noTelepon = ""
        self.statusAktif = True

    def tampilkanData(self): #method biasa
        print(f"ID: {self.idPegawai}, Nama: {self.nama}")

    @abstractmethod
    def hitungGaji(self): #method abstract
        pass

    def ubahStatus(self, status):
        self.statusAktif = status


# KELAS BIASA
class Dosen(Pegawai): #kelas dosen yang merupakan turunan dari kelas pegawai
    def __init__(self, idPegawai, nama, nidn):
        super().__init__(idPegawai, nama)
        self.nidn = nidn
        self.bidangKeahlian = ""
        self.jumlahSKS = 0

    def mengajar(self, mataKuliah):
        print(f"{self.nama} mengajar {mataKuliah}")

    def membimbingMahasiswa(self, namaMahasiswa):
        print(f"{self.nama} membimbing {namaMahasiswa}")

    def hitungGaji(self):
        return 5000000 + (self.jumlahSKS * 100000)


class StaffAdministrasi(Pegawai): #kelas staff administrasi yang merupakan turunan dari kelas pegawai
    def __init__(self, idPegawai, nama, bagian):
        super().__init__(idPegawai, nama)
        self.bagian = bagian
        self.jamKerja = 0

    def kelolaSurat(self):
        print("Mengelola surat")

    def inputDataAkademik(self):
        print("Input data akademik")

    def hitungGaji(self):
        return 3000000 + (self.jamKerja * 50000)


class TenagaKependidikan(Pegawai): #kelas tenaga kependidikan yang merupakan turunan dari kelas pegawai, parent class untuk laboran dan pustakawan
    def __init__(self, idPegawai, nama, unitKerja):
        super().__init__(idPegawai, nama)
        self.unitKerja = unitKerja
        self.shiftKerja = ""

    def mendukungOperasional(self):
        print("Mendukung operasional")

    def membuatLaporanKerja(self):
        print("Membuat laporan kerja")

    def hitungGaji(self):
        return 2500000


class Laboran(TenagaKependidikan):#kelas laboran yang merupakan turunan dari kelas tenaga kependidikan
    def __init__(self, idPegawai, nama, unitKerja):
        super().__init__(idPegawai, nama, unitKerja)
        self.namaLaboratorium = ""
        self.jumlahPeralatan = 0

    def menyiapkanPraktikum(self):
        print("Menyiapkan praktikum")

    def mengecekAlatLab(self):
        print("Mengecek alat lab")

    def hitungGaji(self):
        return 3000000


class Pustakawan(TenagaKependidikan):#kelas pustakawan yang merupakan turunan dari kelas tenaga kependidikan
    def __init__(self, idPegawai, nama, unitKerja):
        super().__init__(idPegawai, nama, unitKerja)
        self.kodePerpustakaan = ""
        self.jumlahBukuDikelola = 0

    def mengelolaPeminjamanBuku(self):
        print("Mengelola peminjaman buku")

    def mengaturKatalogBuku(self):
        print("Mengatur katalog buku")

    def hitungGaji(self):
        return 2800000


# CONTOH PEMAKAIAN
if __name__ == "__main__":
    d = Dosen("P001", "Rachel", "12345")
    d.jumlahSKS = 10
    d.tampilkanData()
    print("Gaji:", d.hitungGaji())

    s = StaffAdministrasi("P002", "Chiara", "Kaprodi")
    s.jamKerja = 25
    s.tampilkanData()
    print("Gaji Staff:", s.hitungGaji())
    
    l = Laboran("P003", "Ghina", "Lab Komputer")
    l.jumlahPeralatan = 30
    l.tampilkanData()
    print("Gaji Laboran:", l.hitungGaji())
    
    p = Pustakawan("P004", "Shofi", "Perpustakaan")
    p.jumlahBukuDikelola = 8000
    p.tampilkanData()
    print("Gaji Pustakawan:", p.hitungGaji())

