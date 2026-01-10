# validasi input dengan while loop

passwordBenar = "luen"
password = input("Masukkan password: ")

while password != passwordBenar:
  print("Password salah, cube lagi")
  password = input("Masukkan password: ")
  
print("Password Benar, silahkan masuk")


# coba

import getpass

pwBetul = "bmx"
maksPercobaan = 3
percobaan = 0

while percobaan < maksPercobaan:
  password = getpass.getpass("Masukkan pw: ")
  if password == pwBetul:
    print("Berhasil masuk, Selamat datang")
    break
  else:
    percobaan += 1
    sisa = maksPercobaan - percobaan
    print(f"TETOT Password salah. Sisa percobaan: {sisa}")
    
if percobaan == maksPercobaan:
  print("Kesempatan habis nt")