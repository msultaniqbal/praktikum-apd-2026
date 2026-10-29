# ==========================================
# PROGRAM RESERVASI BARBERSHOP (DICTIONARY)
# ==========================================

# Inisialisasi dictionary utama untuk menyimpan data reservasi
# Menggunakan ID/Kode Reservasi sebagai key, dan dictionary detail sebagai value
daftar_reservasi = {}
nomor_id = 1

while True:
    print("\n" + "=" * 50)
    print("      APLIKASI RESERVASI BARBERSHOP (DICT)")
    print("=" * 50)
    print("1. Tambah Reservasi (Create)")
    print("2. Lihat Daftar Reservasi (Read)")
    print("3. Ubah Reservasi (Update)")
    print("4. Hapus Reservasi (Delete)")
    print("5. Keluar")
    print("=" * 50)
    
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
                
            waktu = input("Masukkan Waktu/Jam (Contoh: 15.00 WITA): ")
            
            # Membuat key unik untuk setiap data reservasi baru
            kunci_id = f"RES-{nomor_id}"
            
            # Operasi CREATE: Menambahkan nested dictionary ke dalam dictionary utama
            daftar_reservasi[kunci_id] = {
                "nama": nama,
                "barber": barber,
                "paket": paket,
                "waktu": waktu
            }
            
            print(f"\n[SUKSES] Reservasi berhasil ditambahkan dengan Kode: {kunci_id}!")
            nomor_id += 1
            
        elif menu == 2:
            print("\n--- DAFTAR RESERVASI BARBERSHOP ---")
            if len(daftar_reservasi) == 0:
                print("Belum ada data reservasi.")
            else:
                print("Kode    | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 85)
                # Operasi READ: Menggunakan .items() untuk menampilkan key dan value dictionary
                for kode_id, info in daftar_reservasi.items():
                    print(f"{kode_id:<7} | {info['nama']:<19} | {info['barber']:<13} | {info['paket']:<25} | {info['waktu']}")
                print("-" * 85)
                
        elif menu == 3:
            print("\n--- UBAH DATA RESERVASI (UPDATE) ---")
            if len(daftar_reservasi) == 0:
                print("Belum ada data reservasi untuk diubah.")
            else:
                print("Kode    | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 85)
                for kode_id, info in daftar_reservasi.items():
                    print(f"{kode_id:<7} | {info['nama']:<19} | {info['barber']:<13} | {info['paket']:<25} | {info['waktu']}")
                print("-" * 85)
                
                target_id = input("Masukkan Kode Reservasi yang ingin diubah (Contoh: RES-1): ").upper()
                
                # Memeriksa apakah key ada di dalam dictionary
                if target_id in daftar_reservasi:
                    print(f"\nMengubah data untuk reservasi dengan kode: {target_id}")
                    nama_baru = input("Masukkan Nama Pelanggan Baru : ")
                    barber_baru = input("Masukkan Nama Barber Baru   : ")
                    paket_baru = input("Masukkan Paket Layanan Baru : ")
                    waktu_baru = input("Masukkan Waktu Baru         : ")
                    
                    # Operasi UPDATE: Memperbarui nilai dictionary menggunakan update()
                    daftar_reservasi[target_id].update({
                        "nama": nama_baru,
                        "barber": barber_baru,
                        "paket": paket_baru,
                        "waktu": waktu_baru
                    })
                    print("\n[SUKSES] Data reservasi berhasil diperbarui!")
                else:
                    print("\n[GAGAL] Kode reservasi tidak ditemukan.")
                    
        elif menu == 4:
            print("\n--- HAPUS DATA RESERVASI (DELETE) ---")
            if len(daftar_reservasi) == 0:
                print("Belum ada data reservasi untuk dihapus.")
            else:
                print("Kode    | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 85)
                for kode_id, info in daftar_reservasi.items():
                    print(f"{kode_id:<7} | {info['nama']:<19} | {info['barber']:<13} | {info['paket']:<25} | {info['waktu']}")
                print("-" * 85)
                
                target_id = input("Masukkan Kode Reservasi yang ingin dihapus (Contoh: RES-1): ").upper()
                
                if target_id in daftar_reservasi:
                    # Operasi DELETE: Menghapus elemen dari dictionary menggunakan pop()
                    data_terhapus = daftar_reservasi.pop(target_id)
                    print(f"\n[SUKSES] Reservasi atas nama {data_terhapus['nama']} (Kode: {target_id}) berhasil dihapus!")
                else:
                    print("\n[GAGAL] Kode reservasi tidak ditemukan.")
                    
        elif menu == 5:
            print("\nTerima kasih telah menggunakan aplikasi reservasi barbershop!")
            break
        else:
            print("\n[GAGAL] Pilihan menu tidak valid. Masukkan angka 1 sampai 5.")
    else:
        print("\n[GAGAL] Input tidak valid. Harap masukkan angka.")