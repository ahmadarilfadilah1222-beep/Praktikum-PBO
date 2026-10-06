import os

class Pasien:
 # Atribut kelas
    nama_klinik = "Smart Clinic"
    total_pasien = 0
    status_klinik = "Buka"

    def __init__(self, id_pasien, nama, umur, alamat, no_telepon):
     # Atribut instance
        self.id_pasien = id_pasien
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.__no_telepon = no_telepon

        Pasien.total_pasien += 1

    # Instance method
    def tampilkan_data(self):
        print(f"ID Pasien   : {self.id_pasien}")
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur} tahun")
        print(f"Alamat      : {self.alamat}")
        print(f"No. Telepon : {self.__no_telepon}")

    # Getter
    @property
    def no_telepon(self):
        return self.__no_telepon

    # Setter
    @no_telepon.setter
    def no_telepon(self, nomor):
        if not nomor:
            raise ValueError("Nomor telepon tidak boleh kosong.")

        if not nomor.isdigit():
            raise ValueError("Nomor telepon hanya boleh berisi angka.")

        if len(nomor) < 10 or len(nomor) > 13:
            raise ValueError("Nomor telepon harus 10-13 angka.")

        self.__no_telepon = nomor

    # Class method
    @classmethod
    def tambah_pasien(cls, id_pasien, nama, umur, alamat, no_telepon):
        return cls(id_pasien, nama, umur, alamat, no_telepon)

    # Static method
    @staticmethod
    def validasi_umur(umur):
        return 0 < umur <= 100


class Dokter:
 # Atribut kelas
    nama_klinik = "Smart Clinic"
    total_dokter = 0
    jam_operasional = "08.00 - 21.00"

    def __init__(self, id_dokter, nama, spesialisasi, jadwal):
    # Atribut instance
        self.id_dokter = id_dokter
        self.nama = nama
        self.spesialisasi = spesialisasi
        self.jadwal = jadwal
        self.__no_izin = "SIP-" + id_dokter

        Dokter.total_dokter += 1

    # Instance method
    def tampilkan_data(self):
        print(f"ID Dokter    : {self.id_dokter}")
        print(f"Nama         : {self.nama}")
        print(f"Spesialisasi : {self.spesialisasi}")
        print(f"Jadwal       : {self.jadwal}")
        print(f"No. Izin     : {self.__no_izin}")

    # Getter
    @property
    def no_izin(self):
        return self.__no_izin

    # Setter
    @no_izin.setter
    def no_izin(self, nomor):
        if not nomor:
            raise ValueError("Nomor izin tidak boleh kosong.")

        if not nomor.startswith("SIP-"):
            raise ValueError("Nomor izin harus diawali dengan SIP-.")

        self.__no_izin = nomor

    # Class method
    @classmethod
    def ubah_jam_operasional(cls, jam_baru):
        if not jam_baru:
            raise ValueError("Jam operasional tidak boleh kosong.")

        cls.jam_operasional = jam_baru

    # Static method
    @staticmethod
    def validasi_jadwal(jadwal):
        return bool(jadwal.strip())


class Pemeriksaan:
# Atribut kelas
    nama_klinik = "Smart Clinic"
    total_pemeriksaan = 0
    biaya_konsultasi_dasar = 100000

    def __init__(
        self,
        id_pemeriksaan,
        pasien,
        dokter,
        keluhan,
        diagnosa,
        biaya
    ):
        # Atribut instance
        self.id_pemeriksaan = id_pemeriksaan
        self.pasien = pasien
        self.dokter = dokter
        self.keluhan = keluhan
        self.diagnosa = diagnosa
        self.__biaya = biaya

        Pemeriksaan.total_pemeriksaan += 1

    # Instance method
    def tampilkan_pemeriksaan(self):
        print(f"ID Pemeriksaan : {self.id_pemeriksaan}")
        print(f"Pasien         : {self.pasien.nama}")
        print(f"Dokter         : {self.dokter.nama}")
        print(f"Keluhan        : {self.keluhan}")
        print(f"Diagnosa       : {self.diagnosa}")
        print(f"Biaya          : Rp{self.__biaya:,}")

    # Getter
    @property
    def biaya(self):
        return self.__biaya

    # Setter
    @biaya.setter
    def biaya(self, nilai):
        if nilai < 0:
            raise ValueError("Biaya tidak boleh negatif.")

        self.__biaya = nilai

    # Class method
    @classmethod
    def ubah_biaya_konsultasi(cls, biaya_baru):
        if biaya_baru < 0:
            raise ValueError("Biaya tidak boleh negatif.")

        cls.biaya_konsultasi_dasar = biaya_baru

    # Static method
    @staticmethod
    def hitung_total(biaya_pemeriksaan, biaya_obat):
        if biaya_pemeriksaan < 0 or biaya_obat < 0:
            raise ValueError("Biaya tidak boleh negatif.")

        return biaya_pemeriksaan + biaya_obat


# Data yg sdh ada
daftar_pasien = [
    Pasien("P001", "Ahmad Aril Fadillah.B", 20, "Paser", "081234567890"),
    Pasien("P002", "Bintang ", 19, "Samarinda", "082345678901")
]

daftar_dokter = [
    Dokter("D001", "dr. Agus bijer", "Dokter Umum", "08.00 - 14.00"),
    Dokter("D002", "dr. Curukuk", "Dokter Gigi", "14.00 - 21.00")
]

daftar_pemeriksaan = [
    Pemeriksaan(
        "PM001",
        daftar_pasien[0],
        daftar_dokter[0],
        "Demam dan sakit kepala",
        "Flu",
        150000
    ),
    Pemeriksaan(
        "PM002",
        daftar_pasien[1],
        daftar_dokter[1],
        "Sakit gigi",
        "Gigi berlubang",
        200000
    )
]

# Fungsi pembersih terminal saat perpindahan saat memilih di menu
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def garis():
    print("=" * 60)


def pause():
    input("\nTekan ENTER untuk melanjutkan...")
    bersihkan_layar()


# CRUD Pasien

def tambah_pasien():
    print("====================")
    print("\n TAMBAH PASIEN ")
    print("====================")

    id_pasien = input("ID Pasien     : ")

    for pasien in daftar_pasien:
        if pasien.id_pasien == id_pasien:
            print("ID pasien sudah digunakan.")
            return

    nama = input("Nama          : ")

    try:
        umur = int(input("Umur          : "))

        if not Pasien.validasi_umur(umur):
            print("Umur tidak valid.")
            return

    except ValueError:
        print("Umur harus berupa angka.")
        return

    alamat = input("Alamat        : ")
    no_telepon = input("No. Telepon   : ")

    try:
        pasien_baru = Pasien.tambah_pasien(
            id_pasien,
            nama,
            umur,
            alamat,
            no_telepon
        )

        daftar_pasien.append(pasien_baru)

        print("\nPasien berhasil ditambahkan.")

    except ValueError as e:
        print("Gagal menambahkan pasien:", e)


def lihat_pasien():
    print("====================")
    print("\nDAFTAR PASIEN ")
    print("====================")

    if not daftar_pasien:
        print("Belum ada data pasien.")
        return

    for pasien in daftar_pasien:
        print("-" * 60)
        pasien.tampilkan_data()


def ubah_pasien():
    print("====================")
    print("\n UBAH DATA PASIEN ")
    print("====================")

    id_pasien = input("Masukkan ID pasien: ")

    for pasien in daftar_pasien:
        if pasien.id_pasien == id_pasien:

            print("\nData saat ini:")
            pasien.tampilkan_data()

            print("\nMasukkan data baru.")
            nama = input("Nama baru        : ")
            alamat = input("Alamat baru      : ")
            nomor = input("No. Telepon baru : ")

            if nama:
                pasien.nama = nama

            if alamat:
                pasien.alamat = alamat

            try:
                pasien.no_telepon = nomor
            except ValueError as e:
                print("Gagal mengubah nomor telepon:", e)
                return

            print("\nData pasien berhasil diubah.")
            return

    print("Pasien tidak ditemukan.")


def hapus_pasien():
    print("====================")
    print("\n HAPUS DATA PASIEN ")
    print("====================")

    id_pasien = input("Masukkan ID pasien: ")

    for pasien in daftar_pasien:
        if pasien.id_pasien == id_pasien:

            konfirmasi = input(
                f"Hapus pasien {pasien.nama}? (y/n): "
            ).lower()

            if konfirmasi == "y":
                daftar_pasien.remove(pasien)
                Pasien.total_pasien -= 1

                print("Data pasien berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

            return

    print("Pasien tidak ditemukan.")


def menu_pasien():
    while True:
        garis()
        print("              KELOLA DATA PASIEN")
        garis()
        print("1. Tambah Pasien")
        print("2. Lihat Pasien")
        print("3. Ubah Pasien")
        print("4. Hapus Pasien")
        print("0. Kembali")

        pilihan = input("\nPilih menu: ")
        bersihkan_layar()

        if pilihan == "1":
            tambah_pasien()
            pause()

        elif pilihan == "2":
            lihat_pasien()
            pause()

        elif pilihan == "3":
            ubah_pasien()
            pause()

        elif pilihan == "4":
            hapus_pasien()
            pause()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia.")


# CRUD DOKTER
def tambah_dokter():
    print("====================")
    print("\n TAMBAH DOKTER ")
    print("====================")

    id_dokter = input("ID Dokter    : ")

    for dokter in daftar_dokter:
        if dokter.id_dokter == id_dokter:
            print("ID dokter sudah digunakan.")
            return

    nama = input("Nama         : ")
    spesialisasi = input("Spesialisasi : ")
    jadwal = input("Jadwal       : ")

    if not Dokter.validasi_jadwal(jadwal):
        print("Jadwal tidak boleh kosong.")
        return

    dokter_baru = Dokter(
        id_dokter,
        nama,
        spesialisasi,
        jadwal
    )

    daftar_dokter.append(dokter_baru)

    print("\nDokter berhasil ditambahkan.")


def lihat_dokter():
    print("====================")
    print("\n DAFTAR DOKTER ")
    print("====================")

    if not daftar_dokter:
        print("Belum ada data dokter.")
        return

    for dokter in daftar_dokter:
        print("-" * 60)
        dokter.tampilkan_data()


def ubah_dokter():
    print("====================")
    print("\n UBAH DATA DOKTER ")
    print("====================")

    id_dokter = input("Masukkan ID dokter: ")

    for dokter in daftar_dokter:

        if dokter.id_dokter == id_dokter:

            print("\nData saat ini:")
            dokter.tampilkan_data()

            print("\nMasukkan data baru.")

            nama = input("Nama baru         : ")
            spesialisasi = input("Spesialisasi baru : ")
            jadwal = input("Jadwal baru       : ")

            if nama:
                dokter.nama = nama

            if spesialisasi:
                dokter.spesialisasi = spesialisasi

            if not Dokter.validasi_jadwal(jadwal):
                print("Jadwal tidak boleh kosong.")
                return

            dokter.jadwal = jadwal

            print("\nData dokter berhasil diubah.")
            return

    print("Dokter tidak ditemukan.")


def hapus_dokter():
    print("====================")
    print("\n HAPUS DATA DOKTER ")
    print("====================")

    id_dokter = input("Masukkan ID dokter: ")

    for dokter in daftar_dokter:

        if dokter.id_dokter == id_dokter:

            konfirmasi = input(
                f"Hapus dokter {dokter.nama}? (y/n): "
            ).lower()

            if konfirmasi == "y":
                daftar_dokter.remove(dokter)
                Dokter.total_dokter -= 1

                print("Data dokter berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

            return

    print("Dokter tidak ditemukan.")


def menu_dokter():
    while True:
        garis()
        print("              KELOLA DATA DOKTER")
        garis()
        print("1. Tambah Dokter")
        print("2. Lihat Dokter")
        print("3. Ubah Dokter")
        print("4. Hapus Dokter")
        print("0. Kembali")

        pilihan = input("\nPilih menu: ")
        bersihkan_layar()

        if pilihan == "1":
            tambah_dokter()
            pause()

        elif pilihan == "2":
            lihat_dokter()
            pause()

        elif pilihan == "3":
            ubah_dokter()
            pause()

        elif pilihan == "4":
            hapus_dokter()
            pause()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia.")


# CRUD PEMERIKSAAN
def pilih_pasien():
    print("====================")
    print("\n PILIH PASIEN ")
    print("====================")

    if not daftar_pasien:
        print("Belum ada pasien.")
        return None

    for pasien in daftar_pasien:
        print(
            f"{pasien.id_pasien} - "
            f"{pasien.nama}"
        )

    id_pasien = input("ID Pasien: ")

    for pasien in daftar_pasien:
        if pasien.id_pasien == id_pasien:
            return pasien

    print("Pasien tidak ditemukan.")
    return None


def pilih_dokter():
    print("====================")
    print("\n PILIH DOKTER ")
    print("====================")

    if not daftar_dokter:
        print("Belum ada dokter.")
        return None

    for dokter in daftar_dokter:
        print(
            f"{dokter.id_dokter} - "
            f"{dokter.nama} ({dokter.spesialisasi})"
        )

    id_dokter = input("ID Dokter: ")

    for dokter in daftar_dokter:
        if dokter.id_dokter == id_dokter:
            return dokter

    print("Dokter tidak ditemukan.")
    return None


def tambah_pemeriksaan():
    print("====================")
    print("\n TAMBAH PEMERIKSAAN ")

    id_pemeriksaan = input("ID Pemeriksaan: ")

    for pemeriksaan in daftar_pemeriksaan:
        if pemeriksaan.id_pemeriksaan == id_pemeriksaan:
            print("ID pemeriksaan sudah digunakan.")
            return

    pasien = pilih_pasien()

    if pasien is None:
        return

    dokter = pilih_dokter()

    if dokter is None:
        return

    keluhan = input("Keluhan        : ")
    diagnosa = input("Diagnosa       : ")

    try:
        biaya = int(input("Biaya          : "))

        if biaya < 0:
            print("Biaya tidak boleh negatif.")
            return

    except ValueError:
        print("Biaya harus berupa angka.")
        return

    pemeriksaan_baru = Pemeriksaan(
        id_pemeriksaan,
        pasien,
        dokter,
        keluhan,
        diagnosa,
        biaya
    )

    daftar_pemeriksaan.append(pemeriksaan_baru)

    print("\nData pemeriksaan berhasil ditambahkan.")


def lihat_pemeriksaan():
    print("====================")
    print("\n DAFTAR PEMERIKSAAN ")
    print("====================")

    if not daftar_pemeriksaan:
        print("Belum ada data pemeriksaan.")
        return

    for pemeriksaan in daftar_pemeriksaan:
        print("-" * 60)
        pemeriksaan.tampilkan_pemeriksaan()


def ubah_pemeriksaan():
    print("====================")
    print("\n UBAH DATA PEMERIKSAAN ")
    print("====================")

    id_pemeriksaan = input(
        "Masukkan ID pemeriksaan: "
    )

    for pemeriksaan in daftar_pemeriksaan:

        if pemeriksaan.id_pemeriksaan == id_pemeriksaan:

            print("\nData saat ini:")
            pemeriksaan.tampilkan_pemeriksaan()

            print("\nMasukkan data baru.")

            keluhan = input("Keluhan baru  : ")
            diagnosa = input("Diagnosa baru : ")

            if keluhan:
                pemeriksaan.keluhan = keluhan

            if diagnosa:
                pemeriksaan.diagnosa = diagnosa

            biaya = input("Biaya baru    : ")

            if biaya:

                try:
                    pemeriksaan.biaya = int(biaya)

                except ValueError as e:
                    print("Gagal mengubah biaya:", e)
                    return

            print("\nData pemeriksaan berhasil diubah.")
            return

    print("Pemeriksaan tidak ditemukan.")


def hapus_pemeriksaan():
    print("====================")
    print("\n HAPUS DATA PEMERIKSAAN ")
    print("====================")

    id_pemeriksaan = input(
        "Masukkan ID pemeriksaan: "
    )

    for pemeriksaan in daftar_pemeriksaan:

        if pemeriksaan.id_pemeriksaan == id_pemeriksaan:

            konfirmasi = input(
                "Hapus data pemeriksaan ini? (y/n): "
            ).lower()

            if konfirmasi == "y":

                daftar_pemeriksaan.remove(pemeriksaan)
                Pemeriksaan.total_pemeriksaan -= 1

                print(
                    "Data pemeriksaan berhasil dihapus."
                )

            else:
                print("Penghapusan dibatalkan.")

            return

    print("Pemeriksaan tidak ditemukan.")


def menu_pemeriksaan():
    while True:

        garis()
        print("           KELOLA DATA PEMERIKSAAN")
        garis()

        print("1. Tambah Pemeriksaan")
        print("2. Lihat Pemeriksaan")
        print("3. Ubah Pemeriksaan")
        print("4. Hapus Pemeriksaan")
        print("0. Kembali")

        pilihan = input("\nPilih menu: ")
        bersihkan_layar()

        if pilihan == "1":
            tambah_pemeriksaan()
            pause()

        elif pilihan == "2":
            lihat_pemeriksaan()
            pause()

        elif pilihan == "3":
            ubah_pemeriksaan()
            pause()

        elif pilihan == "4":
            hapus_pemeriksaan()
            pause()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia.")


# Informasi klinik
def informasi_klinik():
    garis()
    print("              INFORMASI KLINIK")
    garis()

    print(f"Nama Klinik       : {Pasien.nama_klinik}")
    print(f"Status Klinik     : {Pasien.status_klinik}")
    print(f"Jam Operasional   : {Dokter.jam_operasional}")
    print(f"Total Pasien      : {Pasien.total_pasien}")
    print(f"Total Dokter      : {Dokter.total_dokter}")
    print(
        f"Total Pemeriksaan : "
        f"{Pemeriksaan.total_pemeriksaan}"
    )
    print(
        f"Biaya Konsultasi  : "
        f"Rp{Pemeriksaan.biaya_konsultasi_dasar:,}"
    )


# Menu utama
def menu_utama():

    while True:

        print()
        garis()
        print("          SISTEM MANAJEMEN SMART CLINIC")
        print("             KLINIK KESEHATAN PREMIUM")
        garis()

        print("1. Kelola Data Pasien")
        print("2. Kelola Data Dokter")
        print("3. Kelola Data Pemeriksaan")
        print("4. Informasi Klinik")
        print("0. Keluar")

        pilihan = input("\nPilih menu: ")
        bersihkan_layar()

        if pilihan == "1":
            menu_pasien()
            bersihkan_layar()

        elif pilihan == "2":
            menu_dokter()
            bersihkan_layar()

        elif pilihan == "3":
            menu_pemeriksaan()
            bersihkan_layar()

        elif pilihan == "4":
            informasi_klinik()
            pause()

        elif pilihan == "0":
            bersihkan_layar()
            print("\nTerima kasih telah menggunakan Smart Clinic.")
            break

        else:
            print("\nPilihan tidak tersedia. Silakan coba lagi.")


# PENGUJIAN PROGRAM OOP
def pengujian_program():
    bersihkan_layar()
    garis()
    print("              PENGUJIAN PROGRAM OOP")
    garis()

    # Instance method
    print("====================")
    print("\n Instance Method ")
    print("====================")
    daftar_pasien[0].tampilkan_data()
    print()
    daftar_dokter[0].tampilkan_data()
    print()
    daftar_pemeriksaan[0].tampilkan_pemeriksaan()

    # Class method
    print("====================")
    print("\n Class Method ")
    print("====================")

    pasien_uji = Pasien.tambah_pasien(
        "P003",
        "Citra",
        20,
        "Samarinda",
        "083456789012"
    )
    print("Pasien berhasil dibuat melalui class method:")
    pasien_uji.tampilkan_data()

    Dokter.ubah_jam_operasional("08.00 - 22.00")
    print("\nJam operasional baru:", Dokter.jam_operasional)

    Pemeriksaan.ubah_biaya_konsultasi(120000)
    print(
        "Biaya konsultasi dasar baru:",
        f"Rp{Pemeriksaan.biaya_konsultasi_dasar:,}"
    )

    # Static method
    print("====================")
    print("\n Static Method ")
    print("====================")
    print("Validasi umur 21 :", Pasien.validasi_umur(21))
    print("Validasi umur 150:", Pasien.validasi_umur(150))
    print(
        "Validasi jadwal  :",
        Dokter.validasi_jadwal("08.00 - 14.00")
    )
    print(
        "Total biaya      :",
        f"Rp{Pemeriksaan.hitung_total(150000, 50000):,}"
    )

    # Getter
    print("====================")
    print("\n Getter ")
    print("====================")
    print("No. Telepon Pasien:",
          daftar_pasien[0].no_telepon)
    print("No. Izin Dokter   :",
          daftar_dokter[0].no_izin)
    print("Biaya Pemeriksaan :",
          f"Rp{daftar_pemeriksaan[0].biaya:,}")

    # Setter valid
    print("====================")
    print("\n Setter Valid ")
    print("====================")
    try:
        daftar_pasien[0].no_telepon = "089876543210"
        print("Setter berhasil.")
        print(
            "No. Telepon baru:",
            daftar_pasien[0].no_telepon
        )
    except ValueError as e:
        print("Gagal:", e)

    # Setter tidak valid
    print("====================")
    print("\n Setter Tidak Valid ")
    print("====================")

    try:
        daftar_pasien[0].no_telepon = "ABC123"
    except ValueError as e:
        print("Validasi berhasil:", e)

    print("\n")
    garis()
    print("              PENGUJIAN SELESAI")
    garis()
    pause()


# MENJALANKAN PROGRAM
pengujian_program()
menu_utama()