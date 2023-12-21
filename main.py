class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Pemesanan:
    def __init__(self):
        self.daftar_menu = [
            Menu("Nasi Goreng", 25000),
            Menu("Mie Goreng", 20000),
            Menu("Ayam Bakar", 30000),
            Menu("Soto Ayam", 28000),
            Menu("Es Teh", 5000),
            Menu("Es Jeruk", 6000),
        ]
        self.pesanan = {}

    def tampilkan_menu(self):
        print("Menu Makanan:")
        for i, menu in enumerate(self.daftar_menu, start=1):
            print(f"{i}. {menu.nama} - Rp{menu.harga}")

    def pesan_makanan(self):
        while True:
            self.tampilkan_menu()
            nomor_menu = input("Pilih nomor menu (0 untuk selesai): ")

            if nomor_menu == '0':
                break

            try:
                nomor_menu = int(nomor_menu)
                if 1 <= nomor_menu <= len(self.daftar_menu):
                    jumlah_pesanan = int(input("Jumlah pesanan: "))
                    menu_terpilih = self.daftar_menu[nomor_menu - 1]

                    if menu_terpilih.nama in self.pesanan:
                        self.pesanan[menu_terpilih.nama] += jumlah_pesanan
                    else:
                        self.pesanan[menu_terpilih.nama] = jumlah_pesanan

                    print(f"{jumlah_pesanan} {menu_terpilih.nama} ditambahkan ke pesanan.")
                else:
                    print("Nomor menu tidak valid. Silakan pilih kembali.")
            except ValueError:
                print("Masukan tidak valid. Masukkan angka.")

    def tampilkan_pesanan(self):
        print("Pesanan Anda:")
        total_harga = 0
        for menu, jumlah in self.pesanan.items():
            harga_menu = [m.harga for m in self.daftar_menu if m.nama == menu][0]
            harga_total_menu = harga_menu * jumlah
            total_harga += harga_total_menu
            print(f"{menu} x{jumlah} - Rp{harga_total_menu}")

        print(f"Total Harga: Rp{total_harga}")

    def proses_pesanan(self):
        print("Proses Pesanan:")
        self.tampilkan_pesanan()
        print("Terima kasih telah memesan! Mohon tunggu pesanan Anda.")

if __name__ == "__main__":
    pemesanan = Pemesanan()

    while True:
        print("\nAplikasi Pemesanan Makanan:")
        print("1. Lihat Menu")
        print("2. Pesan Makanan")
        print("3. Lihat Pesanan")
        print("4. Proses Pesanan")
        print("0. Keluar")

        pilihan = input("Masukkan nomor pilihan: ")

        if pilihan == '0':
            print("Terima kasih! Selamat tinggal.")
            break
        elif pilihan == '1':
            pemesanan.tampilkan_menu()
        elif pilihan == '2':
            pemesanan.pesan_makanan()
        elif pilihan == '3':
            pemesanan.tampilkan_pesanan()
        elif pilihan == '4':
            pemesanan.proses_pesanan()
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
