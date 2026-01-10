# Praktikum 34 logikaa

nama_karyawan = input("Masukkan nama karyawan: ")
golongan = int(input("Masukkan golongan: "))
jumlah_hari_kerja = int(input("Masukkan jumlah hari kerja bulan ini: "))

# Menggunakan dictionary untuk gaji pokok, ben lebih rapi
gaji_pokok_per_golongan = {
    1: 3000000,
    2: 4500000,
    3: 7000000
}

# Mendapatkan gaji pokok dari dictionary
gaji_pokok = gaji_pokok_per_golongan.get(golongan, 0)

# bonus
bonus = 0
if jumlah_hari_kerja > 20:
    bonus = 0.1 * gaji_pokok

# total gaji
total_gaji = gaji_pokok + bonus

print("\nDetail Gaji Karyawan")
print(f"Nama Karyawan    : {nama_karyawan}")
print(f"Golongan         : {golongan}")
print(f"Jumlah Hari Kerja: {jumlah_hari_kerja} hari")
print(f"Gaji Pokok       : Rp{gaji_pokok:,.0f}")
print(f"Bonus            : Rp{bonus:,.0f}")
print(f"Total Gaji       : Rp{total_gaji:,.0f}")