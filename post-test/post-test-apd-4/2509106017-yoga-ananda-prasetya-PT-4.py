# Import Library yang diperlukan
import os
import time

# Deklarasi variabel untuk pengulangan program, serta variabel untuk login
ulang = "y"
username = "yoga"
password = "017"

# Deklarasi variabel untuk harga makanan dan minuman
harga_nasi_campur = 18000
harga_nasi_kuning = 15000
harga_nasi_padang = 20000
harga_nasi_uduk = 22000

harga_air_mineral = 4000
harga_teh = 5000
harga_jeruk = 6000
harga_doger = 9000

# Program akan terus berjalan selama nilai dari ulang == y
while ulang == "y":
    # Deklarasi variabel yang akan digunakan untuk Autentifikasi Login
    kesempatan = 4 
    verifikasi = False

    # Deklarasi variabel yang akan digunakan untuk menghitung total dan jenis makanan yang dipesan
    keranjang = "" 
    total = 0

    # Bagian Header Program
    print("-" * 60)
    print("|", "Warung Makan 'Asal Makan'".center(56), "|")
    print("-" * 60)
    member = input("Apakah anda Member (y/n)? ")

    # Bagian pertanyaan terkait member atau bukan
    if member == "y":
        # Bagian Login dan Auntentifikasi Login
        while kesempatan != 0: 
            # Bagian input username dan password
            username_login = input("Masukkan Username Anda : ")
            password_login = input("Masukkan Password Anda : ")
            print("-" * 60)

            # Bagian pengecekan username dan password
            if username_login == username and password_login == password: 
                print("Berhasil Login")
                verifikasi = True
                time.sleep(1)
                os.system("cls")
                break
           
            time.sleep(1)
            os.system("cls")

            # Bagian jika user salah memasukkan username / password
            print("-" * 60)
            print("|", f"{'Login gagal, Silahkan coba lagi!' :57} {"|"}" )
            kesempatan -= 1
            print("|", f"Sisa Kesempatan : {kesempatan :39}", "|")
            print("-" * 60)
            
            # Jika user kehabisan kesempatan, maka program akan pergi kesini
            if kesempatan == 0: 
                print("|", f"{'Kesempatan Habis, Mengalihkan ke menu belanja':57}", "|")
                print("-" * 60)
                time.sleep(1)
                os.system("cls")


    # Program akan pergi kesini jika user bukan member        
    else: 
        print("Bukan Member, Mengalihkan ke menu belanja")
        print("-" * 60)
        time.sleep(1)
        os.system("cls")

    # Bagian Menu dan pemesanannya
    while True:
        # Bagian display menu
        print("-" * 60)
        print("|", "DAFTAR MENU".center(56), "|")
        print("-" * 60)

        print("|", "Makanan".center(56), "|")
        print("|", f"{'1 - Nasi Campur' :35} {'Rp 18.000 / Porsi' :20} {"|"}")
        print("|", f"{'2 - Nasi Kuning' :35} {'Rp 15.000 / Porsi' :20} {"|"}")
        print("|", f"{'3 - Nasi Padang' :35} {'Rp 20.000 / Porsi' :20} {"|"}")
        print("|", f"{'4 - Nasi Uduk Komplit' :35} {'Rp 22.000 / Porsi' :20} {"|"}")
        print("-" * 60)
        
        print("|", "Minuman".center(56), "|")
        print("|", f"{'5 - Air Mineral' :35} {'Rp 4.000 / Botol' :20} {"|"}")
        print("|", f"{'6 - Es Teh' :35} {'Rp 5.000 / Gelas' :20} {"|"}")
        print("|", f"{'7 - Es Jeruk' :35} {'Rp 6.000 / Gelas' :20} {"|"}")
        print("|", f"{'8 - Es Doger' :35} {'Rp 9.000 / Gelas' :20} {"|"}")
        print("-" * 60)

        print("|", "Opsi".center(56), "|")
        print("|", f"{'0 - Checkout Pesanan Anda' :56} {"|"}")
        print("-" * 60)

        # Bagian untuk menampilkan jumlah makanan/minuman yang dipesan beserta harganya
        print("Pesanan Sementara :")
        print(keranjang)
        print(f"Total Sementara = Rp {f"{total:,}".replace(",", ".")}")
        print("-" * 60)

        # Bagian untuk pemesanan
        print("Jika ingin Checkout, silahkan pilih menu 0")
        menu = int(input("Masukkan Pesanan Anda (1-8) : "))
        
        # Mengecek apakah user ingin checkout atau tidak
        if menu == 0:
            print("-" * 60)
            time.sleep(1)
            os.system("cls") 
            break

        jumlah = int(input("Masukkan Jumlah Pesanan : "))
        print("-" * 60)
        time.sleep(1)
        os.system("cls")

        # Bagian untuk menghitung total harga dari jumlah porsi yang dipesan
        if menu == 1: 
            total += harga_nasi_campur * jumlah
            keranjang += f"Nasi Campur x {jumlah} = Rp {f"{harga_nasi_campur * jumlah:,}".replace(",", ".")}\n"
        elif menu == 2: 
            total += harga_nasi_kuning * jumlah
            keranjang += f"Nasi Kuning x {jumlah} = Rp {f"{harga_nasi_kuning * jumlah:,}".replace(",", ".")}\n"
        elif menu == 3: 
            total += harga_nasi_padang * jumlah
            keranjang += f"Nasi Padang x {jumlah} = Rp {f"{harga_nasi_padang * jumlah:,}".replace(",", ".")}\n"
        elif menu == 4: 
            total += harga_nasi_uduk * jumlah
            keranjang += f"Nasi Uduk x {jumlah} = Rp {f"{harga_nasi_uduk * jumlah:,}".replace(",", ".")}\n"
        elif menu == 5: 
            total += harga_air_mineral * jumlah
            keranjang += f"Air Mineral x {jumlah} = Rp {f"{harga_air_mineral * jumlah:,}".replace(",", ".")}\n"
        elif menu == 6: 
            total += harga_teh * jumlah
            keranjang += f"Es Teh x {jumlah} = Rp {f"{harga_teh * jumlah:,}".replace(",", ".")}\n"
        elif menu == 7: 
            total += harga_jeruk * jumlah
            keranjang += f"Es Jeruk x {jumlah} = Rp {f"{harga_jeruk * jumlah:,}".replace(",", ".")}\n"
        elif menu == 8: 
            total += harga_doger * jumlah
            keranjang += f"Es Doger x {jumlah} = Rp {f"{harga_doger * jumlah:,}".replace(",", ".")}\n"
        else: 
            print("-" * 60)
            print("|", f"{'Pilihan menu tidak valid!' :56} {"|"}")
            print("|", f"{'Masukkan angka berdasarkan menu yang ada!' :56} {"|"}")
            print("-" * 60)
            time.sleep(1)
            os.system("cls")

    # Bagian Checkout
    print("-" * 60)
    print("|", "STRUK BELANJA".center(56), "|")
    print("-" * 60)
    print(keranjang)
    print("-" * 60)

    # Bagian jika user adalah member
    if verifikasi == True: 
        print(f"Total Harga Sebelum Diskon = Rp {total:,}".replace(",", "."))
        print(f"Diskon = 15%")
        diskon = int(total * 0.15)

        print(f"Total Diskon = Rp {diskon:,}".replace(",", "."))
        print(f"Total yang harus dibayar = Rp {total - diskon:,}".replace(",", "."))

    # Bagian jika user bukan member
    else: 
        print(f"Total yang harus dibayar = Rp {total:,}".replace(",", "."))
    
    # Bagian untuk pengulangan program
    print("-" * 60)
    ulang = input("Apakah anda ingin berbelanja lagi (y/n)? ")
    time.sleep(1)
    os.system("cls")

print("Belanja Selesai!")
print("Terimakasih telah datang ke Warung 'Asal Makan'\n")