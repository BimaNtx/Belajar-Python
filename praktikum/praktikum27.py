# menjumlahkan bilangan

n = int(input("Masukkan nilai N: "))
jumlah = 0
for i in range(1, n + 1):
  jumlah += i
  print(f"Langkah {i}: Jumlah semestara = {jumlah}")
print("Jumlah:", jumlah)

