print("-" * 60)
print("Selamat Datang di Wahana Roller Coaster Tornado Dufan!".center(60))
print("-" * 60)

tinggi_badan = int(input("Masukkan Tinggi Badan Anda (Dalam cm) : "))
izin = "Diizinkan Naik Wahana" if tinggi_badan >= 145 else "Tidak Diizinkan Naik Wahana"

print("Anda", izin)