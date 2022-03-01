class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Marmut merah jambu", "Raditya Dika", 2010)
buku2 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku3 = Buku("Harry Potter", "J.K.Rowling", 1997)

buku_novel = [buku1, buku2, buku3]
print("List Buku Novel")
for buku in buku_novel :
    teks = 'Buku novel {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")