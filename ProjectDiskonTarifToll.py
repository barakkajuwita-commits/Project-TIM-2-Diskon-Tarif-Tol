#IDENTITAS MAHASISWA 
# Nama : Juwita (Kelas A - Bisnis Digital)
# Judul: Program Kalkulator Diskon Tarif Tol Otomatis Berdasarkan Golongan

# 1. BAGIAN INPUT (MENGUMPULKAN DATA) 
print("="*45)
print("           PROGRAM INPUT DATA TOL            ")
print("="*45)

print("Pilih Jenis Kendaraan:")
print("1. Golongan I (Sedan, Jip, Pick Up)")
print("2. Golongan II (Truk dengan 2 gandar)")
print("3. Golongan III (Truk dengan 3 gandar)")

pilihan = input("Masukkan pilihan (1/2/3): ")

# Menentukan tarif berdasarkan golongan
if pilihan == "1":
    jenis_kendaraan = "Golongan I"
    tarif_dasar = 10000
elif pilihan == "2":
    jenis_kendaraan = "Golongan II"
    tarif_dasar = 15000
elif pilihan == "3":
    jenis_kendaraan = "Golongan III"
    tarif_dasar = 20000
else:
    jenis_kendaraan = "Tidak Diketahui"
    tarif_dasar = 0

# Menanyakan status hari untuk menentukan diskon
hari = input("Apakah hari ini hari Libur? (ya/tidak): ")

# 2. BAGIAN LOGIKA (PENGAMBILAN KEPUTUSAN) 
if hari.lower() == "ya":
    persen_diskon = 0.20  # Diskon 20% jika hari libur
    status_waktu = "Hari Libur (Promo 20%)"
else:
    persen_diskon = 0.05  # Diskon 5% jika hari biasa
    status_waktu = "Hari Kerja (Promo 5%)"

# 3. PERHITUNGAN SEDERHANA (ARITMATIKA) 
potongan_harga = tarif_dasar * persen_diskon
total_bayar = tarif_dasar - potongan_harga

# 4. BAGIAN OUTPUT (STRUK PEMBAYARAN) 
print("\n" + "-"*45)
print("                STRUK E-TOLL                 ")
print("-"*45)
print(f"Jenis Kendaraan : {jenis_kendaraan}")
print(f"Tarif Dasar     : Rp {tarif_dasar:,.0f}")
print(f"Promo Tambahan  : {status_waktu}")
print(f"Total Potongan  : Rp {potongan_harga:,.0f}")
print("-" * 45)
print(f"TOTAL BAYAR     : Rp {total_bayar:,.0f}")
print(f"STATUS TRANSAKSI: BERHASIL")
print("-" * 45)
print("       TERIMA KASIH & HATI-HATI DI JALAN      ")
print("="*45)