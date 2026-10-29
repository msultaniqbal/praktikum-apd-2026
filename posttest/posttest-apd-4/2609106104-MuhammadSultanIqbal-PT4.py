# ==========================================
# PROGRAM REKAPITULASI PENGELUARAN BULANAN
# Nama : Iqbal
# NIM  : 104
# ==========================================

USERNAME_BENAR = "iqbal"
PASSWORD_BENAR = "104"

percobaan = 3
login_berhasil = False

while percobaan > 0:
    print("=" * 45)
    print("         SISTEM LOGIN PENGGUNA         ")
    print("=" * 45)
    
    username_input = input("Masukkan Username : ").strip()
    password_input = input("Masukkan Password : ").strip()

    if username_input == "" or password_input == "":
        print("\n[ERROR] Username dan Password tidak boleh kosong!\n")
        continue

    if username_input.lower() == USERNAME_BENAR and password_input == PASSWORD_BENAR:
        print("\n>>> Login Berhasil! Selamat datang, Iqbal <<<\n")
        login_berhasil = True
        break
    else:
        percobaan -= 1
        if percobaan > 0:
            print(f"\n[AKSES DITOLAK] Login Gagal. Sisa percobaan: {percobaan}\n")
        else:
            print("\n[AKSES DIBLOKIR] Batas percobaan habis. Program dihentikan.")

if login_berhasil:
    print("=" * 45)
    print("      INISIALISASI UANG SAKU AWAL      ")
    print("=" * 45)
    
    while True:
        input_uang = input("Masukkan jumlah uang saku awal (Rp): ").strip()
        
        if input_uang == "":
            print("[ERROR] Input tidak boleh kosong!")
        elif not input_uang.isdigit():
            print("[ERROR] Masukkan nominal dalam bentuk angka saja!")
        elif int(input_uang) <= 0:
            print("[ERROR] Uang saku awal harus lebih besar dari 0!")
        else:
            uang_bulanan = int(input_uang)
            break

    total_pengeluaran = 0

    while uang_bulanan > 0:
        print("\n" + "=" * 45)
        print("          MENU UTAMA REKAPITULASI          ")
        print("=" * 45)
        print("[1] Catat Pengeluaran")
        print("[2] Cek Sisa Uang Saku")
        print("[3] Keluar")
        print("=" * 45)
        
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "":
            print("[ERROR] Pilihan menu tidak boleh kosong!")
            continue
        elif pilihan not in ["1", "2", "3"]:
            print("[ERROR] Pilihan menu tidak valid. Pilih angka 1, 2, atau 3!")
            continue

        if pilihan == "1":
            while True:
                input_nominal = input("\nMasukkan nominal pengeluaran (Rp): ").strip()
                
                if input_nominal == "":
                    print("[ERROR] Nominal tidak boleh kosong!")
                    continue
                elif not input_nominal.isdigit():
                    print("[ERROR] Nominal harus berupa angka positif!")
                    continue
                
                nominal = int(input_nominal)

                if nominal <= 0:
                    print("[ERROR] Nominal pengeluaran harus lebih besar dari 0!")
                    continue
                elif nominal > uang_bulanan:
                    print(f"[ERROR] Saldo tidak cukup! Sisa saku Anda saat ini: Rp{uang_bulanan:,}")
                else:
                    uang_bulanan -= nominal
                    total_pengeluaran += nominal
                    print(f"-> Pengeluaran dicatat : Rp{nominal:,}")
                    print(f"-> Sisa Uang Saku      : Rp{uang_bulanan:,}")

                if uang_bulanan <= 0:
                    print("\n[PERINGATAN] Uang saku Anda telah habis!")
                    break

                konfirmasi_valid = False
                pilihan_lanjut = ""
                while not konfirmasi_valid:
                    jawab = input("\nApakah Anda ingin mencatat pengeluaran lagi? (Y/T): ").strip().lower()
                    if jawab in ["y", "t"]:
                        pilihan_lanjut = jawab
                        konfirmasi_valid = True
                    else:
                        print("[ERROR] Input tidak valid! Masukkan 'Y' untuk Ya atau 'T' untuk Tidak.")

                if pilihan_lanjut == "t":
                    break

        elif pilihan == "2":
            print("\n" + "-" * 45)
            print("         INFORMASI SALDO & PENGELUARAN        ")
            print("-" * 45)
            print(f" Total Pengeluaran : Rp{total_pengeluaran:,}")
            print(f" Sisa Uang Saku    : Rp{uang_bulanan:,}")
            print("-" * 45)

        elif pilihan == "3":
            print("\n" + "=" * 45)
            print(" Terima kasih telah menggunakan program ini, Iqbal! ")
            print("=" * 45)
            break

    if uang_bulanan <= 0:
        print("\n" + "=" * 45)
        print(" Program dihentikan karena sisa uang saku telah habis. ")
        print("=" * 45)