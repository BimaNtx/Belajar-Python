# Praktikum 12: Aritmatika

# Mendefinisikan harga satuan barang
harga_a = 12500
harga_b = 7300
harga_c = 2850

# Minta input dari pengguna (Jumlah barang yang ingin dibeli)
jumlah_a = int(input("Masukkan jumlah barang A yang ingin dibeli: "))
jumlah_b = int(input("Masukkan jumlah barang B yang ingin dibeli: "))
jumlah_c = int(input("Masukkan jumlah barang C yang ingin dibeli: "))

# Hitung harga kotor (sebelum diskon)
total_kotor = (jumlah_a * harga_a) + (jumlah_b * harga_b) + (jumlah_c * harga_c)

# Menentukan harga diskon 
if total_kotor > 1501000:
  diskon = 0.15 * total_kotor
elif total_kotor > 100000:
  diskon = 0.10 * total_kotor
else:
  diskon = 0

# Menghitung total harga bersih
total_bersih = total_kotor - diskon

# Tampilkan
print("\n========== STRUK PEMBELIAN ==========")
print(f"Total harga kotor : Rp{total_kotor:,.0f}")
print(f"Diskon            : Rp{diskon:,.0f}")
print(f"Total harga bersih: Rp{total_bersih:,.0f}")
print("=====================================")






