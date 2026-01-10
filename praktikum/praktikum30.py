# membuat bintang

n = int(input("Masukkan tinggi segitiga: "))
for i in range(n, 0, -1):
  print("*" * i)
  
print("-"*50)

bintang = int(input("Masukkan tinggi segitiga: "))

for i in range(1, bintang + 1):
  print(" " * (bintang - i) + "*" * (2 * i -1))