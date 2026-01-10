# belajar coding 4

n = int(input("Masukkan jumlah siswa: "))

nama_siswa = [] # untuk membuat list kosong
nilai_siswa = []

# Loop jumlah siswa
for i in range(n):
    print(f"\nData siswa ke-{i+1}")
    nama = input(f"Masukkan Nama {i+1}: ")
    nilai = int(input(f"Masukkan Nilai {i+1}: "))
    
    nama_siswa.append(nama) #appaned buat menambahkan ke dalam list
    nilai_siswa.append(nilai)

# menghitung rata-rata
rata_rata = sum(nilai_siswa) / n

# Cari nilai tertinggi top singko
nilai_tertinggi = max(nilai_siswa)
indeks_tertinggi = nilai_siswa.index(nilai_tertinggi)
nama_tertinggi = nama_siswa[indeks_tertinggi]

print("\n\nHasil Akhir")
print(f"Selamat kepada {nama_tertinggi}, Anda mendapatkan nilai tertinggi ({nilai_tertinggi})")
print(f"Nilai rata-rata dari {n} siswa yaitu: {rata_rata:.2f}")
