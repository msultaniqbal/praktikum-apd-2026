# ==========================================
# PROGRAM RESERVASI BARBERSHOP (CRUD)
# ==========================================

# Inisialisasi list utama untuk menyimpan data reservasi
# Format elemen: [nama_pelanggan, nama_barber, paket_layanan, waktu]
daftar_reservasi = []

while True:
    print("\n" + "=" * 45)
    print("      APLIKASI RESERVASI BARBERSHOP")
    print("=" * 45)
    print("1. Tambah Reservasi (Create)")
    print("2. Lihat Daftar Reservasi (Read)")
    print("3. Ubah Reservasi (Update)")
    print("4. Hapus Reservasi (Delete)")
    print("5. Keluar")
    print("=" * 45)
    
    pilihan = input("Pilih menu (1-5): ")
    
    # Validasi menu utama tanpa try-except
    if pilihan.isdigit():
        menu = int(pilihan)
        
        if menu == 1:
            print("\n--- TAMBAH RESERVASI BARU ---")
            nama = input("Masukkan Nama Pelanggan : ")
            barber = input("Masukkan Nama Barber   : ")
            print("Pilih Paket Layanan:")
            print("1. Haircut (Potong Rambut)")
            print("2. Haircut + Shaving (Cukur Jenggot)")
            print("3. Full Treatment (Potong + Cuci + Styling)")
            pilihan_paket = input("Pilih paket (1-3): ")
            
            if pilihan_paket == "1":
                paket = "Haircut"
            elif pilihan_paket == "2":
                paket = "Haircut + Shaving"
            elif pilihan_paket == "3":
                paket = "Full Treatment"
            else:
                paket = "Haircut Standar"
                
            waktu = input("Masukkan Waktu/Jam (Contoh: 20.00 WITA): ")
            
            # Operasi CREATE: Menambahkan data ke dalam list
            reservasi_baru = [nama, barber, paket, waktu]
            daftar_reservasi.append(reservasi_baru)
            print("\n[SUKSES] reservasi berhasil ditambahkan!")
            
        elif menu == 2:
            print("\n--- DAFTAR RESERVASI BARBERSHOP ---")
            if len(daftar_reservasi) == 0:
                print("Belum ada data reservasi.")
            else:
                print("No | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 75)
                
                # Operasi READ: Menampilkan seluruh isi list
                for indeks, data in enumerate(daftar_reservasi):
                    print(f"{indeks + 1:<2} | {data[0]:<19} | {data[1]:<13} | {data[2]:<25} | {data[3]}")
                print("-" * 75)
                
        elif menu == 3:
            print("\n--- UBAH DATA RESERVASI (UPDATE) ---")
            if len(daftar_reservasi) == 0:
                print("Belum ada data reservasi untuk diubah.")
            else:
                print("No | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 75)
                for indeks, data in enumerate(daftar_reservasi):
                    print(f"{indeks + 1:<2} | {data[0]:<19} | {data[1]:<13} | {data[2]:<25} | {data[3]}")
                print("-" * 75)
                
                pilih_index = input("Masukkan nomor reservasi yang ingin diubah: ")
                if pilih_index.isdigit():
                    idx = int(pilih_index) - 1
                    if idx >= 0 and idx < len(daftar_reservasi):
                        print(f"\nMengubah data untuk: {daftar_reservasi[idx][0]}")
                        nama_baru = input("Masukkan Nama Pelanggan Baru : ")
                        barber_baru = input("Masukkan Nama Barber Baru   : ")
                        paket_baru = input("Masukkan Paket Layanan Baru : ")
                        waktu_baru = input("Masukkan Waktu Baru         : ")
                        
                        # Operasi UPDATE: Memperbarui elemen di dalam list
                        daftar_reservasi[idx] = [nama_baru, barber_baru, paket_baru, waktu_baru]
                        print("\n[SUKSES] Data reservasi berhasil diperbarui!")
                    else:
                        print("\n[GAGAL] Nomor reservasi tidak ditemukan.")
                else:
                    print("\n[GAGAL] Masukan harus berupa angka.")
                    
        elif menu == 4:
            print("\n--- HAPUS DATA RESERVASI (DELETE) ---")
            if len(daftar_reservasi) == 0:
                print("Belum ada data reservasi untuk dihapus.")
            else:
                print("No | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 75)
                for indeks, data in enumerate(daftar_reservasi):
                    print(f"{indeks + 1:<2} | {data[0]:<19} | {data[1]:<13} | {data[2]:<25} | {data[3]}")
                print("-" * 75)
                
                pilih_index = input("Masukkan nomor reservasi yang ingin dihapus: ")
                if pilih_index.isdigit():
                    idx = int(pilih_index) - 1
                    if idx >= 0 and idx < len(daftar_reservasi):

                        # Operasi DELETE: Menghapus elemen dari list menggunakan pop
                        data_terhapus = daftar_reservasi.pop(idx)
                        print(f"\n[SUKSES] reservasi atas nama {data_terhapus[0]} berhasil dihapus!")
                    else:
                        print("\n[GAGAL] Nomor reservasi tidak ditemukan.")
                else:
                    print("\n[GAGAL] Masukan harus berupa angka.")
                    
        elif menu == 5:
            print("\nTerima kasih telah menggunakan aplikasi reservasi barbershop!")
            break
        else:
            print("\n[GAGAL] Pilihan menu tidak valid. Masukkan angka 1 sampai 5.")
    else:
        print("\n[GAGAL] Input tidak valid. Harap masukkan angka.") 