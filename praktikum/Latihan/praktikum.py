pertanyaan = [
  'Siapa nama Anda: '
  'Siapa nama Saya: '
  'Siapa nama Dia: '
]
jawaban = [
  'orang'
  'bima'
  'siapa ya'
]

skor = 0 
for i in range(pertanyaan):
  pertanyaan_sekarang = pertanyaan[i]
  jawaban_pengguna = input(f'pertanyaan sekrang {i+1}: {pertanyaan_sekarang}')
  
  jawaban_benar = jawaban[i]
  
  if jawaban_pengguna.lower() == jawaban.lower():
    print('Benar')
    skor += 1
  else: 
    print('Salah')
    
print("\n" + "="*20)
print(f"KUIS SELESAI!")
print(f"Skor akhir Anda: {skor}")
print("="*20)