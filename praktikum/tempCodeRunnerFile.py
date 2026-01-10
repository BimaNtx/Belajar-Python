# belajar coding 4
# input data nama dan data nilai siswa

n = int(input("Masukkan jumlah siswa: "))

nama1 = input("Masukkan Nama 1: ")
nilai1 = int(input("Masukkan Nilai 1: "))
print()
nama2 = (input("Masukkan Nama 2: "))
nilai2 = int(input("Masukkan nilai 2: "))
print()
nama3 = input("Masukkan nama 3: ")
nilai3 = int(input("Masukkan Nilai 3: "))

count = nilai1 + nilai2 + nilai3
count /= 3
print("\n\n\n")
# mencari nilai palling tinggi
if nilai1 >= nilai2 and nilai1 >= nilai3:
  print(f"Selamat kepada {nama1}, Anda mendapatkan nilai tertinggi")
elif nilai2 >= nilai1 and nilai2 >= nilai3:
  print(f"Selamat kepada {nama2}, Anda mendapatkan nilai tertinggi ")
else:
  print(f"Selamat kepada {nama3}, Amda mendapatkan nilai tertinggi")
  
print(f"Nilai rata-rata dari ketiga siswa yaitu: {count}")