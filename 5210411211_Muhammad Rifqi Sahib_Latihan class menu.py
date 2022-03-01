class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

minuman1 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat", 12000)
minuman2 = Menu("Jus Jambu", "Jus jambu merah murni", 7500)
minuman3 = Menu("Red & Smooth", "Smoothie pisang dan strawberry dengan tambahan susu", 15500)
minuman4 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 10000)

makanan1 = Menu("Hotdog", "Roti dengan Topping Sosis", 25000)
makanan2 = Menu("Mie Ayam", "Mie Ayam dengan Pangsit", 10000)
makanan3 = Menu("Spaghetti", "Spaghetti dengan Keju dan sedikit irisan daging", 17500)
makanan4 = Menu("Bubur", "Bubur dengan bumbu tiga rasa", 10000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")