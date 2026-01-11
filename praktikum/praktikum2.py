# Data awal
usia = 17                  # integer
tinggi_badan = 170.5       # float
mahasiswa_aktif = True     # boolean

# Konversi tipe data
usia_str = str(usia)                       # int ke string
tinggi_int = int(tinggi_badan)            # float ke int (pembulatan ke bawah)
mahasiswa_int = int(mahasiswa_aktif)      # bool ke int (True = 1, False = 0)

# Menampilkan hasil dan tipe datanya
print("Konversi usia ke string:")
print("Hasil:", usia_str, "| Tipe:", type(usia_str))

print("\nKonversi tinggi_badan ke integer:")
print("Hasil:", tinggi_int, "| Tipe:", type(tinggi_int))

print("\nKonversi mahasiswa_aktif ke integer:")
print("Hasil:", mahasiswa_int, "| Tipe:", type(mahasiswa_int))

# Variasi tambahan: Konversi kebalikan
print("\n--- Variasi Tambahan ---")

# Konversi string ke integer
usia_asli = int(usia_str)
print("Konversi kembali usia_str ke integer:", usia_asli, "| Tipe:", type(usia_asli))

# Konversi integer ke float
tinggi_float = float(tinggi_int)
print("Konversi tinggi_int ke float:", tinggi_float, "| Tipe:", type(tinggi_float))

# Konversi angka 0 dan 1 ke boolean
print("Konversi 0 ke boolean:", bool(0), "| Tipe:", type(bool(0)))
print("Konversi 1 ke boolean:", bool(1), "| Tipe:", type(bool(1)))
