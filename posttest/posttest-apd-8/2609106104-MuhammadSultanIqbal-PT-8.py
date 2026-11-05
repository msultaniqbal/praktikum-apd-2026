from database import tampilkan_header, cetak_notifikasi
import database
from reservasi_ops import (
    pilih_menu, hitung_total_reservasi, proses_tambah_reservasi,
    cari_id_reservasi, tampilkan_tabel_reservasi
)

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
            
            kunci_id = f"RES-{database.nomor_id}"
            paket_data_baru = {
                "nama": nama_pelanggan,
                "barber": barber_pilihan,
                "paket": paket_layanan,
                "waktu": waktu_reservasi
            }
            
            berhasil = proses_tambah_reservasi(kunci_id, paket_data_baru)
            if berhasil:
                database.nomor_id += 1
                
        elif menu == 2:
            print("\n--- DAFTAR RESERVASI BARBERSHOP ---")
            total = hitung_total_reservasi()
            if total == 0:
                print("Belum ada data reservasi.")
            else:
                print(f"Total Reservasi Aktif: {total}")
                tampilkan_tabel_reservasi()
                
        elif menu == 3:
            print("\n--- UBAH DATA RESERVASI (UPDATE) ---")
            if hitung_total_reservasi() == 0:
                print("Belum ada data reservasi untuk diubah.")
            else:
                tampilkan_tabel_reservasi()
                target_id = input("Masukkan Kode Reservasi yang ingin diubah (Cth: RES-1): ").upper()
                
                status_ada, info_lama = cari_id_reservasi(target_id)
                
                if status_ada:
                    print(f"\nMengubah data untuk: {info_lama['nama']}")
                    nama_baru = input("Masukkan Nama Pelanggan Baru : ")
                    barber_baru = input("Masukkan Nama Barber Baru   : ")
                    paket_baru = input("Masukkan Paket Layanan Baru : ")
                    waktu_baru = input("Masukkan Waktu Baru         : ")
                    
                    try:
                        database.daftar_reservasi[target_id].update({
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
                tampilkan_tabel_reservasi()
                target_id = input("Masukkan Kode Reservasi yang ingin dihapus (Cth: RES-1): ").upper()
                
                status_ada, info_lama = cari_id_reservasi(target_id)
                if status_ada:
                    try:
                        data_terhapus = database.daftar_reservasi.pop(target_id)
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