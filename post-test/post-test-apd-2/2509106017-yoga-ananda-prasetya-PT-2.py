# Bagian Header dari Program
print("-" * 67)
print("|", "PROGRAM MEMERIKSA STATUS BERAT BADAN".center(63), "|")
print("-" * 67)

# Bagian Input nama, tinggi dan berat badan
nama = str(input(f"{'Nama pasien' :32}: "))
tinggi_badan = float(input(f"{'Tinggi badan pasien (dalam cm)' :32}: "))
berat_badan = float(input(f"{'Berat badan pasien (dalam kg)' :32}: "))

# Bagian menghitung berat badan serta pengecekan berat badan
berat_ideal = tinggi_badan - 100
isKelebihan = berat_badan > berat_ideal
status = ["Berat Badan Ideal", "Kelebihan Berat Badan"] # List berfungsi sebagai pengganti dari percabangan IF & ELSE

# Bagian Header dari tabel akhir
print("-" * 67)
print("|", "HASIL CEK BERAT BADAN".center(63), "|")
print("-" * 67)

# Bagian isi dari tabel akhir
print(f"{'|'} {'Nama Pasien' :30}: {nama} {' ' * (30 - len(nama))} {'|'}")
print(f"{'|'} {'Tinggi Badan' :30}: {tinggi_badan:.2f} {' ' * (29 - len(str(tinggi_badan)))} {'|'}")
print(f"{'|'} {"Berat Badan" :30}: {berat_badan:.2f} {' ' * (29 - len(str(berat_badan)))} {'|'}")
print(f"{'|'} {'Berat Ideal' :30}: {berat_ideal:.2f} {' ' * (29 - len(str(berat_ideal)))} {'|'}")
print(f"{'|'} {'Status' :30}: {status[int(isKelebihan)]} {' ' * (30 - len(str(status[int(isKelebihan)])))} {'|'}")
print("-" * 67)
