# Praktikum 33 logika

nama_produk = input("Masukkan nama barang: ")
harga = int(input("Masukkan harganya: "))

print(f"\nProduk: {nama_produk}")
print(f"Harga: Rp{harga:,.0f}")

if harga > 500000:
    kategori = "Premium (harga di atas Rp500.000)"
elif harga >= 100000:
    kategori = "Standar (harga antara Rp100.000 - Rp500.000)"
else:
    kategori = "Murah (harga di bawah Rp100.000)"

print(f"Kategori: {kategori}")