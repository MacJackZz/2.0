from function import *
from data import *


startApp = True

while (startApp) :
  
  printHalamanAwal()
  userInput = int(input("Silahkan masukan pilihan anda : "))
  # pilihanUser = True

# Kategori No. 1 : Ilmu Komputer dan Umum
  pilihanKategoriBuku(userInput, 1, kategori_buku[0], kategori_1_list)
  # Kategori No. 2 : Filosofi dan Psikologi
  pilihanKategoriBuku(userInput, 2, kategori_buku[1], kategori_2_list)
  # Kategori No. 3 : Agama
  pilihanKategoriBuku(userInput, 3, kategori_buku[2], kategori_3_list)
  # Kategori No. 4 : Ilmu Sosial
  pilihanKategoriBuku(userInput, 4, kategori_buku[3], kategori_4_list)
  # Kategori No. 5 : Bahasa
  pilihanKategoriBuku(userInput, 5, kategori_buku[4], kategori_5_list)
  # Kategori No. 6 : Ilmu Pengetahuan
  pilihanKategoriBuku(userInput, 6, kategori_buku[5], kategori_6_list)
  # Kategori No. 7 : Teknologi & Ilmu Pengetahuan Terapan
  pilihanKategoriBuku(userInput, 7, kategori_buku[6], kategori_7_list)
  # Kategori No. 8 : Seni
  pilihanKategoriBuku(userInput, 8, kategori_buku[7], kategori_8_list)
  # Kategori No. 9 : Sastra
  pilihanKategoriBuku(userInput, 9, kategori_buku[8], kategori_9_list)
  # Kategori No. 10 : Sejarah & Geografi
  pilihanKategoriBuku(userInput, 10, kategori_buku[9], kategori_10_list)


# Opsi untuk keluar aplikasi
  if(userInput == 99) :
    exitApp = input("Apakah anda ingin keluar dari aplikasi? (Y/N) : ").upper()
    if (exitApp == 'Y') :
      startApp = False
    elif (exitApp == 'N') :
      pass
    else :
      print("Data yg anda masukan tidak valid!")
      pass
  
  

tampilPesanKeluar()