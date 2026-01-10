# Input harga dan jumlah barang
harga_sabun = int(input("Masukkan harga sabun: "))
jumlah_sabun = int(input("Masukkan jumlah sabun: "))

harga_pasta = int(input("Masukkan harga pasta gigi: "))
jumlah_pasta = int(input("Masukkan jumlah pasta gigi: "))

harga_shampoo = int(input("Masukkan harga shampoo: "))
jumlah_shampoo = int(input("Masukkan jumlah shampoo: "))

# Hitung total tiap barang
total_sabun = harga_sabun * jumlah_sabun
total_pasta = harga_pasta * jumlah_pasta
total_shampoo = harga_shampoo * jumlah_shampoo

# Hitung total keseluruhan
total_belanja = total_sabun + total_pasta + total_shampoo

# Cetak hasil rapi
print("\nSTRUK BELANJA")
print(f"Sabun mandi   : {jumlah_sabun} x Rp{harga_sabun} = Rp{total_sabun}")
print(f"Pasta gigi    : {jumlah_pasta} x Rp{harga_pasta} = Rp{total_pasta}")
print(f"Shampoo       : {jumlah_shampoo} x Rp{harga_shampoo} = Rp{total_shampoo}")
print("-"*50)
print(f"Total belanja : Rp{total_belanja}")
