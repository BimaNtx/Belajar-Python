nama = input("Masukkan nama: ")
tagihan = int(input("Masukkan jumlah tagihan: "))
bayar = int(input("Masukkan jumlah yang dibayarkan: "))

if bayar == tagihan:
    print(f"Nasabah {nama} telah LUNAS")
elif bayar < tagihan:
    sisa = tagihan - bayar
    print(f"Nasabah {nama} masih punya sisa tagihan Rp{sisa}")
else:
    lebih = bayar - tagihan
    print(f"Nasabah {nama} LUNAS dan punya kelebihan Rp{lebih}")
