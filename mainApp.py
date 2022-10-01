from function import *
from data import *

# for buku in kategori_1_dict.values() :
#   for judul in buku.values() :
#     print(judul['judul'])

# for buku in kategori_1_dict.keys():
#   print 
#   for judul in kategori_1_dict[buku].keys():
#         print 





for x in get_all_keys(kategori_1_dict):
    print(x)

# print(kategori_1_dict)
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


