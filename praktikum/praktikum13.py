# Meminta input nilai dari pengguna untuk ke-3 mapel
mtk = int(input("Masukkan nilai Matematika: "))
bindo = int(input("Masukkan nilai Bahasa Indonesia: "))
ipa = int(input("Masukkan nilai IPA: "))

# Hitung rata-rata dari ke-3 mapel
rata_rata = (mtk + bindo + ipa) / 3

# Cek kondisi kelulusan berdasarkan aturan

if mtk > 85 and bindo > 85 and ipa > 85:
    status = "Lulus dengan Predikat Istimewa"
elif mtk < 70 and bindo < 70 or mtk < 70 and ipa < 70 or bindo < 70 and ipa < 70:
    status = "Tidak Lulus"
elif (mtk < 70 or bindo < 70 or ipa < 70) and (
    (mtk > 80 and bindo > 80) or (mtk > 80 and ipa > 80) or (bindo > 80 and ipa > 80)
):
    status = "Lulus Bersyarat"
elif mtk >= 70 and bindo >= 70 and ipa >= 70 and rata_rata >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

# Tampilkan ke layarrrr
print("\n========== HASIL KELULUSAN ==========")
print(f"Nilai Matematika      : {mtk}")
print(f"Nilai Bahasa Indonesia: {bindo}")
print(f"Nilai IPA             : {ipa}")
print(f"Rata-rata Nilai       : {rata_rata:.2f}")
print(f"Status Kelulusan      : {status}")
print("=====================================")
