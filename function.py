
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
     
# Menampilkan list buku sesuai dengan no. kategori dalam parameter
def tampilListBuku (kategori_list_no):
    number = 1
    for judul in kategori_list_no :
      print(f"{number}. {judul}")
      number +=1






# Eksekusi pilihahKategoriBuku Function
# pilihanKategoriBuku(userInput, 1, kategori_1, kategori_1_list)

# Function pilihanKategoriBuku
# def pilihanKategoriBuku (userInput, no_pilihan, kategori_ke, kategori_list_ke) :
#     while(userInput == no_pilihan) :
    
#         printKategoriHeader(kategori_ke)
#         tampilListBuku(kategori_list_ke)

#         # Opsi Kembali
#         exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
#         if (exitPilihanUser == 'Y') :
#           userInput = False
#         elif (exitPilihanUser == 'N') :
#             continue
#         else :
#             print("Data yg anda masukan tidak valid!")
#         pass
