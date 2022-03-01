class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("Rifqi", "5210411211", "Informatika")
mahasiswa2 = Mahasiswa("Pertiwi", "5211911013", "Informatika medis")
mahasiswa3 = Mahasiswa("jack", "5210411378", "Informatika")
mahasiswa4 = Mahasiswa("William", "5210411215", "Informatika")
mahasiswa5 = Mahasiswa("Jovian","5210511214","Perencanaan Wilayah Kota")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5]
print("List Mahasiswa Informatika")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")