# ==========================================
# MODUL DATABASE & VARIABEL GLOBAL
# ==========================================

daftar_reservasi = {}
nomor_id = 1
NAMA_BARBERSHOP = "BARBERSHOP STUDIO"

def tampilkan_header():
    print("\n" + "=" * 55)
    print(f"      SELAMAT DATANG DI {NAMA_BARBERSHOP}")
    print("=" * 55)

def cetak_notifikasi(pesan):
    print(f"[INFO SISTEM]: {pesan}")