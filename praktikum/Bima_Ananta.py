jumlah_gelas = int(input('Berapa gelas kopi yang dibeli?'))

harga_kopi = 18000
total = jumlah_gelas * harga_kopi

potongan = 0
totalAkhir = total

if jumlah_gelas < 0:
  print('Jumalah gelas tidak valid.')
elif jumlah_gelas <= 6:
  print(f'Tidak mendapatkan potongan')
  print(f'Harga yang harus dibayar: Rp{total}')
else:
  diskon = 20000
  totalAkhir = total - diskon
  print(f'Mendapatkan potongan: Rp{diskon}')
  print(f'Total: Rp{totalAkhir}')



