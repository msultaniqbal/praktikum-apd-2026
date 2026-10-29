daftar_reservasi = {}
nomor_id = 1
NAMA_BARBERSHOP = "BARBERSTUDIO"

def tampilkan_header():
    print("\n" + "=" * 55)
    print(f"      SELAMAT DATANG DI {NAMA_BARBERSHOP}")
    print("=" * 55)

def cetak_notifikasi(pesan):
    print(f"[INFO SISTEM]: {pesan}")

def pilih_menu():
    print("\n[ MENU UTAMA ]")
    print("1. Tambah Reservasi (Create)")
    print("2. Lihat Daftar Reservasi (Read)")
    print("3. Ubah Reservasi (Update)")
    print("4. Hapus Reservasi (Delete)")
    print("5. Keluar")
    pilihan_menu = input("Pilih menu (1-5): ")
    return pilihan_menu

def hitung_total_reservasi():
    total_data = len(daftar_reservasi)
    return total_data

def proses_tambah_reservasi(id_baru, data_baru):
    # Variabel Lokal (1, 2, 3, 4, 5)
    lokal_status = True
    lokal_pesan = "Berhasil"
    lokal_id = id_baru
    lokal_data = data_baru
    lokal_counter = 1
    
    try:
        daftar_reservasi[lokal_id] = lokal_data
        if lokal_counter == 1:
            pass
    except Exception as e:
        lokal_status = False
        lokal_pesan = str(e)
    else:
        cetak_notifikasi(f"Data dengan ID {lokal_id} berhasil dimasukkan.")
    finally:
        print(f"Status Eksekusi Tambah Data: {lokal_status}")
        
    return lokal_status

def cari_id_reservasi(target_id):
    lokal_target = target_id
    lokal_ada = False
    lokal_info = {}
    lokal_iterasi = 0
    lokal_keterangan = "Pengecekan selesai"
    
    try:
        if lokal_target in daftar_reservasi:
            lokal_ada = True
            lokal_info = daftar_reservasi[lokal_target]
        else:
            raise KeyError("ID Reservasi tidak ditemukan di dalam database.")
    except KeyError as error_key:
        cetak_notifikasi(f"Kesalahan: {error_key}")
    else:
        lokal_iterasi += 1
    finally:
        print(f"Proses verifikasi ID selesai. (Iterasi ke-{lokal_iterasi})")
        
    return lokal_ada, lokal_info

while True:
    tampilkan_header()
    menu_pilihan = pilih_menu()

    try:
        if not menu_pilihan.isdigit():
            raise ValueError("Menu harus berupa angka antara 1 sampai 5!")
        
        menu = int(menu_pilihan)

        if menu == 1:
            print("\n--- TAMBAH RESERVASI BARU ---")
            nama_pelanggan = input("Masukkan Nama Pelanggan : ")
            barber_pilihan = input("Masukkan Nama Barber   : ")
            print("Pilih Paket Layanan:")
            print("1. Haircut")
            print("2. Haircut + Shaving")
            print("3. Full Treatment")
            pilihan_paket = input("Pilih paket (1-3): ")
            
            if pilihan_paket == "1":
                paket_layanan = "Haircut"
            elif pilihan_paket == "2":
                paket_layanan = "Haircut + Shaving"
            elif pilihan_paket == "3":
                paket_layanan = "Full Treatment"
            else:
                paket_layanan = "Haircut Standar"
                
            waktu_reservasi = input("Masukkan Waktu/Jam (Contoh: 15.00 WITA): ")
            
            kunci_id = f"RES-{nomor_id}"
            paket_data_baru = {
                "nama": nama_pelanggan,
                "barber": barber_pilihan,
                "paket": paket_layanan,
                "waktu": waktu_reservasi
            }
            berhasil = proses_tambah_reservasi(kunci_id, paket_data_baru)
            if berhasil:
                nomor_id += 1
                
        elif menu == 2:
            print("\n--- DAFTAR RESERVASI BARBERSHOP ---")
            total = hitung_total_reservasi()
            if total == 0:
                print("Belum ada data reservasi.")
            else:
                print(f"Total Reservasi Aktif: {total}")
                print("Kode    | Nama Pelanggan      | Barber        | Paket Layanan             | Waktu")
                print("-" * 85)
                for kode_id, info in daftar_reservasi.items():
                    print(f"{kode_id:<7} | {info['nama']:<19} | {info['barber']:<13} | {info['paket']:<25} | {info['waktu']}")
                print("-" * 85)
                
        elif menu == 3:
            print("\n--- UBAH DATA RESERVASI (UPDATE) ---")
            if hitung_total_reservasi() == 0:
                print("Belum ada data reservasi untuk diubah.")
            else:
                for kode_id, info in daftar_reservasi.items():
                    print(f"[{kode_id}] {info['nama']} - {info['waktu']}")
                
                target_id = input("Masukkan Kode Reservasi yang ingin diubah (Cth: RES-1): ").upper()
                
                status_ada, info_lama = cari_id_reservasi(target_id)
                
                if status_ada:
                    print(f"\nMengubah data untuk: {info_lama['nama']}")
                    nama_baru = input("Masukkan Nama Pelanggan Baru : ")
                    barber_baru = input("Masukkan Nama Barber Baru   : ")
                    paket_baru = input("Masukkan Paket Layanan Baru : ")
                    waktu_baru = input("Masukkan Waktu Baru         : ")

                    try:
                        daftar_reservasi[target_id].update({
                            "nama": nama_baru,
                            "barber": barber_baru,
                            "paket": paket_baru,
                            "waktu": waktu_baru
                        })
                    except Exception as err:
                        cetak_notifikasi(f"Gagal memperbarui data: {err}")
                    else:
                        cetak_notifikasi("Data reservasi berhasil diperbarui!")
                    finally:
                        print("Blok update selesai diproses.")
                        
        elif menu == 4:
            print("\n--- HAPUS DATA RESERVASI (DELETE) ---")
            if hitung_total_reservasi() == 0:
                print("Belum ada data reservasi untuk dihapus.")
            else:
                for kode_id, info in daftar_reservasi.items():
                    print(f"[{kode_id}] {info['nama']} - {info['waktu']}")
                
                target_id = input("Masukkan Kode Reservasi yang ingin dihapus (Cth: RES-1): ").upper()
                
                status_ada, info_lama = cari_id_reservasi(target_id)
                if status_ada:

                    try:
                        data_terhapus = daftar_reservasi.pop(target_id)
                    except Exception as err:
                        cetak_notifikasi(f"Gagal menghapus data: {err}")
                    else:
                        cetak_notifikasi(f"Reservasi atas nama {data_terhapus['nama']} berhasil dihapus!")
                    finally:
                        print("Blok penghapusan data selesai diproses.")
                        
        elif menu == 5:
            cetak_notifikasi("Terima kasih telah menggunakan aplikasi reservasi barbershop!")
            break
        else:
            cetak_notifikasi("Pilihan menu tidak valid. Masukkan angka 1 sampai 5.")
            
    except ValueError as ve:
        cetak_notifikasi(f"Error Input: {ve}")
    except Exception as e:
        cetak_notifikasi(f"Terjadi kesalahan sistem: {e}")
    finally:
        print("[Siklus Menu Selesai]")