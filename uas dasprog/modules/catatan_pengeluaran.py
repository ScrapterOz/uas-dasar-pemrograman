from datetime import datetime

class CatatanPengeluaran:
    KATEGORI_OPSI = (
        "Pengeluaran Rutin",
        "Cicilan Utang",
        "Pengeluaran Tabungan dan Investasi",
        "Pengeluaran Sosial",
        "Pengeluaran Gaya Hidup",
        "Pengeluaran Asuransi",
    )

    JENIS_OPSI = (
        "Debet",
        "Kredit",
    )

    def __init__(self):
        self.catatan = []

    def tambah_pengeluaran(self, tanggal, kategori, jumlah, jenis, deskripsi):
        nomor = len(self.catatan) + 1
        self.catatan.append({'nomor': nomor, 'tanggal': tanggal, 'kategori': kategori, 'jumlah': jumlah, 'jenis': jenis, 'deskripsi': deskripsi})

    def lihat_pengeluaran(self):
        header = ['No', 'Tanggal', 'Kategori', 'Jumlah', 'Jenis', 'Deskripsi']
        self._tampilkan_tabel(header)

        for transaksi in self.catatan:
            self._tampilkan_tabel([transaksi['nomor'], transaksi['tanggal'], transaksi['kategori'], transaksi['jumlah'], transaksi['jenis'], transaksi['deskripsi']])

    def hapus_pengeluaran(self, nomor):
        self.catatan = [transaksi for transaksi in self.catatan if transaksi['nomor'] != nomor]

    def total_pengeluaran(self):
        total = sum(transaksi['jumlah'] for transaksi in self.catatan)
        print(f"Total Pengeluaran: {self._format_rupiah(total)}")

    def pilih_kategori(self):
        print("\nPilih Kategori:")
        for i, kategori in enumerate(self.KATEGORI_OPSI, 1):
            print(f"{i}. {kategori}")
        
        while True:
            try:
                index = int(input("Masukkan nomor kategori: "))
                if 1 <= index <= len(self.KATEGORI_OPSI):
                    return self.KATEGORI_OPSI[index - 1]
                else:
                    print("Nomor kategori tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input harus berupa angka.")

    def pilih_jenis(self):
        print("\nPilih Jenis:")
        for i, jenis in enumerate(self.JENIS_OPSI, 1):
            print(f"{i}. {jenis}")

        while True:
            try:
                index = int(input("Masukkan nomor jenis: "))
                if 1 <= index <= len(self.JENIS_OPSI):
                    return self.JENIS_OPSI[index - 1]
                else:
                    print("Nomor jenis tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input harus berupa angka.")

    def _tampilkan_tabel(self, header):
        print("-" * (len(header) * 20))
        for kolom in header:
            print(f"{kolom.center(20)}|", end="")
        print("\n" + "-" * (len(header) * 20))

    def _format_rupiah(self, jumlah):
        return f"Rp. {jumlah:,.2f}"

    def simpan_ke_file(self, nama_file='catatan_pengeluaran.txt'):
        with open(nama_file, 'w') as file:
            for transaksi in self.catatan:
                file.write(','.join(map(str, [transaksi['nomor'], transaksi['tanggal'], transaksi['kategori'], transaksi['jumlah'], transaksi['jenis'], transaksi['deskripsi']])) + '\n')

    def baca_dari_file(self, nama_file='catatan_pengeluaran.txt'):
        try:
            with open(nama_file, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    nomor, tanggal, kategori, jumlah, jenis, deskripsi = map(int, data[:-1]) + [float(data[-1])]
                    self.catatan.append({'nomor': nomor, 'tanggal': tanggal, 'kategori': kategori, 'jumlah': jumlah, 'jenis': jenis, 'deskripsi': deskripsi})
        except FileNotFoundError:
            print("File catatan_pengeluaran.txt tidak ditemukan. Membuat file baru.")
