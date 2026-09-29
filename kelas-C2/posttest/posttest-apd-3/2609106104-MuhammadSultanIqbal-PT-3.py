NAMA_BENAR = "iqbale"
NIM_BENAR = "104"    

print("=" * 45)
print("   SYSTEM LOGIN RENTAL PLAYSTATION   ")
print("=" * 45)

nama_input = input("Masukkan Nama Panggilan : ").strip().lower()
nim_input = input("Masukkan 3 Digit NIM : ").strip()

if nama_input == NAMA_BENAR and nim_input == NIM_BENAR:
    print("\n[+] Login Berhasil! Selamat datang.\n")

    print("=" * 45)
    print("   PILIHAN JENIS KONSOL PS   ")
    print("=" * 45)
    print("1. PS4     - Rp 10.000 / jam")
    print("2. PS4 Pro - Rp 15.000 / jam")
    print("3. PS5     - Rp 20.000 / jam")
    print("=" * 45)

    pilihan = input("Pilih jenis konsol (1-3): ").strip()

    if pilihan == "1":
        nama_konsol = "PS4"
        harga_per_jam = 10000
    elif pilihan == "2":
        nama_konsol = "PS4 Pro"
        harga_per_jam = 15000
    elif pilihan == "3":
        nama_konsol = "PS5"
        harga_per_jam = 20000
    else:
        nama_konsol = None

    if nama_konsol is not None:
        jumlah_jam = float(input("Masukkan jumlah jam sewa : "))

        total_harga = harga_per_jam * jumlah_jam

        if jumlah_jam >= 5:
            persen_diskon = 0.08
        elif jumlah_jam >= 3:
            persen_diskon = 0.05
        else:
            persen_diskon = 0.0

        diskon_durasi = total_harga * persen_diskon
        
        print("\n--- KETENTUAN WAKTU SEWA ---")
        print("1. Weekday (Senin - Jumat)")
        print("2. Weekend (Sabtu - Minggu)")
        waktu_sewa = input("Pilih waktu sewa (1/2): ").strip()
        
        if waktu_sewa == "2":
            status_waktu = "Weekend (+10%)"
            tambahan_weekend = total_harga * 0.10
        else:
            status_waktu = "Weekday"
            tambahan_weekend = 0.0

        total_bayar = total_harga - diskon_durasi + tambahan_weekend

        print("\n" + "=" * 45)
        print("            NOTA TRANSAKSI RENTAL            ")
        print("=" * 45)
        print(f"Nama Penyewa     : {nama_input.capitalize()}")
        print(f"NIM Penyewa      : {nim_input}")
        print(f"Jenis Konsol     : {nama_konsol}")
        print(f"Lama Sewa        : {jumlah_jam} Jam")
        print(f"Waktu Sewa       : {status_waktu}")
        print("-" * 45)
        print(f"Total Harga Awal : Rp {total_harga:,.0f}")
        print(f"Diskon Durasi    : Rp {diskon_durasi:,.0f}")
        print(f"Tambahan Weekend : Rp {tambahan_weekend:,.0f}")
        print("-" * 45)
        print(f"TOTAL BAYAR      : Rp {total_bayar:,.0f}")
        print("=" * 45)

    else:
        print("\n[-] Pilihan konsol tidak valid (harus 1-3). Program berhenti.")

else:
    print("\n[-] Login Gagal! Nama atau NIM tidak sesuai. Program berhenti.")