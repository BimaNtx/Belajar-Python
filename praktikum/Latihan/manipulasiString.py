nama = "bima"
print(len (nama))

saya = '''
halo
aku 
bima
'''
print(saya)

name = 'bima'
nama_upper = name.upper()
print(nama_upper)

nama_upper = name.lower()
print(nama_upper)

lengkap = 'bima ananta'
title = lengkap.title()
print(title)
title = lengkap.capitalize()
print(title)

spasi = '     bima     '
noSpasi = spasi.split()
print(noSpasi)

bima = 'bima sangar'
bimaV2 = bima.replace('sangar', 'tampan')
print(bimaV2)

jumlah_a = bima.count('a')
print(jumlah_a)

harga = 10000
jumlah = 3
total  = (f'Jumlah yang harus dibayar Rp{harga * jumlah}')
print(total)