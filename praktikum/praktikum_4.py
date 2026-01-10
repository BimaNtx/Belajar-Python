# Data diri dengan tipe yang tepat
nama = "Dimas Setiawan"       # teks, jadi pakai tanda kutip
umur = int("21")              # konversi dari string ke integer agar bisa dihitung
berat = float("65.4")         # konversi ke float agar bisa dihitung dalam rumus BMI
tinggi = 170                  # dalam cm
status_siswa = True           # gunakan boolean True (tanpa tanda kutip)

# Menghitung BMI
# Rumus BMI: berat (kg) / (tinggi (m))^2
bmi = berat / ((tinggi / 100) ** 2)   # tinggi diubah ke meter (dengan dibagi 100)

# Penjelasan tambahan (tidak dieksekusi, hanya sebagai catatan / dokumentasi)
"""
BMI adalah singkatan dari Indeks Massa Tubuh (Body Mass Index).
BMI adalah ukuran yang digunakan untuk menentukan apakah berat badan seseorang ideal,
kurang, atau berlebih berdasarkan tinggi badan mereka.
"""

# Menampilkan hasil output ke layar
print("Nama:", nama)
print("Umur:", umur + 1, "tahun")              # Umur ditambah 1 tahun
print("Berat badan:", berat, "kg")
print("BMI:", round(bmi, 2))                   # BMI dibulatkan 2 angka di belakang koma
print("Siswa Aktif:", status_siswa)            # Menampilkan status siswa sebagai boolean
