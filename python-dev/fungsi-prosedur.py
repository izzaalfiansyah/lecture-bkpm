# # variabel global
# nama = "Muhammad Alfiansyah"
# golongan = "D"

# def sebut():
#     # variabel lokal
#     nama = "Ricky Mahbubi"
#     golongan = "B"
#     # akses variabel lokal
#     print("Nama     : %s" % nama)
#     print("Versi    : Golongan %s" % golongan)

# # mengakses variabel global
# print("Nama     : %s" % nama)
# print("Versi    : Golongan %s" % golongan)

# sebut()



# def perkalian(bil1, bil2):
#     hasil = int(bil1) * int(bil2)
#     return hasil

# print('hasil perkalian dari 3 dan 5 adalah', perkalian(3, 5))


# def dataDiri(nama, usia):
#     # menampilkan nama dan kata
#     print('Nama saya adalah', nama)
#     print('Usia saya adalah', usia)

# dataDiri('Alfiansyah', 17)


# def salam(**person):
#     print('Halo', person['namaDepan'], person['namaBelakang'])

# salam(namaDepan = 'Muhammad', namaBelakang = 'Alfiansyah')
# salam(namaBelakang = 'Utomo', namaDepan = 'Budi')
# salam(namaDepan = 'Indah', namaBelakang = 'Pertiwi', usia = 20)
# salam(namaDepan = 'Alex')


# def identitas(namaDepan, namaBelakang, usia):
#     print('Nama Saya', namaDepan, namaBelakang, ', Usia saya', usia, 'tahun')

# identitas(usia = 17, namaDepan='Muhammad', namaBelakang='Alfiansyah')


# def salam(*nama):
#     i = 0
#     print('Hallo', end = '')
#     while len(nama) > i:
#         print(nama[i], end = ', ')
#         i += 1
#     print()

# salam('Aldo', 'Budi', 'Chacha')
# salam('Aldo', 'Budi', 'Chacha', 'Doni', 'Elvis', 'Fina')



# def salam(nama1, nama2, nama3):
#     # menampilkan nama dan kata
#     print('Assalamualaikum', nama1, ',', nama2, ',', nama3)

# salam('Aldo', 'Bobi', 'Chaca')



# def salam(name):
#     print('Halo', name)

# salam('Mahasiswa')
# salam(123)



# def halo(salam):
#     print(salam)

# halo('Assalamu\'alaikum')


# # membuat fungsi
# def halo():
#     print('Selamat datang di TKK')
#     print('Selamat belajar Workshop Pemrograman Dasar')

# halo()
# halo()
# halo()


# def halo():
#     print('Selamat datang di TKK')
#     print('Selamat belajar Workshop Pemrograman Dasar')

# halo()