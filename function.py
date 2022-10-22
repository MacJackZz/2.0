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

def tampilListBuku (kategori_list_no):
    '''Menampilkan list buku sesuai dengan no. kategori dalam parameter'''
    number = 1
    for judul in kategori_list_no :
      print(f"{number}. {judul}")
      number +=1


def pilihanKategoriBuku (userInput, no_pilihan, kategori_ke, kategori_list_ke) :
    '''Function untuk setiap pilihan kategori bukunya masing-masing'''
    while(userInput == no_pilihan) :
    
        printKategoriHeader(kategori_ke)
        tampilListBuku(kategori_list_ke)

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
    print("-".center(67, "-"))
    print("Anda telah keluar dari Aplikasi!".center(67))
    print("-".center(67, "-"))
    print("\n"*7)