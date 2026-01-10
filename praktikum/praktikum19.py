username = input("Masukkan username Anda: ")

if username.lower() == "aadmin":
  print ("Selamat datang, Admin yang terhormat")
  print("Anda memiliki akses penuh ke sistem.")
else:
  print("Maaf, ", username, "tidak memiliki akses admin.")
  print("Hubungi administrator untuk mendapatkan akses")