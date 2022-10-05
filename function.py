
# Fungsi untuk tampilan menu awal
def printHalamanAwal() :
    print("-".center(67,"-"))
    print("Perpustakaan ABC".center(67))
    print("-".center(67,"-"))

    print("Selamat Datang di Perpustakaan ABC!".center(67))
    print("""
1.  Ilmu Komputer dan Umum
2.  Filosofi dan Psikologi
3.  Agama
4.  Ilmu Sosial
5.  Bahasa
6.  Ilmu Pengetahuan
7.  Teknologi & Ilmu Pengetahuan Terapan
8.  Seni
9.  Sastra
10. Sejarah & Geografi

99. Keluar Aplikasi
    """) 


# Fungsi untuk print Header sesuai dengan kategorinya masing-masing
def printKategoriHeader (kategori) :
    print("-".center(67,"-"))
    print("Perpustakaan ABC".center(67))
    print("-".center(67,"-"))
    print(kategori.center(67))
    print("-".center(67,"-"))
     
