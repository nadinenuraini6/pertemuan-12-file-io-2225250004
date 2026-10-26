# Pertemuan 12 File I/O dan Error Handling

Nama: [Nadine Nur'Aini]
NIM: 2225250004
Kelas: [3B]

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM, nilai

## Cara Menjalankan
```bash
python tugas/rekap_nilai_file.py
```

## Error yang Ditangani
1. **FileNotFoundError**: Terjadi jika file input `data/nilai.txt` tidak tersedia di direktori kerja. Ditangani dengan memberikan pesan informatif agar program tidak berhenti mendadak (*crash*).
2. **ValueError**: Terjadi jika data nilai pada baris file input bukan berupa angka (seperti teks `abc`) atau format kolom salah. Ditangani per baris sehingga baris yang salah dilewati dan baris valid lainnya tetap diproses.

## Test Case

| Kasus | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Normal** | Semua baris data valid | Semua record diproses dan hasil rekap statistik benar. | File `hasil_rekap.txt` dibuat dengan nilai rata-rata, min, max, dan jumlah lulus yang akurat. | **Lolos** |
| **File Hilang**| File `nilai.txt` tidak tersedia | Pesan file tidak ditemukan muncul; program tidak *crash*. | Muncul pesan `[Error] File tidak ditemukan` di terminal dengan aman. | **Lolos** |
| **Nilai Invalid**| Terdapat baris berisi teks alfabet seperti `A004, abc` | Baris invalid dilewati/dilaporkan; record lain tetap diproses. | Baris bermasalah dilaporkan sebagai peringatan di terminal, data valid lainnya sukses dihitung. | **Lolos** |
| **Baris Kosong**| Ada baris kosong di dalam file | Baris kosong langsung dilewati tanpa membuat error. | Baris kosong diabaikan dengan sukses dan statistik akhir tetap akurat. | **Lolos** |
| **Batas Lulus** | Nilai mahasiswa tepat 60 | Dihitung sebagai kategori lulus. | Mahasiswa dengan nilai 60 sukses terhitung ke dalam jumlah kelulusan. | **Lolos** |

## Refleksi
Salah satu error penting yang ditemukan dan berhasil ditangani adalah **ValueError** ketika memproses baris data yang formatnya tidak valid (seperti baris berisi string alfabet `abc` atau baris kosong). 

Jika tidak ditangani menggunakan struktur *try-except* yang diletakkan **di dalam perulangan baris**, kegagalan konversi fungsi `float()` akan langsung menghentikan seluruh eksekusi program secara kasar. Akibatnya, baris-baris valid setelahnya tidak akan pernah sempat ikut diproses. Dengan menerapkan penanganan error secara spesifik per baris, program menjadi jauh lebih tangguh karena mampu mengisolasi kesalahan pada baris yang rusak saja, melaporkannya ke terminal untuk diperiksa, dan langsung melanjutkan pemrosesan baris berharga berikutnya hingga selesai.
