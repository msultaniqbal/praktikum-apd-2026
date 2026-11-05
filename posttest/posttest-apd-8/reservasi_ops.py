# ==========================================
# MODUL OPERASI & FUNGSI RESERVASI
# ==========================================

from prettytable import PrettyTable
from database import daftar_reservasi, NAMA_BARBERSHOP, cetak_notifikasi

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
    return len(daftar_reservasi)

def proses_tambah_reservasi(id_baru, data_baru):
    lokal_status = True
    lokal_id = id_baru
    lokal_data = data_baru
    lokal_counter = 1
    
    try:
        daftar_reservasi[lokal_id] = lokal_data
        if lokal_counter == 1:
            pass
    except Exception as e:
        lokal_status = False
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

def tampilkan_tabel_reservasi():
    """Menampilkan daftar reservasi menggunakan PrettyTable"""
    tabel = PrettyTable()
    tabel.field_names = ["Kode", "Nama Pelanggan", "Barber", "Paket Layanan", "Waktu"]
    
    # Mengatur perataan teks pada tabel
    tabel.align["Nama Pelanggan"] = "l"
    tabel.align["Barber"] = "l"
    tabel.align["Paket Layanan"] = "l"
    tabel.align["Kode"] = "c"
    tabel.align["Waktu"] = "c"
    
    for kode_id, info in daftar_reservasi.items():
        tabel.add_row([
            kode_id,
            info['nama'],
            info['barber'],
            info['paket'],
            info['waktu']
        ])
    print(tabel)