# Import library yang diperlukan
import os
import time

# Deklarasi List yang diperlukan
# List menu_awal digunakan untuk memanggil menu utama tanpa harus mencetak nilai satu persatu-persatu
menu_awal = [["Tambah Game Baru", "[CREATE]"], # Formatnya yaitu : ["Nama Menu", "Prinsip CRUD yang diterapkan"]
             ["Lihat list game", "[READ]"], 
             ["Update Informasi Game", "[UPDATE]"], 
             ["Hapus Game dari Koleksi", "[DELETE]"]
             ]

# List ini menyimpan semua informasi / data game yang kita masukkan ke direktori
# Formatnya yaitu : ["Nama Game", "Tahun rilis game", "Developer Game", "Status game"]
koleksi_game = [
    ["Armored Core V", "2008", "Fromsoftware", "Belum Tamat"], 
    ["Armored Core Verdict Day", "2009", "Fromsoftware", "Tamat"],
    ["Armored Core 4: For Answer", "2008", "Fromsoftware", "Tamat"], 
    ["Armored Core 4", "2007", "Fromsoftware", "Belum Tamat"], 
]

# Perulangan yang akan terus mengulang program sampai pengguna memilih untuk berhenti
while True: 
    jumlah_baris = 1 # Me-reset ulang jumlah baris yang akan digunakan ketika list menu_awal dipanggil
    indeks_global = 0 # Indeks utama yang digunakan diseluruh bagian program

    # Bagian header menu utama
    print("=" * 25, "SELAMAT DATANG DI DIREKTORI GAME SEDERHANA", "=" * 25)
    print(f"{"No":5}{'Nama Menu':69}{"Fungsi"}")
    print("=" * 94)
    
    # Perulangan ini bertujuan untuk memanggil menu utama lewat list yang sudah dideklarasikan sebelumnya
    for i in menu_awal: 
        print(f"{str(jumlah_baris):5}{menu_awal[indeks_global][0]:69}{menu_awal[indeks_global][1]}")
        jumlah_baris += 1
        indeks_global += 1
    
    # Bagian ini menampilkan opsi keluar / menghentikan proram
    print("=" * 94)
    print(f"{'0':5}Keluar")
    print("=" * 94)

    # Bagian input pilihan yang diinginkan oleh pengguna
    pilih_menu = int(input("Masukkan menu yang ingin dipilih : "))
    print("=" * 94)
    
    # Bagian ini bertujuan untuk membersihkan terminal 
    time.sleep(1)
    os.system("clear")
    os.system("cls")

    # Bagian ini digunakan untuk memeriksa dan masuk ke menu yang dipilih oleh pengguna
    if pilih_menu == 0: # Menghentikan program
        break
    elif pilih_menu == 1: # Menambah game baru ke direktori, penerapan dari prinsip Create
        while True: 
            # Bagian header serta input data game yang ingin dimasukkan ke direktori
            print("=" * 25, "MENAMBAHKAN GAME BARU KE DIREKTORI", "=" * 25)
            game_baru = input(f"{'Masukkan Judul Game':30}: ")
            tahun_rilis = input(f"{'Masukkan Tahun Rilis Game':30}: ")
            developer_game = input(f"{'Masukkan Developer Game':30}: ")
            status_game = input(f"{'Masukkan Status Game':30}: ")
            print("=" * 86)
            
            time.sleep(1)
            os.system("clear")
            os.system("cls")

            # Memeriksa apakah ada dari keempat data tersebut apakah ada yang kosong
            if game_baru and tahun_rilis and developer_game and status_game != 0: # Jika semua data terisi, program lanjut ke bagian ini
                # Bagian ini menampilkan informasi terkait game baru yang akan dimasukkan ke direktori
                print("=" * 45, "INFORMASI GAME BARU", "=" * 45)
                print(f"{'Judul Game':45} {'Tahun Rilis':20} {'Developer':25} {'Status'}")
                print(f"{game_baru:45} {tahun_rilis:20} {developer_game:25} {status_game}")
                print("=" * 111)
                input("Tekan 'enter' untuk melanjutkan")
                print("=" * 111)

                time.sleep(1)
                os.system("clear")
                os.system("cls")

                # Bagian ini merupakan bagian menambah serta menampilkan daftar game
                koleksi_game.append([game_baru, tahun_rilis, developer_game, status_game]) # Bagian yang menambahkan game baru ke direktori
                print("=" * 45, "LIST GAME SEKARANG", "=" * 45)
                print(f"{"No":5}{'Judul Game':45} {'Tahun Rilis':20} {'Developer':25} {'Status'}") 
                print("=" * 111)

                # Bagian yang menampilkan daftar game setelah game baru ditambahkan
                indeks_global = 0
                for i in koleksi_game: 
                    print(f"{str(indeks_global + 1):5}{koleksi_game[indeks_global][0]:45} {koleksi_game[indeks_global][1]:20} {koleksi_game[indeks_global][2]:25} {koleksi_game[indeks_global][3]}")
                    indeks_global += 1
                
                print("=" * 111)                
                input("Tekan 'enter' untuk kembali")
                print("=" * 111)
                
                time.sleep(1)
                os.system("clear")
                os.system("cls")
                break # Kembali ke menu utama

            else: # Jika ada satu data saja yang tidak terisi, program akan menjalankan bagian kode ini
                print("=" * 111)
                print("Tidak Boleh ada yang kosong!") # Memberikan peringatan agar pengguna tidak meninggalkan data kosong
                print("=" * 111)

                time.sleep(1)
                os.system("clear")
                os.system("cls")        
    elif pilih_menu == 2: # Menampilkan game yang terdapat di direktori, penerapan dari prinsip Read
        # Header Program
        print("=" * 49, "KOLEKSI GAME", "=" * 48)
        print(f"{"No":5}{'Judul Game':45} {'Tahun Rilis':20} {'Developer':25} {'Status'}")
        print("=" * 111)
        
        # Digunakan untuk membuat daftar game yang ada di direktori
        indeks_global = 0
        for i in koleksi_game: 
            print(f"{str(indeks_global + 1):5}{koleksi_game[indeks_global][0]:45} {koleksi_game[indeks_global][1]:20} {koleksi_game[indeks_global][2]:25} {koleksi_game[indeks_global][3]}")
            indeks_global += 1
        
        print("=" * 111)
        input("Tekan 'enter' untuk kembali ke menu utama ")
        print("=" * 111)

        time.sleep(1)
        os.system("clear")
        os.system("cls")
    elif pilih_menu == 3: # Implementasi dari prinsip Update, yaitu mengganti data game
        while True: 
            # Bagian header
            print("=" * 49, "MENU UPDATE", "=" * 49)
            print(f"{"No":5}{'Judul Game':45} {'Tahun Rilis':20} {'Developer':25} {'Status'}")
            print("=" * 111)

            # Bagian yang menampilkan semua game yang ada pada direkori
            indeks_global = 0
            for i in koleksi_game: 
                print(f"{str(indeks_global + 1):5}{koleksi_game[indeks_global][0]:45} {koleksi_game[indeks_global][1]:20} {koleksi_game[indeks_global][2]:25} {koleksi_game[indeks_global][3]}")
                indeks_global += 1
            
            # Bagian yang digunakan untuk keluar dari mode update
            print("=" * 111)
            print(f"{'0':5}Keluar")
            print("=" * 111)

            # Bagian input nomor game yang akan diganti datanya
            pilih_update = int(input("Masukkan nomor game yang ingin diubah : "))
            print("=" * 111)

            time.sleep(1)
            os.system("clear")
            os.system("cls")

            # Bagian yang akan menghentikan proses update
            if pilih_update == 0: 
                break
            
            pilih_menu_update = pilih_update -1 # Dikurangi satu karena indeks dimulai dari 0, maka secara otomatis pilihan kita ada di bilangan sebelumnya
            print("")
            
            # Bagian yang memerika apakah nilai menu yang dimasukkan ada dalam range list koleksi 
            if 0 <= pilih_menu_update < len(koleksi_game): # Jika menu update yang dimasukkan benar, program akan lanjut disini
                while True: 
                    indeks_global = 0 # Mengatur indeks menjadi nilainya semula karena akan digunakan lagi
                    
                    # Bagian header 
                    print("=" * 61)
                    print("GAME YANG INGIN DIUPDATE ")
                    print("=" * 61)

                    # Bagian ini menampilkan informasi game yang diingin di-update
                    print(f"{'1 - Judul Game':20}:", koleksi_game[pilih_menu_update][0])
                    print(f"{'2 - Tahun Rilis':20}:", koleksi_game[pilih_menu_update][1])
                    print(f"{'3 - Developer':20}:", koleksi_game[pilih_menu_update][2])
                    print(f"{'4 - Status':20}:", koleksi_game[pilih_menu_update][3])
                    
                    print("=" * 61)
                    print("0 - Keluar") # Menampilkan menu keluar
                    print("=" * 61)
                    
                    # Bagian pengguna untuk memilih data mana yang ingin diganti
                    menu_update = int(input("Masukkan bagian yang ingin diubah : "))
                    print("=" * 61)

                    time.sleep(1)
                    os.system("clear")
                    os.system("cls")

                    if menu_update == 0: # Program akan kembali ke menu update jika pengguna memasukkan 0
                        break

                    elif menu_update == 1: # Bagian ini mengubah judul game yang dipilih
                        while True:
                            print("=" * 61)
                            print("MENGUBAH JUDUL GAME")                            
                            print("=" * 61)

                            print("Judul game lama :", koleksi_game[pilih_menu_update][0]) # Menampilkan judul game sebelum penggantian
                            ganti_judul = input("Judul game baru : ") # Bagian pengguna mengganti judul game
                            print("=" * 61)

                            time.sleep(1)
                            os.system("clear")
                            os.system("cls")

                            # Bagian ini memeriksa judul game yang dimasukkan kosong atau tidak
                            if len(ganti_judul) != 0: # Program akan lanjut kesini jika judul game yang dimasukkan tidak kosong
                                koleksi_game[pilih_menu_update][0] = ganti_judul # Mengganti judul game dengan yang baru
                                
                                print("=" * 61)
                                print("Judul Game Sekarang :", koleksi_game[pilih_menu_update][0]) # Menampilkan judul game setelah penggantian
                                input("Tekan 'enter' untuk kembali")
                                print("=" * 61)
                                
                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                                break
                            else: # Program akan menjalankan bagian ini jika judul game kosong
                                print("=" * 111)
                                print("Judul Game Tidak Boleh kosong!")
                                print("=" * 111)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                        
                        break

                    elif menu_update == 2: # Bagian ini mengganti tahun rilis dari game yang dipilih
                        while True: 
                            # Bagian header program
                            print("=" * 61)
                            print("MENGUBAH TAHUN RILIS")                            
                            print("=" * 61)
                            
                            print("Tahun Rilis Awal :", koleksi_game[pilih_menu_update][1]) # Menampilkan tahun rilis game sebelum penggantian                           
                            ganti_tahun = input("Tahun Rilis baru : ") # Bagian pengguna mengganti tahun rilis
                            print("=" * 61)

                            time.sleep(1)
                            os.system("clear")
                            os.system("cls")

                            # Bagian ini memeriksa apakah tahun yang dimasukkan kosong atau tidak
                            if len(ganti_tahun) != 0: # Jika tahun tidak kosong, program akan lanjut kesini
                                koleksi_game[pilih_menu_update][1] = ganti_tahun # Mengganti tahun rilis dengan tahun rilis yang dimasukkan pengguna
                                print("=" * 61)
                                print("Tahun rilis sekarang :", koleksi_game[pilih_menu_update][1]) # Menampilkan tahun rilis setelah diadakannya penggantian
                                input("Tekan 'enter' untuk kembali")
                                print("=" * 61)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                                break
                            
                            else: # Jika tahun rilis kosong, maka program akan menjalankan bagian ini
                                print("=" * 111)
                                print("Bagian tahun rilis tidak boleh kosong!")
                                print("=" * 111)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                        break

                    elif menu_update == 3: # Mengganti data developer game yang telah dipilih oleh pengguna
                        while True: 
                            # Bagian header
                            print("=" * 61)
                            print("MENGUBAH DEVELOPER GAME")
                            print("=" * 61)

                            print("Developer Awal :", koleksi_game[pilih_menu_update][2]) # Menampilkan data developer sebelum penggantian
                            ganti_developer = input("Developer Baru : ") # Bagian pengguna mengganti data developer dengan yang baru
                            print("=" * 61)

                            time.sleep(1)
                            os.system("clear")
                            os.system("cls")

                            # Memeriksa apakah data developer kosong atau tidak
                            if len(ganti_developer) != 0: # Jika tidak kosong, maka program akan lanjut kesini
                                koleksi_game[pilih_menu_update][2] = ganti_developer # Bagian ini mengganti data developer dengan data yang dimasukkan oleh pengguna
                                print("=" * 61)
                                print("Developer sekarang:", koleksi_game[pilih_menu_update][2]) # Menampilkan data developer setelah diadakan penggantian
                                input("Tekan 'enter' untuk kembali")
                                print("=" * 61)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                                break
                            else: # Jika data developer kosong, maka program akan menjalankan bagian ini
                                print("=" * 111)
                                print("Bagian Developer tidak boleh kosong!")
                                print("=" * 111)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                        break

                    elif menu_update == 4: # Bagian ini mengganti data status game yang dipilih oleh pengguna
                        while True: 
                            # Bagian header
                            print("=" * 61)
                            print("MENGUBAH STATUS")
                            print("=" * 61)

                            print("Status Awal :", koleksi_game[pilih_menu_update][3]) # Menampilkan status game sebelum penggantian
                            ganti_status = input("Status Baru : ") # Bagian pengguna mengganti status game 
                            print("=" * 61)

                            time.sleep(1)
                            os.system("clear")
                            os.system("cls")

                            # Memeriksa apakah status game yang dimasukkan kosong atau tidak
                            if len(ganti_status) != 0: # Jika tidak kosong, maka program akan lanjut ke bagian ini
                                koleksi_game[pilih_menu_update][3] = ganti_status # Mengganti status dengan dengan status yang dimasukkan oleh pengguna
                                print("=" * 61)
                                print("Status Baru :", koleksi_game[pilih_menu_update][3]) # Menampilkan status game setelah proses penggantian
                                input("Tekan 'enter' untuk melanjutkan")
                                print("=" * 61)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")

                                break
                            else: # Jika status game kosong, program akan menjalankan bagian ini
                                print("=" * 111)
                                print("Bagian Status tidak boleh kosong!")
                                print("=" * 111)

                                time.sleep(1)
                                os.system("clear")
                                os.system("cls")
                        break

                    else: 
                        print("=" * 111)
                        print("Pilihan Tidak Valid!")
                        print("=" * 111)

                        time.sleep(1)
                        os.system("clear")
                        os.system("cls")
                            
            else: # Jika menu update yang dimasukkan salah, program akan menjalankan bagian kode ini
                print("=" * 111)
                print("Pilihan tidak valid")
                print("=" * 111)

                time.sleep(1)
                os.system("clear")
                os.system("cls")
    elif pilih_menu == 4: # Bagian implementasi dari prinsip Delete, yaitu menghapus game yang tidak diinginkan
        while True:
            # Bagian Header
            print("=" * 49, "MENU HAPUS", "=" * 49)
            print(f"{"No":5}{'Judul Game':45} {'Tahun Rilis':20} {'Developer':25} {'Status'}")
            print("=" * 110)

            # Menampilkan data game yang ada di direktori
            indeks_global = 0
            for i in koleksi_game: 
                print(f"{str(indeks_global + 1):5}{koleksi_game[indeks_global][0]:45} {koleksi_game[indeks_global][1]:20} {koleksi_game[indeks_global][2]:25} {koleksi_game[indeks_global][3]}")
                indeks_global += 1
            
            print("=" * 110)
            print(f"{'0':5}Keluar") # Opsi keluar dari menu delete
            print("=" * 110)

            # Bagian pengguna memilih game mana yang ingin dihapus
            pilih_hapus = int(input("Masukkan nomor game yang ingin dihapus : "))
            print("=" * 110)

            time.sleep(1)
            os.system("clear")
            os.system("cls")
            
            # Bagian yang memeriksa apakah pengguna memasukkan angka 0 atau tidak
            if pilih_hapus == 0: 
                break
            
            pilih_menu_hapus = pilih_hapus -1 # Mengurangi dengan 1 karena indeks dimulai dari 0. Karena itu, data yang ingin diakses akan bergeser ke kiri sebanyak satu
            print("")

            # Bagian yang memeriksa apakah menu yang dimasukkan oleh pengguna ada pada range list koleksi_game atau tidak
            if 0 <= pilih_menu_hapus < len(koleksi_game): # Program akan lanjut kesini jika menu berada di dalam range
                # Bagian header
                print("=" * 110)
                print("GAME YANG INGIN DIHAPUS")
                print("=" * 110)

                # Menampilkan informasi game yang ingin dihapus
                print(f"{'1 - Judul Game':20}:", koleksi_game[pilih_menu_hapus][0])
                print(f"{'2 - Tahun Rilis':20}:", koleksi_game[pilih_menu_hapus][1])
                print(f"{'3 - Developer':20}:", koleksi_game[pilih_menu_hapus][2])
                print(f"{'4 - Status':20}:", koleksi_game[pilih_menu_hapus][3])
                print("=" * 110)

                # Bagian yang memeriksa apakah pengguna yakin ingin menghapus game dari direktori
                konfirmasi_hapus = input("Apakah anda yakin ingin menghapus game ini dari direktori (y/n)? ")
                print("=" * 110)

                time.sleep(1)
                os.system("clear")
                os.system("cls")
                
                # Bagian yang memeriksa jawaban dari pengguna
                if konfirmasi_hapus == "y": # Jika menjawab ya, maka program akan lanjut kesini
                    del koleksi_game[pilih_menu_hapus] # Bagian ini menghapus game yang dipilih oleh pengguna
                    
                    # Bagian ini menampilkan sisa game yang ada pada direktori
                    print("=" * 110)
                    print("GAME YANG TERSISA")
                    print("=" * 110)

                    print(f"{"No":5}{'Judul Game':45} {'Tahun Rilis':20} {'Developer':25} {'Status'}")
                    print("=" * 110)

                    indeks_global = 0
                    for i in koleksi_game: 
                        print(f"{str(indeks_global + 1):5}{koleksi_game[indeks_global][0]:45} {koleksi_game[indeks_global][1]:20} {koleksi_game[indeks_global][2]:25} {koleksi_game[indeks_global][3]}")
                        indeks_global += 1
                    print("=" * 110)
                    input("Tekan 'enter' untuk kembali")
                    print("=" * 110)

                    time.sleep(1)
                    os.system("clear")
                    os.system("cls")
                    break

                else: # Jika pengguna menjawab tidak atau dengan jawaban lainnya, maka program akan lanjut ke bagian ini
                    print("=" * 111)
                    print("Tidak jadi hapus!") # Bagian ini memberitahu pengguna kalau game yang dipilih tidak jadi untuk dihapus
                    print("=" * 111)

                    time.sleep(1)
                    os.system("clear")
                    os.system("cls")
                    break

            else: # Program akan menjalankan bagian ini jika pilihan menu delete yang dimasukkan pengguna tidak berada dalam range
                print("=" * 111)
                print("Pilihan tidak valid!") # Menampilkan pesan kalau pilihan pengguna tidak benar
                print("=" * 111)

                time.sleep(1)
                os.system("clear")
                os.system("cls")
    else: # Program akan menjalankan bagian ini jika pilihan menu awal yang dimasukkan peserta tidak benar
        print("=" * 111)
        print("Pilihan tidak valid!")
        print("=" * 111)

        time.sleep(1)
        os.system("clear")
        os.system("cls")

# Bagian ini akan tampak ketika pengguna selesai menggunakan program
print("Program Selesai!")
print("Terimakasih telah menggunakan program ini!")