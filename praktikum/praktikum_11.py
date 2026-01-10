# Soal: Menentukan Kelayakan Magang

# Data siswa
umur = 17
rerata = 83.2
lulus_praktikum = True

# data awal
print("Data Siswa:")
print("Umur                    =", umur)
print("Rerata Nilai            =", rerata)
print("Lulus Semua Praktikum   =", lulus_praktikum)
print("-" * 40)

# Syarat:
# 1. Rerata minimal 83.0
# 2. Umur tidak lebih dari 21 tahun
# 3. Sudah lulus semua praktikum wajib

berhak_magang = (rerata >= 83.0) and (umur <= 21) and lulus_praktikum

# Cetak
print("Apakah siswa berhak mengikuti magang?")
print("Jawaban:", berhak_magang)
