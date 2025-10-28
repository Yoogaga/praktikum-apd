# Import library yang diperlukan
import os
import time
from fungsi import *
import fungsi

# Deklarasi Dictionary yang diperlukan
akun = {
    "acc1": {
        "username": "Chryse", 
        "password": "79-Au",  
        "role": "admin", 
        "game": {
            "g1": {"nama": "Armored Core Verdict Day", "tahun": "2007", "dev": "Fromsoftware", "status": "Tamat"},  
            "g2": {"nama": "Armored Core 4: For Answer", "tahun": "2008", "dev": "Fromsoftware", "status": "Belum tamat"}
            }
        },

    "acc2": {
        "username": "Dapupu", 
        "password": "Ketua_Nibung", 
        "role": "member", 
        "game": {
            "g1": {"nama": "MudRunner", "tahun": "2017", "dev": "Saber Interactive", "status": "Belum Tamat"},  
            }
        }
}

# Perulangan Utama yang akan terus mengulang program sampai pengguna memilih untuk berhenti 
while True: 
    try: 
        konfirmasi_login = False # Mengatur apakah pengguna sudah login atau belum (Sudah = True, Belum = False)
        kesempatan = 4 # Mengatur kesempatan login yang dimiliki pengguna
        gagal_login = False # Merupakan parameter yang akan digunakan apabila pengguna menghabiskan kesempatan loginnya
        
        # Tampilan Header Program
        print("=" * 80)
        print("{:^80}".format("PROGRAM DIREKTORI GAME"))
        print("=" * 80)

        # Tampilan Menu
        print("1 - Login Akun")
        print("2 - Register Akun")
        print("=" * 80)

        # Tampilan Opsi Tambahan
        print("0 - Akhiri Program")
        print("=" * 80)

        # Input Pilihan Pengguna
        print("Silakan pilih menu yang anda inginkan:")
        aksi = int(input("> "))
        print("=" * 80)

        # Bagian untuk membersihkan terminal
        clear()

        if aksi == 0:
            break
        elif aksi == 1: 
            login()
        elif aksi == 2: 
            register()
            fungsi.konfirmasi_login = False
        else: 
            print("Pilihan tidak valid")
        
        if fungsi.konfirmasi_login == True: 
            while True:
                # Bagian Display Menu
                print("=" * 74)
                print(f"Selamat datang kembali, {fungsi.username_anda}")
                print(f"Anda login sebagai: {fungsi.role_anda}")
                print("=" * 74)

                # Display Menu
                print("1 - Tambah Game Baru")
                print("2 - Lihat List Game")
                print("3 - Update Informasi Game")
                print("4 - Hapus Game dari Direktori")
                print("=" * 74)

                print("0 - Logout")
                if fungsi.role_anda == 'admin': 
                    print("5 - Menu Admin")

                print("=" * 74)
                print("Masukkan Menu yang Anda Inginkan :")
                print("=" * 74)
                pilih_menu = int(input("> "))
                print("=" * 74)

                clear()

                if pilih_menu == 0:
                    break
                elif pilih_menu == 1: 
                    tambah_game()
                elif pilih_menu == 2: 
                    lihat_game()
                elif pilih_menu == 3: 
                    update_game()
                elif pilih_menu == 4: 
                    hapus_game()
                elif pilih_menu == 5 and fungsi.role_anda == "admin": 
                    menu_admin()
                else: 
                    print("Piihan Tidak valid")
                    clear()
    
    except AttributeError: 
        print("Pilihan Tidak Valid")
        clear()

    except ValueError: 
        print("Pilihan Tidak Valid")
        clear()

print("Program Selesai!")
print("Terimakasih telah menggunakan program ini!")

    