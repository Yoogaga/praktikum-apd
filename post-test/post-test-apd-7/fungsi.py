import os
import time 

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

kesempatan = 4

# Fungsi Dasar
def clear(): # Fungsi Untuk Membersihkan Terminal
    time.sleep(1)
    os.system('clear')
    os.system('cls')

def login(): # Fungsi Untuk Login ke Program
    while True:
        try: 
            global konfirmasi_login, kesempatan
            konfirmasi_login = False

            # Bagian Display Menu Login
            print("=" * 75)
            print(f"{'MENU LOGIN':^75}")
            print("=" * 75)
            username_login = input(f"{'Masukkan Username : ':<10}")
            password_login = input(f"{'Masukkan Password : ':<10}")
            print("=" * 75)

            if len(username_login) == 0 or len(password_login) == 0: 
                raise ValueError ("Username atau Password tidak Boleh Kosong!") 

            for id_akun, info in akun.items(): 
                if username_login == info['username'] and password_login == info['password']: # Bagian ini akan berjalan jika informasi yang dimasukkan pengguna sama dengan informasi yang tersimpan di dictionary
                    global role_anda, id_anda, username_anda
                    konfirmasi_login = True # Mengubah status menjadi 'berhasil login'
                    username_anda = info["username"]
                    role_anda = info['role'] # Mengambil role dari pengguna yang login 
                    id_anda = id_akun # Mengambil id akun dari pengguna yang login

                    print("LOGIN BERHASIL")
                    print("=" * 75)
                    clear()

            if konfirmasi_login == True:
                break
            else: 
                print("Login gagal, silahkan coba lagi!")
                kesempatan -= 1
                print(f"Sisa kesempatan : {kesempatan}")
                
                clear()

                if kesempatan == 0: # Memeriksa apakah kesempatan login pengguna sudah habis
                    print("Kesempatan Login habis, silahkan anda membuat sebuah akun!")

                    time.sleep(1)
                    clear()
                    register()
                    kesempatan = 4
                    break
        except ValueError as e: 
            print(e)
            time.sleep(1)
            clear()
    
    return konfirmasi_login

def register(): # Fungsi untuk membuat sebuah akun
    while True:
        try:
            print("=" * 50)
            print(f"{'MEMBUAT AKUN BARU':^50}")
            print("=" * 50)

            # Input Username dan Password
            username_baru = input("Masukkan Username : ")
            password_baru = input("Masukkan Password : ")

            clear()

            # Bagian yang memeriksa apakah ada elemen yang kosong
            if len(username_baru) and len(password_baru) != 0:
                print("=" * 60)
                print(f"{'KONFIRMASI AKUN BARU':^60}")
                print("=" * 60)

                print(f"{'Username':<20}: {username_baru}")
                print(f"{'Password':<20}: {password_baru}")

                # Bagian Konfirmasi akun
                print("=" * 60)
                print("Apakah informasi akun sudah benar? (y/n)")
                print("=" * 60)
                konfirmasi_regis = input("> ")

                clear()

                if konfirmasi_regis == "y": # Akan mendaftarkan aku ketika pengguna mengetik 'y'
                    id_akun = f"acc{len(akun) + 1}"

                    akun[id_akun] = {
                        "username": username_baru, 
                        "password": password_baru, 
                        "role": "member",
                        "game": {}
                    }
                    print("=" * 60)
                    print("Akun berhasil dibuat!")
                    input("Tekan 'Enter' untuk Kembali")
                    print("=" * 60)
                    clear()
                    break
                    
                elif konfirmasi_regis == "n": # Jika mengetik 'n' maka pengguna akan mengulang proses registrasi
                    print("Mengulang Proses")
                    clear()
                else: # Akan berjalan jika pengguna salah input
                    print("Pilihan tidak valid")
                    clear()
            
            elif len(username_baru) == 0: # Akan berjalan jika ada elemen yang kosong
                raise ValueError("Username Tidak Boleh Kosong")
            elif len(password_baru) == 0: 
                raise ValueError("Password Tidak Boleh Kosong")
            elif len(username_baru) and len(password_baru) == 0:
                raise ValueError("Username dan Password Tidak boleh kosong")
        
        except ValueError as e: 
            print(e)
            clear()

# Fungsi Untuk Member
def tambah_game(): 
    while True:
        # Bagian Display Menu
        print("=" * 74)
        print(f"{'MENAMBAHKAN GAME KE DIREKTORI':^74}")
        print("=" * 74)

        # Bagian Input game beserta beberapa elemen lainnya
        game_baru = input(f"{'Masukkan Judul Game':<35}: ")
        tahun_rilis = input(f"{'Masukkan Tahun Rilis Game':<35}: ")
        developer_game = input(f"{'Masukkan Developer Game':<35}: ")
        status_game = input(f"{'Masukkan Status Game':<35}: ")
        print("=" * 74)

        clear()

        if game_baru and tahun_rilis and developer_game and status_game != 0: # Jika semua data terisi, program lanjut ke bagian ini
            # Bagian ini menampilkan informasi terkait game baru yang akan dimasukkan ke direktori
            print("=" * 74)
            print(f"{'INFORMASI GAME BARU':^74}")
            print("=" * 74)
            print(f"{'Judul Game':<30} {'Tahun Rilis':<15} {'Developer':<20} {'Status':<10}")
            print(f"{game_baru:<30} {tahun_rilis:<15} {developer_game:<20} {status_game:<10}")

            print("=" * 74)
            input("Tekan 'Enter' untuk kembali...")
            print("=" * 74)

            clear()

            id_game_baru = f"g{len(akun[id_anda]['game']) + 1}" # Membuat ID baru untuk game yang baru ditambahkan

            # Menambahkan game ke dalam direktori
            akun[id_anda]['game'][id_game_baru] = {
                "nama": game_baru, 
                "tahun": tahun_rilis, 
                "dev": developer_game, 
                "status": status_game
            }
            break
        
        else: # Bagian ini akan dijalankan jika ada informasi game yang kosong
            print("=" * 74)
            print("Tidak Boleh ada yang kosong!")
            print("=" *74)

            clear()

def lihat_game(): 
    # Bagian Display menu
    print("=" * 90)
    print(f"{'KOLEKSI GAME':^90}")
    print("=" * 90)
    print(f"{'ID':<5} {'Judul Game':<30} {'Tahun Rilis':<15} {'Developer':<20} {'Status':<10}")
    for gid, game in akun[id_anda]['game'].items():
        print(f"{gid:<5} {game['nama']:<30} {game['tahun']:<15} {game['dev']:<20} {game['status']:<10}")

    print("=" * 90)
    input("Tekan 'Enter' untuk kembali ke menu utama...")
    print("=" * 90)

    clear()

def update_game(): 
    while True: 
        game_update_benar = False # Merupakan parameter yang melihat apakah id game yang dimasukkan pengguna benar atau tidak
        # Display menu
        print("=" * 90)
        print(f"{'MENU UPDATE':^90}")
        print("=" * 90)
        print(f"{'ID':<5} {'Judul Game':<30} {'Tahun Rilis':<15} {'Developer':<20} {'Status':<10}")
        for gid, game in akun[id_anda]['game'].items():
            print(f"{gid:<5} {game['nama']:<30} {game['tahun']:<15} {game['dev']:<20} {game['status']:<10}")

        print("=" * 90)
        print(f"{'0':<5} Keluar")
        print("=" * 90)

        # Input ID game yang ingin diupdate
        print("Pilih ID Game yang Ingin Anda Update :")
        print("=" * 90)
        pilih_update = input("> ")

        clear()

        if pilih_update == "0": # Jika input == 0, maka pengguna akan dikeluarkan dari Menu Update
            break

        # Bagian ini digunakan untuk memeriksa apakah ID game yang dimasukkan oleh pengguna ada di dictionary
        for gid, game in akun[id_anda]["game"].items(): 
            if pilih_update == gid: # Program ini akan berjalan jika ID game yang dimasukkan oleh pengguna sama dengan ID game yang ada di dictionary
                while True: 
                    # Display menu
                    print("=" * 74)
                    print(f"{'GAME YANG INGIN DIUPDATE':^74}")
                    print("=" * 74)

                    print(f"{'1 - Judul Game':<25}: {game['nama']}")
                    print(f"{'2 - Tahun Rilis':<25}: {game['tahun']}")
                    print(f"{'3 - Developer':<25}: {game['dev']}")
                    print(f"{'4 - Status':<25}: {game['status']}")
                    game_update_benar = True # Memberi tahu ke program kalau ID game yang dimasukkan benar

                    print("=" * 74)
                    print("0 - Keluar")
                    print("=" * 74)

                    # Bagian Input Informasi game yang ingin di ubah
                    print("Masukkan bagian yang ingin diubah:")
                    print("=" * 74)
                    menu_update = input("> ")
                    print("=" * 74)

                    clear()
                    if menu_update == "0": # Jika pengguna memasukkan 0, maka pengguna akan kembali ke Menu Update
                        break
                    elif menu_update == "1": # Bagian ini berfungsi untuk mengganti judul game
                        while True:
                            # Display Menu
                            print("=" * 74)
                            print(f"{'MENGUBAH JUDUL GAME':^74}")
                            print("=" * 74)

                            # Bagian Input judul game yang baru
                            print(f"{'Judul game lama':<30} : {game['nama']}") # Menampilkan judul game yang lama
                            ganti_judul = input(f"{'Masukkan judul game baru':<30} : ") # Pengguna memasukkan judul game yang baru

                            if len(ganti_judul) != 0: # Memeriksa apakah panjang karakter dari judul yang dimasukkan
                                akun[id_anda]['game'][pilih_update].update({'nama': ganti_judul}) # Mengganti judul game dengan judul yang telah dimasukkan oleh pengguna
                                
                                clear()
                                break

                            else: # Bagian ini akan berjalan jika pengguna tidak memasukkan apa apa ke bagian ganti judul
                                print("=" * 25)
                                print("Tidak boleh kosong!")
                                print("=" * 25)

                                clear()

                    elif menu_update == "2": # Bagian ini berfungsi untuk mengganti tahun rilis dari game
                        while True: 
                            # Display menu
                            print("=" * 74)
                            print(f"{'MENGUBAH TAHUN RILIS GAME':^74}")
                            print("=" * 74)

                            # Bagian Input tahun rilis yang baru
                            print(f"{'Tahun Rilis Awal':<30} : {game['tahun']}") # Menampilkan tahun rilis yang lama
                            ganti_tahun = input(f"{'Masukkan Tahun Rilis baru':<30} : ") # Pengguna memasukkan tahhun rilis yang baru

                            if len(ganti_tahun) != 0: # Memeriksa panjang karakter dari tahun yang telah diisi oleh penggun
                                akun[id_anda]['game'][pilih_update].update({'tahun': ganti_tahun}) # Mengganti tahun rilis dengan tahun yang telah dimasukkan oleh pengguna
                                
                                clear()
                                break
                            else: # Bagian akan berjalan jika pengguna tidak mengisi Tahun rilis yang baru
                                print("=" * 25)
                                print("Pilihan tidak valid")
                                print("=" * 25)

                                clear()

                    elif menu_update == "3": # Bagian ini berfungsi untuk mengganti developer game
                        while True:
                            print("=" * 74)
                            print(f"{'MENGUBAH DEVELOPER GAME':^74}")
                            print("=" * 74)

                            print(f"{'Developer Awal':<30} : {game['dev']}")
                            ganti_developer = input(f"{'Masukkan Developer yang baru':<30} : ")
                            
                            if len(ganti_developer) != 0: 
                                akun[id_anda]['game'][pilih_update].update({'dev': ganti_developer})
                                
                                clear
                                break
                            else: 
                                print("=" * 25)
                                print("Pilihan Anda Tidak Valid")
                                print("=" * 25)

                                clear()

                    elif menu_update == "4": # Bagian ini berfungsi untuk mengganti status game
                        while True:    
                            print("=" * 74)
                            print(f"{'MENGUBAH STATUS GAME':^74}")
                            print("=" * 74)

                            print(f"{'Status Awal':<30} : {game['status']}")
                            ganti_status = input(f"{'Masukkan status yang baru':<30} : ")

                            if len(ganti_status) != 0: 
                                akun[id_anda]['game'][pilih_update].update({'status': ganti_status})
                                
                                clear()
                                break
                            else: 
                                print("=" * 25)
                                print("Pilihan Anda tidak valid")
                                print("=" * 25)

                                clear()
                    else: 
                        print("=" * 25)
                        print("Pilihan tidak valid.")
                        print("=" * 25)

                        clear()

        if game_update_benar == False: # Bagian ini akan berjalan jika pengguna memasukkan ID yang salah
            print("=" * 25)
            print("Pilihan tidak valid")
            print("=" * 25)

            clear()

def hapus_game(): 
    while True: 
        selesai_delete = False # Merupakan parameter yang mengatur apakah pengguna sudah selesai menghapus atau belum
        # Display Menu
        print("=" * 90)
        print(f"{'MENU HAPUS':^90}")
        print("=" * 90)
        print(f"{'ID':<5} {'Judul Game':<30} {'Tahun Rilis':<15} {'Developer':<20} {'Status':<10}")
        for gid, game in akun[id_anda]['game'].items():
            print(f"{gid:<5} {game['nama']:<30} {game['tahun']:<15} {game['dev']:<20} {game['status']:<10}")

        print("=" * 90)
        print(f"{'0':<5} Keluar")
        print("=" * 90)

        # Bagian input ID game yang ingin dihapus
        print("Masukkan ID Game yang ingin Anda hapus :")
        print("=" * 90)
        pilih_hapus = input("> ")

        clear()

        if pilih_hapus == "0": 
            break
        
        # Bagian ini memeriksa apakah ID yang dimasukkan pengguna ada di dictionary atau tidak
        for gid, game in akun[id_anda]["game"].items(): 
            if pilih_hapus == gid:
                while True: 
                    # Menampilkan game yang ingin dihapus
                    print("=" * 90)
                    print(f"{'GAME YANG INGIN DIHAPUS':^90}")
                    print("=" * 90)
                    print(f"{'ID':<5} {'Judul Game':<30} {'Tahun Rilis':<15} {'Developer':<20} {'Status':<10}")
                    print(f"{gid:<5} {game['nama']:<30} {game['tahun']:<15} {game['dev']:<20} {game['status']:<10}")

                    # Bagian konfirmasi apakah pengguna yakin ingin menghapus game
                    print("=" * 90)
                    print("Apakah anda yakin ingin menghapus game ini? (y/n):")
                    print("=" * 90)
                    konfirmasi_hapus = input("> ")
                    print("=" * 90)

                    if konfirmasi_hapus == "y": # Bagian ini akan menghapus game yang sudah dipilih secara permanen
                        del akun[id_anda]['game'][pilih_hapus] # Menghapus game

                        # Bagian ini merupakan bagian reordering ID game yang tersisa
                        games_lama = akun[id_anda]['game']
                        games_baru = {}
                        nomor = 1

                        # Bagian ini berfungsi untuk membuat ulang ID game setelah ada satu game yang dihapus
                        for _, data in games_lama.items(): 
                            new_id = f"g{nomor}"
                            games_baru[new_id] = data
                            nomor += 1
                        
                        # Menyatukan perubahan yang ada pada proses sebelumnya
                        akun[id_anda]['game'] = games_baru
                        selesai_delete = True # Memberikan tanda kalau proses delete sudah selesai

                        os.system('clear')
                        os.system('cls')
                        break
                    else: # Akan berjalan jika pengguna tidak jadi menghapus game
                        print("Tidak jadi hapus!")
                        os.system('clear')
                        os.system('cls')
                        break

            if selesai_delete == True: # Akan berjalan jika penggguna selesai melakukan proses delete
                break

# Fungsi Untuk Admin
def menu_admin(): 
    while True: 
        # Display menu
        print("=" * 50)
        print(f"{'MENU ADMIN':^50}")
        print("=" * 50)

        print("1 - Tambahkan Akun")
        print("2 - Lihat Akun")
        print("3 - Update Info Akun")
        print("4 - Hapus Akun")
        print("=" * 50)

        print("0 - Keluar")
        print("=" * 50)

        print("Pilih Menu yang Anda Inginkan :")
        print("=" * 50)
        menu_admin = input("> ")

        clear()

        if menu_admin == "0": # Keluar dari Menu Admin 
            break
        elif menu_admin == "1": 
            register()
        elif menu_admin == "2":
            lihat_akun()
        elif menu_admin == "3": 
            update_akun()
        elif menu_admin == "4":
            hapus_akun()

def lihat_akun(): 
    # Menampilkan semua informasi aku yang ada pada dictionary
    print("=" * 60)
    print(f"{'AKUN-AKUN YANG TERDAFTAR':^60}")
    print("=" * 60)

    print(f"{'ID':<5} {'Nama Akun':<20} {'Password':<20} {'Role':<10}")
    for id_acc, info_akun in akun.items():
        print(f"{str(id_acc):<5} {info_akun['username']:<20} {info_akun['password']:<20} {info_akun['role']:<10}")

    print("=" * 60)
    input("Tekan 'Enter' untuk kembali ke Menu Admin... ")
    print("=" * 60)

    clear()

def update_akun(): 
    while True:
        # Bagian ini berfungsi untuk mengganti Username, Password, dan juga role dari akun-akun yang ada
        # Prinsip kerjanya kurang lebih sama dengan proses Update yang ada pada menu "Update Informasi Game"
        print("=" * 70)
        print(f"{'UPDATE INFORMASI AKUN':^70}")
        print("=" * 70)

        print(f"{'ID':<5} {'Nama Akun':<25} {'Password':<25} {'Role'}")
        for id_acc, info_akun in akun.items():
            print(f"{str(id_acc):<5} {info_akun['username']:<25} {info_akun['password']:<25} {info_akun['role']}")

        print("=" * 70)
        print(f"{'0':<5} Keluar")
        print("=" * 70)
        print("Masukkan ID Pengguna yang Ingin Anda Ubah:")
        admin_update = input("> ")
        print("=" * 70)

        clear()

        if admin_update == "0": 
            break

        for id_acc, info_akun in akun.items(): 
            if admin_update == id_acc:
                while True: 
                    print("=" * 70)
                    print(f"{'INFORMASI AKUN YANG DIUBAH':^70}")
                    print("=" * 70)

                    print(f"{'1 - Username Pengguna':<30}: {info_akun['username']}")
                    print(f"{'2 - Password Pengguna':<30}: {info_akun['password']}")
                    print(f"{'3 - Role Pengguna':<30}: {info_akun['role']}")
                    status_admin_update = True

                    print("=" * 70)
                    print("0 - Keluar")
                    print("=" * 70)
                    print("Masukkan bagian yang ingin diubah :")
                    print("=" * 70)
                    menu_update = input("> ")
                    print("=" * 70)

                    clear()

                    if menu_update == "0": 
                        break
                    elif menu_update == "1": 
                        while True:
                            print("=" * 70)
                            print(f"{'UPDATE USERNAME':^70}")
                            print("=" * 70)
                            print(f"{'Username Lama':<30} : {info_akun['username']}")
                            ganti_username = input(f"{'Masukkan username baru':<30} : ")
                            print("=" * 70)

                            clear()

                            if len(ganti_username) != 0: 
                                akun[id_acc].update({'username': ganti_username})
                                break
                            else: 
                                print("Pilihan Tidak Valid")
                                clear()

                    elif menu_update == "2": 
                        while True: 
                            print("=" * 70)
                            print(f"{'UPDATE PASSWORD':^70}")
                            print("=" * 70)
                            print(f"{'Password Lama':<30} : {info_akun['password']}")
                            ganti_password = input(f"{'Masukkan Password Baru':<30} : ")
                            print("=" * 70)

                            clear()

                            if len(ganti_password) != 0:
                                akun[id_acc].update({'password': ganti_password})
                                break
                            else:
                                print("Pilihan tidak valid")
                                clear()

                    elif menu_update == "3": 
                        while True:
                            print("=" * 70)
                            print(f"{'UPDATE ROLE':^70}")
                            print("=" * 70)
                            print(f"{'Role Sebelumnya':<35} : {info_akun['role']}")
                            ganti_role = input(f"{'Ubah role akun ini (member/admin)':<35} : ")
                            print("=" * 70)

                            clear()

                            if len(ganti_role) != 0 and (ganti_role == "admin" or ganti_role == "member"):
                                akun[id_acc].update({'role': ganti_role})
                                break 
                            else:
                                print("Pastikan anda memasukkan data dengan benar!") 
                                clear()

def hapus_akun(): 
    while True:
        global akun
        selesai_delete = False
        print("=" * 70)
        print(f"{'HAPUS AKUN':^70}")
        print("=" * 70)

        print(f"{'ID':<5} {'Nama Akun':<25} {'Password':<25} {'Role'}")
        for id_acc, info_akun in akun.items():
            print(f"{str(id_acc):<5} {info_akun['username']:<25} {info_akun['password']:<25} {info_akun['role']}")

        print("=" * 70)
        print(f"{'0':<5} Kembali")
        print("=" * 70)
        print("Masukkan ID akun yang ingin dihapus :")
        print("=" * 70)
        pilih_hapus = input("> ")
        print("=" * 70)

        clear()

        if pilih_hapus == "0": 
            break

        for id_acc, info_akun in akun.items(): 
            if pilih_hapus == id_acc: 
                print("=" * 70)
                print(f"{'KONFIRMASI HAPUS AKUN':^70}")
                print("=" * 70)

                print(f"{'ID':<5} {'Nama Akun':<25} {'Password':<25} {'Role'}")
                print(f"{pilih_hapus:<5} {info_akun['username']:<25} {info_akun['password']:<25} {info_akun['role']}")
                print("=" * 70)

                print("Apakah Anda yakin ingin menghapus akun ini (y/n)?")
                print("=" * 70)
                konfirmasi_hapus = input("> ")
                print("=" * 70)

                clear()

                if konfirmasi_hapus == "y": 
                    del akun[pilih_hapus]
                    akun_lama = akun
                    akun_baru = {}
                    nomor = 1

                    for _, data in akun_lama.items(): 
                        new_id = f"acc{nomor}"
                        akun_baru[new_id] = data
                        nomor += 1
                    
                    akun = akun_baru
                    selesai_delete = True
                    break
                else: 
                    print("Tidak jadi hapus!")
                    clear()
                    break
            
        if selesai_delete == True:
            break     
