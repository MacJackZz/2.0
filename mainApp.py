from function import *
from data import *





startApp = True

while (startApp) :
  
  printHalamanAwal()
  userInput = int(input("Silahkan masukan pilihan anda : "))
  # pilihanUser = True

# Kategori No. 1 : Ilmu Komputer dan Umum
  while(userInput == 1 ) :
    
    printKategoriHeader(kategori_1)
    tampilListBuku(kategori_1_list)


    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass


# Kategori No. 2 : Filosofi dan Psikologi
  while(userInput == 2 ) :
    
    printKategoriHeader(kategori_2)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_2_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass


# Kategori No. 3 : Agama
  while(userInput == 3 ) :
    
    printKategoriHeader(kategori_3)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_3_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 4 : Ilmu Sosial
  while(userInput == 4 ) :
    
    printKategoriHeader(kategori_4)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_4_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 5 : Bahasa
  while(userInput == 5 ) :
    
    printKategoriHeader(kategori_5)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_5_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 6 : Ilmu Pengetahuan
  while(userInput == 6 ) :
    
    printKategoriHeader(kategori_6)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_6_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 7 : Teknologi & Ilmu Pengetahuan Terapan
  while(userInput == 7 ) :
    
    printKategoriHeader(kategori_7)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_7_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 8 : Seni
  while(userInput == 8 ) :
    
    printKategoriHeader(kategori_8)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_8_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 9 : Sastra
  while(userInput == 9 ) :
    
    printKategoriHeader(kategori_9)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_9_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass

# Kategori No. 10 : Sejarah & Geografi
  while(userInput == 10 ) :
    
    printKategoriHeader(kategori_10)

    # Tampilkan List Buku
    number = 1
    for judul in kategori_10_list :
      print(f"{number}. {judul}")
      number +=1

    # Opsi Kembali
    exitPilihanUser = input("Ingin kembali ke beranda ? (Y/N)").upper()
    if (exitPilihanUser == 'Y') :
      userInput = False
    elif (exitPilihanUser == 'N') :
      continue
    else :
      print("Data yg anda masukan tidak valid!")
      pass


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
  
  

print("-".center(67, "-"))
print("Anda telah keluar dari Aplikasi!".center(67))
print("-".center(67, "-"))



