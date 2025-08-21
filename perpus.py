class Buku:
    def _init_(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

    def tampilkan(self, nomor):
        print(f"{nomor}. \tISBN\t: {self.isbn}\n"
              f"\tJudul\t: {self.judul}\n"
              f"\tPengarang\t: {self.pengarang}\n"
              f"\tJumlah Buku\t: {self.jumlah}\n"
              f"\tTerpinjam\t: {self.terpinjam}\n")
    
class Records:
    def init(self, isbn, status, tanggal_pinjam, tanggal_kembali="", nama_peminjam=""):
        self.isbn = isbn
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.nama_peminjam = nama_peminjam
    
    def _str_(self):
        return (f"\tISBN\t\t: {self.isbn}\n"
                f"\tStatus\t\t: {self.status}\n"
                f"\tTanggal Pinjam\t: {self.tanggal_pinjam}\n"
                f"\tTanggal Kembali\t: {self.tanggal_kembali if self.status == 'Selesai' else '-'}\n"
                f"\tPeminjam\t: {self.nama_peminjam if self.nama_peminjam else '-'}")
# data buku
books = [
    {"isbn":"9786237121144", "judul":"resep makanan", "pengarang":"fadlan", "jumlah":3, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"analisis pasar market", "pengarang":"fahri", "jumlah":12, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"belajar sambil bermain", "pengarang":"nathan", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"belajar menanam/grow a garden", "pengarang":"farrel", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""},
]

def tampilkan_data():
    for i in range(len(books)):
        print(i + 1,". \tISBN\t: ",books[i]["isbn"],"\n"
              ,"\tJudul\t:",books[i]["judul"],"\n",
              "\tPengarang\t:",books[i]["pengarang"],"\n",
              "\tJumlah Buku\t:",books[i]["jumlah"],"\n",
              "\tTerpinjam\t:",books[i]["terpinjam"],"\n")

def tambah_data():
    Ibaru = input("ISBN : ")
    Jbaru = input("Judul : ")
    Pbaru = input("Pengarang : ")
    Jmbaru = int(input("Jumlah : "))
    Tbaru = 0
    BukuBaru = {"isbn":Ibaru,"judul":Jbaru,"pengarang":Pbaru,"jumlah":Jmbaru,"terpinjam":Tbaru}
    books.append(BukuBaru)

def edit_data():
    Iganti = int(input("Masukkan Nomor Buku Yang Ingin DiGanti : "))-1
    books[Iganti]["isbn"]= input("ISBN : ")
    books[Iganti]["judul"]= input("Judul : ")
    books[Iganti]["pengarang"]= input("Pengarang : ")
    books[Iganti]["jumlah"]= int(input("Jumlah : "))
    books[Iganti]["terpinjam"]= int(input("Terpinjam : "))

def hapus_data():
    Dhapus = int(input("Masukkan Nomor Buku Yang Ingin DIHAPUS : "))-1
    books.pop(Dhapus)

def tampilkan_peminjaman():
    for i in range(len(records)):
        print(i + 1,". \tISBN\t: ",records[i]["isbn"],"\n"
              ,"\tStatus\t:",records[i]["status"],"\n",
              "\tTanggal Pinjam\t:",records[i]["tanggal_pinjam"],"\n",
              "\tTanggal Kembali\t:",records[i]["tanggal_kembali"],"\n",)

def tampilkan_belum():
    nomor = 1
    for i in range(len(records)):
        if records[i]["status"] == "Belum":
            print(nomor, ". \tISBN\t: ", records[i]["isbn"], "\n"
                "\tStatus\t:", records[i]["status"], "\n",
                "\tTanggal Pinjam\t:", records[i]["tanggal_pinjam"], "\n")
            nomor += 1

def peminjaman():
    Ipinjam = int(input("Masukan no buku yang ingin dipinjam: "))-1
    
    # Cek apakah buku tersedia
    if books[Ipinjam]["jumlah"] - books[Ipinjam]["terpinjam"] <= 0:
        print("Maaf, buku tidak tersedia untuk dipinjam.")
        return
    
    nama = input("Masukan nama peminjam: ")
    tanggal_pinjam = input("Masukan tanggal pinjam (YYYY-MM-DD): ")
    
    books[Ipinjam]["terpinjam"] += 1 
    
    records.append({
        "isbn": books[Ipinjam]["isbn"],  
        "status": "Belum", 
        "tanggal_pinjam": tanggal_pinjam, 
        "tanggal_kembali": "",
        "nama_peminjam": nama
    })
    
    print(f"Buku '{books[Ipinjam]['judul']}' berhasil dipinjam oleh {nama}")

def pengembalian():
    Ipinjam = input("Masukan isbn buku yang ingin dikembalikan: ")
    tanggal_kembali = input("Masukan tanggal kembali (YYYY-MM-DD): ")
    
    # Cari dan update record peminjaman
    record_found = False
    for record in records:
        if record["isbn"] == Ipinjam and record["status"] == "Belum":
            record["status"] = "Selesai"
            record["tanggal_kembali"] = tanggal_kembali
            record_found = True
            break
    
    if not record_found:
        print("Peminjaman dengan ISBN tersebut tidak ditemukan atau sudah dikembalikan.")
        return
    
    # Update jumlah buku yang terpinjam
    for book in books:
        if book["isbn"] == Ipinjam:
            book["terpinjam"] -= 1 
            print(f"Buku '{book['judul']}' berhasil dikembalikan")
            break

status = True
while status:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    match menu:
        case "1":
            tampilkan_data()
        case "2":
            tambah_data()
        case "3":
            edit_data()
        case "4":
            hapus_data()
        case "5":
            tampilkan_peminjaman()
        case "6":
            tampilkan_belum()
        case "7":
            peminjaman()
        case "8":
            pengembalian()
        case "x"|"X":
            status = False