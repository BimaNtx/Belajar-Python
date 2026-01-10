# Soal 15 menentukan bilangan Positif dan Negatif

# Minta pengguna memasukkan bilangan
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# Periksa kondisi bilangan
if bilangan > 0:
    print("Bilangan positif")
elif bilangan < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")