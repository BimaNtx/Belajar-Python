# Skor awal gamer
skor = 0
print(f"Skor awal               : {skor}")

# Misi 1: +120 poin
skor += 120
print(f"Setelah Misi 1 (+120)   : {skor}")

# Misi 2: +150 poin
skor += 150
print(f"Setelah Misi 2 (+150)   : {skor}")

# Misi 3: +100 poin
skor += 100
print(f"Setelah Misi 3 (+100)   : {skor}")

# Penalti karena keluar jalur: -50 poin
skor -= 50
print(f"Setelah penalti (-50)   : {skor}")

# Bonus pengali skor 2 kali lipat
skor *= 2
print(f"Setelah bonus x2 (*2)   : {skor}")

# Kehilangan 30 poin karena kesalahan teknis
skor -= 30
print(f"Setelah kesalahan (-30) : {skor}")

# Tampilkan skor akhir
print(f"Skor akhir gamer        : {skor}")
