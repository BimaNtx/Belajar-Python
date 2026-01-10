# Soal Praktikum 10: Gabungan Operator

# Nilai awal yang diberikan
nilai_matematika = 80
nilai_fisika = 70

# Menghitung nilai rata-rata
rata_rata = (nilai_matematika + nilai_fisika) / 2

# Menampilkan nilai-nilai
print("Nilai Matematika =", nilai_matematika)
print("Nilai Fisika     =", nilai_fisika)
print("Rata-rata        =", rata_rata)
print("-" * 35)

# Ekspresi logika:
# 1. Rata-rata minimal 75
# 2. Nilai matematika lebih besar dari fisika

hasil = (rata_rata >= 75) and (nilai_matematika > nilai_fisika)

# Menampilkan hasil evaluasi logika
print("Apakah memenuhi syarat kelulusan?")
print("Jawaban:", hasil)
