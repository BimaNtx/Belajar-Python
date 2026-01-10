# menjumlahkan angka

n = int(input('Masukkan nilai N: '))
i = 1
jumlah = 0 

while i <= n: # menjumlahkan semua angka dari 1 sampai n
  print(i, end=" ") #end=" " agar output ridak pindah baris dan dipisahkan dgn spasi
  jumlah += i
  i += 1
  
print("\njumlah:", jumlah) # \n buat pindah ke baris baru

# coba

nilai = int(input("Masukkan Nilai: "))
jumlah = n * (n + 1)//2 # menggunakan rumus N x (N+1) / 2
print("Jumlah:", jumlah)