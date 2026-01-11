# Latihan ujian

print('=' * 40)
print('      ☕ PROGRAM PEMBELIAN KOPI ☕')
print('=' * 40)

try:
    jumlah_gelas = int(input('Masukkan jumlah gelas kopi yang dibeli: '))
except ValueError:
    print('\n❌ Input tidak valid! Harus berupa angka.')
    exit()

harga_kopi = 18000

if jumlah_gelas < 0:
    print('\n❌ Jumlah gelas tidak boleh negatif.')
else:
    total = jumlah_gelas * harga_kopi
    diskon = 20000 if jumlah_gelas > 6 else 0
    totalAkhir = total - diskon
    pesan_tambahan = "🎉 Anda berhak mendapatkan diskon!" if diskon > 0 else "(Beli lebih dari 6 gelas untuk dapat diskon!)"

    print('\n------ RINCIAN PEMBELIAN ------')
    print(f'Jumlah Gelas   : {jumlah_gelas}')
    print(f'Harga per Gelas: Rp{harga_kopi:,}')
    print(f'Total Harga    : Rp{total:,}')
    print(f'Potongan       : Rp{diskon:,}')
    print('-' * 30)
    print(f'Total Bayar    : Rp{totalAkhir:,}')
    print('-' * 30)
    print(pesan_tambahan)
    print('=' * 40)
    print('Terima kasih telah membeli kopi kami ☕')
    print('=' * 40)
