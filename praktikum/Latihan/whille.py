angka = 0
while angka <= 9:
  print(angka)
  angka +=1
  
password = ''
while password != '12345':
  password = (input('Masukkan password Anda: '))
  if password != '12345':
    print('Password salah')
print('Password benar')


