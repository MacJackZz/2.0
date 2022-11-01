import os


def printHalamanAwal() :
    ''' Fungsi untuk tampilan menu awal'''

    # Biar auto clear
    os.system('cls')


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



def printKategoriHeader (kategori) :
    '''Fungsi untuk print Header sesuai dengan kategorinya masing-masing'''
    os.system('cls')

    print("-".center(67,"-"))
    print("Perpustakaan ABC".center(67))
    print("-".center(67,"-"))
    print(kategori.center(67))
    print("-".center(67,"-"))

# kategori_n_list  = kategori_1_list, kategori_2_list, kategori_3_list, ....
def tampilListBuku (kategori_n_list):
    '''Menampilkan list buku'''
    for indeks, judul in enumerate(kategori_n_list) :
        print(f"{indeks+1}. {judul}")



def pilihanKategoriBuku (userInput, no_pilihan_user, kategori_buku, kategori_n_list) :
    '''Function untuk setiap pilihan kategori bukunya masing-masing'''
    while(userInput == no_pilihan_user) :
    
        printKategoriHeader(kategori_buku)
        tampilListBuku(kategori_n_list)

        # Opsi Kembali
        exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N) : ").upper()
        if (exitPilihanUser == 'Y') :
            userInput = False
            return userInput
        elif (exitPilihanUser == 'N') :
            continue
        else :
            print("Data yg anda masukan tidak valid!")
        pass


def tampilPesanKeluar() :
    ''' Fungsi untuk pesan ketika user keluar dari aplikasi '''
    os.system('cls')
    print("\n"*7)
    print("".center(67, "-"))
    print("Anda telah keluar dari Aplikasi!".center(67))
    print("".center(67, "-"))
    print("\n"*7)