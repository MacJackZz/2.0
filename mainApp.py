from function import *
from data import *

print(k_1_buku1)

startApp = True

while (startApp) :
  printHalamanAwal()
  userInput = int(input("Silahkan masukan pilihan anda : "))

  if(userInput == 1 ) :
    printKategoriHeader(kategori_1)
    print('Ilmu Komputer dan Umum :', *kategori_1_list, sep='\n -')
    userInput2 = int(input("Silahkan pilih buku : "))
    # if(userInput2) == 1 :


  



  



  
  exitApp = input("Ingin keluar? (Y/N) : ").upper()
  if (exitApp == 'Y') :
    startApp = False
  elif (exitApp == 'N') :
    pass
  else :
    print("Data yg anda masukan tidak valid!")


print("Anda telah keluar dari Aplikasi")


