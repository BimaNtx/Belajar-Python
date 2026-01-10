# soal 17: validasi usia 

usia = int(input("Masukkan usia anda: "))

if usia >= 60:
  print("Anda sudah Lansia")
elif usia >= 20:
  print("Anda sudah Dewasa")
elif usia >= 17:
  print("Anda Remaja")
elif usia >= 12:
  print("Anda masih Anak-Anak")
else:
  print("Anda masih Kecil tidak boleh")