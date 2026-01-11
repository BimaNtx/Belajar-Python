data_angka = [10, 5, 8, 2, 5]
total = 0

for angka in data_angka:
  total = total + angka
  
print(f'List angka: {data_angka}')
print(f'Total penjumlahan: {total}')

baris = int(input('Masukkan tinggi segitiga: '))
for i in range(1, baris+1):
  for j in range(i):
    print('*', end='')
  print()