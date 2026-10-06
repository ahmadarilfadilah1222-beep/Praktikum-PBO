# SISTEM MANAJEMEN SMART CLINIC
             KLINIK KESEHATAN PREMIUM - Program OOP Python

## Deskripsi
Program ini adalah sistem sederhana untuk mengelola data pasien, dokter, dan pemeriksaan pada Smart Clinic. Program dibuat menggunakan pendekatan Object-Oriented Programming (OOP) sesuai materi Class & Object, Atribut & Method, serta Encapsulation & Property.

## Class yang Digunakan

### 1. Class Pasien
Digunakan untuk menyimpan dan mengelola data pasien.

- Atribut kelas: `nama_klinik`, `total_pasien`, `status_klinik`
- Atribut instance: `id_pasien`, `nama`, `umur`, `alamat`, `__no_telepon`
- Instance method: `tampilkan_data()`
- Class method: `tambah_pasien()`
- Static method: `validasi_umur()`
- Property: `no_telepon` sebagai getter dan setter

### 2. Class Dokter
Digunakan untuk menyimpan dan mengelola data dokter.

- Atribut kelas: `nama_klinik`, `total_dokter`, `jam_operasional`
- Atribut instance: `id_dokter`, `nama`, `spesialisasi`, `jadwal`, `__no_izin`
- Instance method: `tampilkan_data()`
- Class method: `ubah_jam_operasional()`
- Static method: `validasi_jadwal()`
- Property: `no_izin` sebagai getter dan setter

### 3. Class Pemeriksaan
Digunakan untuk menyimpan data pemeriksaan pasien.

- Atribut kelas: `nama_klinik`, `total_pemeriksaan`, `biaya_konsultasi_dasar`
- Atribut instance: `id_pemeriksaan`, `pasien`, `dokter`, `keluhan`, `diagnosa`, `__biaya`
- Instance method: `tampilkan_pemeriksaan()`
- Class method: `ubah_biaya_konsultasi()`
- Static method: `hitung_total()`
- Property: `biaya` sebagai getter dan setter

## Encapsulation dan Validasi
Program menggunakan atribut private dengan awalan `__`. Atribut private diakses melalui `@property` dan diperbarui melalui setter.

Contoh validasi:
- Nomor telepon hanya boleh berisi angka.
- Nomor telepon harus terdiri dari 10-13 angka.
- Nomor izin dokter harus diawali `SIP-`.
- Biaya tidak boleh bernilai negatif.
- Umur harus berada pada rentang yang ditentukan.

## Pengujian Program
Pada bagian akhir program terdapat pengujian:
1. Instance method.
2. Class method.
3. Static method.
4. Getter.
5. Setter dengan data valid.
6. Setter dengan data tidak valid.

Program juga memiliki minimal dua objek awal untuk masing-masing class:
- 2 objek Pasien.
- 2 objek Dokter.
- 2 objek Pemeriksaan.

## Cara Menjalankan
1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder program.
3. Jalankan:

```bash
python posttest1_2509106119_AhmadArilFadillah.B.py
```

Setelah pengujian OOP selesai, program masuk ke menu utama Smart Clinic yang menyediakan pengelolaan data pasien, dokter, pemeriksaan, dan informasi klinik.
