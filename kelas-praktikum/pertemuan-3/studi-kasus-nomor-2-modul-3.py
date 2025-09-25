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