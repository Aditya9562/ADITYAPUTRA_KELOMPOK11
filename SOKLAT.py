# Fungsi untuk menampilkan daftar menu
def show_menu():
    print("===== DAFTAR MENU =====")
    print("1. PAKET SOKLAT BESAR\t\tRp. 15.000")
    print("2. PAKET SOKLAT KECIL\t\tRp. 12.000")
    print("3. SOKLAT SEDANG\t\tRp. 10.000")
    print("4. ROTI\t\t\t\tRp. 5.000")
    print("5. Selesai Memesan")

# Fungsi untuk menghitung total harga pesanan
def calculate_price(jumlah, harga):
    return jumlah * harga

# Fungsi untuk menampilkan pesanan
def show_pesanan(menu, jumlah, total_harga):
    print("========================")
    print("Pesanan Anda:")
    for i in range(len(menu)):
        print(f"{menu[i]}\t x{jumlah[i]}\tRp. {total_harga[i]}")
    print("========================")
    print(f"Total Harga: Rp. {sum(total_harga)}")

class Restoran:
    def __init__(self, nama_restoran):
        self.nama_restoran = nama_restoran
        self.menu_minuman = ["PAKET SOKLAT BESAR", "PAKET SOKLAT KECIL", "SOKLAT SEDANG", "ROTI"]
        self.harga_minuman = [15000, 12000, 10000, 5000]
        self.pesanan_menu = []
        self.pesanan_jumlah = []
        self.pesanan_harga = []

    # Method untuk menambah pesanan minuman ke dalam list pesanan
    def tambah_pesanan(self, pilihan_menu, jumlah):
        if pilihan_menu > 0 and pilihan_menu < 5:
            menu = self.menu_minuman[pilihan_menu-1]
            harga = self.harga_minuman[pilihan_menu-1]
            total_harga = calculate_price(jumlah, harga)
            self.pesanan_menu.append(menu)
            self.pesanan_jumlah.append(jumlah)
            self.pesanan_harga.append(total_harga)
            print(f"{jumlah} porsi {menu} berhasil ditambahkan ke pesanan Anda!")
        else:
            print("Menu tidak tersedia, silakan pilih kembali.")

    # Method untuk menampilkan daftar pesanan
    def lihat_pesanan(self):
        show_pesanan(self.pesanan_menu, self.pesanan_jumlah, self.pesanan_harga)

    # Method untuk menghitung total harga pesanan
    def hitung_total_harga(self):
        return sum(self.pesanan_harga)

    # Fungsi untuk memberikan diskon 10% jika total harga pesanan lebih dari Rp. 50.000
    def diskon(self):
        total_harga = self.hitung_total_harga()
        if total_harga > 50000:
            return total_harga * 0.1
        else:
            return 0

    # Method untuk menghitung total harga pesanan setelah didiskon
    def hitung_total_harga_setelah_diskon(self):
        return self.hitung_total_harga() - self.diskon()

    # Method untuk menampilkan struk pembayaran
    def struk_pembayaran(self):
        print("========= Struk Pembayaran =========")
        self.lihat_pesanan()
        print(f"Total Harga: Rp. {self.hitung_total_harga()}")
        if self.diskon() > 0:
            print(f"Diskon: Rp. {self.diskon()}")
            print(f"Total Harga Setelah Diskon: Rp. {self.hitung_total_harga_setelah_diskon()}")
        else:
            print("Anda tidak mendapatkan diskon")
            print("Terima kasih telah memesan di SOKLAT, silakan datang kembali!")

# Program utama
restoran = Restoran("SOKLAT")

while True:
    print("===== Selamat Datang di SOKLAT =====")
    show_menu()
    pilihan_menu = int(input("Masukkan nomor menu yang ingin dipesan: "))
    if pilihan_menu == 5:
        print("Terima kasih telah berkunjung. Sampai jumpa lagi!")
        break

    else:
        jumlah_porsi = int(input("Masukkan jumlah porsi yang ingin dipesan: "))
        restoran.tambah_pesanan(pilihan_menu, jumlah_porsi)

print()
restoran.struk_pembayaran()
print(f"Diskon yang diberikan: Rp. {restoran.diskon()}")
print(f"Total Harga setelah diskon: Rp. {restoran.hitung_total_harga_setelah_diskon()}")

print ("\n=====DIBUAT OLEH=====\n")
print ("KELOMPOK 11 (SHIFT GENAP)")
print ("ADITYA PUTRA AFENDI     21120122140035 ")
print ("KADEK WISNU PARIJATA PUTRA  21120122140036")
print ("NADHIF ABHIRAMA N       21120122140139")
print ("M FARHAN RAMADHAN       21120122140088")



