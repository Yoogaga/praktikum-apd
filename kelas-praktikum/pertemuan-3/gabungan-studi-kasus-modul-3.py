print("Pilih Studi Kasus :")
print("1 - Nomor 1")
print("2 - Nomor 2")

nomor = int(input("Masukkan Pilihan Anda : "))

if nomor == 1: 
    print("-" * 60)
    print("Selamat Datang di Wahana Roller Coaster Tornado Dufan!".center(60))
    print("-" * 60)

    tinggi_badan = int(input("Masukkan Tinggi Badan Anda (Dalam cm) : "))
    izin = "Diizinkan Naik Wahana" if tinggi_badan >= 145 else "Tidak Diizinkan Naik Wahana"

    print("Anda", izin)

elif nomor == 2: 
    print("-" * 60)
    print("Diskon Grand Opening!".center(60))
    print("-" * 60)

    total_belanja = int(input("Masukkan Total belanja Anda : "))

    if total_belanja > 100000: 
        diskon = total_belanja * 0.20
        harga_akhir = total_belanja - diskon

    elif total_belanja > 50000: 
        diskon = total_belanja * 0.10
        harga_akhir = total_belanja - diskon 

    else:
        harga_akhir = total_belanja
        print("Anda tidak mendapatkan diskon")

    print("Harga Akhir Anda Adalah :", harga_akhir)        