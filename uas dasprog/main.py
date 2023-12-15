from modules.catatan_pengeluaran import CatatanPengeluaran
from datetime import datetime

def main():
    catatan_pengeluaran = CatatanPengeluaran()
    catatan_pengeluaran.baca_dari_file()

    while True:
        print("\nMenu:")
        print("1. Tambah Catatan Pengeluaran")
        print("2. Lihat Catatan Pengeluaran")
        print("3. Hapus Catatan Pengeluaran")
        print("4. Lihat Total Pengeluaran")
        print("5. Simpan Catatan Pengeluaran ke File")
        print("6. Keluar")

        try:
            pilihan = input("Pilih menu (1/2/3/4/5/6): ")

            if pilihan == '1':
                tanggal_input = input("Masukkan Tanggal (YYYY-MM-DD): ")
                tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").strftime("%Y %m %d")
                kategori = catatan_pengeluaran.pilih_kategori()
                jumlah_input = input("Masukkan Jumlah: ")
                jumlah = float(''.join(filter(str.isdigit, jumlah_input)))
                jenis = catatan_pengeluaran.pilih_jenis()
                deskripsi = input("Masukkan Deskripsi: ")

                catatan_pengeluaran.tambah_pengeluaran(tanggal, kategori, jumlah, jenis, deskripsi)
                print("Catatan pengeluaran berhasil ditambahkan.")

            elif pilihan == '2':
                catatan_pengeluaran.lihat_pengeluaran()

            elif pilihan == '3':
                nomor_hapus = int(input("Masukkan nomor catatan yang akan dihapus: "))
                catatan_pengeluaran.hapus_pengeluaran(nomor_hapus)
                print("Catatan pengeluaran berhasil dihapus.")

            elif pilihan == '4':
                catatan_pengeluaran.total_pengeluaran()

            elif pilihan == '5':
                catatan_pengeluaran.simpan_ke_file()
                print("Catatan pengeluaran berhasil disimpan ke file.")

            elif pilihan == '6':
                print("Keluar dari program.")
                break

            else:
                print("Pilihan menu tidak valid. Silakan coba lagi.")

        except ValueError as e:
            print(f"Terjadi kesalahan: {e}. Harap masukkan input yang valid.")

if __name__ == "__main__":
    main()
