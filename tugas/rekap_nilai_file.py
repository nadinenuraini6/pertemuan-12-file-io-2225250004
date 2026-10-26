def baca_data(nama_file):
    """
    Membaca data dari file input, membersihkan spasi, 
    melewati baris kosong, dan menangani ValueError per baris.
    """
    data = []
    try:
        # Membuka file dengan mode r dan encoding UTF-8
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris_bersih = baris.strip()
                
                # Mengabaikan/melewati baris yang kosong
                if not baris_bersih:
                    continue
                
                try:
                    # Memisahkan format NIM, nilai
                    nim, teks_nilai = baris_bersih.split(",")
                    nilai = float(teks_nilai)
                    
                    # Menyimpan data valid ke dalam list tuple
                    data.append((nim.strip(), nilai))
                    
                except ValueError:
                    # Menangani error nilai non-numerik atau format kolom salah per baris
                    print(f"[Peringatan] Baris {nomor} tidak valid dan dilewati: '{baris_bersih}'")
                    
    except FileNotFoundError:
        # Menangani jika file input tidak tersedia agar program tidak crash
        print(f"[Error] File tidak ditemukan: '{nama_file}'")
        
    return data


def tulis_rekap(nama_file, data):
    """
    Menghitung jumlah data valid, rata-rata, nilai min, nilai max,
    jumlah kelulusan (nilai >= 60), lalu menulis ringkasannya ke file output.
    """
    if not data:
        print("[Informasi] Tidak ada data valid untuk direkap.")
        return
        
    # Mengambil list nilai saja dari data tuple
    list_nilai = [item[1] for item in data]
    
    # Menghitung statistik data
    jumlah_data = len(list_nilai)
    rata_rata = sum(list_nilai) / jumlah_data
    nilai_min = min(list_nilai)
    nilai_max = max(list_nilai)
    
    # Menghitung jumlah mahasiswa yang lulus (Nilai minimal 60 dianggap lulus)
    jumlah_lulus = sum(1 for x in list_nilai if x >= 60)
    
    try:
        # Menulis ringkasan statistik ke file dengan mode w dan encoding UTF-8
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(f"Jumlah data valid: {jumlah_data}\n")
            file.write(f"Rata-rata: {rata_rata:.2f}\n")
            file.write(f"Minimum: {nilai_min:.2f}\n")
            file.write(f"Maksimum: {nilai_max:.2f}\n")
            file.write(f"Jumlah lulus: {jumlah_lulus}\n")
            
        print(f"[Sukses] Ringkasan rekapitulasi berhasil ditulis ke '{nama_file}'")
        
    except IOError:
        print(f"[Error] Gagal menulis ke file output '{nama_file}'")


# Alur Utama Program
if __name__ == "__main__":
    # Menggunakan path relatif sesuai struktur direktori proyek
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"
    
    print("=== Memulai Proses Rekapitulasi Nilai ===")
    
    # 1. Jalankan fungsi membaca dan memvalidasi data
    data_valid = baca_data(input_file)
    
    # 2. Jalankan fungsi menulis rekap jika data valid berhasil ditemukan
    if data_valid:
        tulis_rekap(output_file, data_valid)
        
        # Menampilkan ringkasan ringkas proses pada terminal
        print("\n--- Ringkasan Proses di Terminal ---")
        print(f"Total baris valid yang diproses: {len(data_valid)} baris.")
    else:
        print("\n[Gagal] Proses rekapitulasi dihentikan karena tidak ada data yang valid.")
