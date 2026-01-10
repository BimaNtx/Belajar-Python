# Belajar

# * pke if aja nih 
# angka = int(input('Masukkan angka: '))

# if angka > 0:
#   print('Angka Positif')
# if angka < 0:
#   print('Angka Negatif')
# if angka == 0:
#   print('Angka NOL')
  
print('_'*50)

# * pke if-else
# nilai = int(input('Masukkan Nilai Anda: '))
# if nilai > 80:
#   print('Bagus')
# else:
#   print('Belajar Lagi')

print('_'*50)

# * if-elif-else 
# nilai = int(input('Masukkan Nilai Anda: '))
# if nilai >= 90:
#   print('A')
# elif nilai >= 80:
#   print('B')
# elif nilai >= 70:
#   print('C')
# else:
#   print('NONO')

# * operator logika
# umur = int(input('Masukkan Umur Anda: '))
# sim = input('Apakah punya SIM: (ya/tidak)')

# if umur > 17 and sim == 'ya':
#   print('Boleh naek motor')
# else:
#   print('Pulang saja')
  
# * nasted if
# username = input('Masukkan username Anda: ')
# password = input('Masukkan PW Anda: ')

# if username == 'admin':
  
#   if password == '123':
#     print('Login sukses')
#     print('Selamat datang cuy')
#   else:
#     print('PW salah')
  
# else: 
#   print('Username salah')

# * match case
# hari = input('Masukkan nama Hari: ').lower()

# match hari:
#   case "senin" | 'selasa' | 'rabu' | 'kamis' | 'jumat':
#     print('Hari kerja')
#   case 'sabtu' | 'minggu':
#     print('Hari libur') 
#   case _:
#     'Hari ape tu woy'

# * ternary operator

angka = int(input('Masukkan Angka: '))

# if angka > 0:
#   print('Angka Positif')
#   hasil = 'Positif'
# else:
#   hasil = 'Non-Positif'

hasil = 'Positif' if angka > 0 else 'Non positif'
print(hasil)