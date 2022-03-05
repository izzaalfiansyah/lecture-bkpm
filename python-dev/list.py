# # 10
# # list minuman dengan 2 dimensi
# list_minuman = [
#     ['kopi', 'susu', 'teh'],
#     ['jus apel', 'jus melon', 'jus jeruk'],
#     ['es kopi', 'es campur', 'es teler']
# ]
# print(list_minuman)
# print('\n')

# # cara mengakses list multi dimensi
# # angka pertama menunjukkam kolom, yang kedua adalah baris
# print('menampilkan salah satu menu dengan menunjuk nomor index:')
# print(list_minuman[2][0])
# print(list_minuman[0][1])
# print('\n')

# # mencetak isi list satu persatu
# print('menampilkan isi list:')
# for item in list_minuman:
#     print(item)
# print('\n')

# # mencetak isi list di dalam list satu persatu
# print('menampilkan isi list di dalam list:')
# for data in list_minuman:
#     for item in data:
#         print(item)

# # 9
# listAngka = [3, 5, 8, 1, 2, 9, 7, 4, 6]
# listHuruf = ['doni', 'caca', 'eva', 'bobi', 'ani', 'faruq']
# print(listAngka)
# print(listHuruf)

# # mengurutkan isi list berupa angka dan kata menggunakan sort
# print('marilah kita urutkan:')
# listAngka.sort()
# listHuruf.sort()
# print(listAngka)
# print(listHuruf)

# # membalik index isi list berupa angka dan kata menggunakan reverse
# print('membalik urutan index:')
# listAngka.reverse()
# listHuruf.reverse()
# print(listAngka)
# print(listHuruf)


# # 8
# listHari = ['hari', 'senin', 'selasa', 'maret', 'rabu', 'kamis', 'juni']
# print(listHari)

# # remove = menghapus nilai yang sama
# print('menghapus maret dari list:')
# listHari.remove('maret')
# print(listHari)

# # kata kunci del = menghapus nilai item sesuai dengan index yang diminta
# print('menghapus index ke 0 yaitu hari:')
# del listHari[0]
# print(listHari)

# # pop = menghapus nilai item sesuai dengan index yang diminta
# print('menghapus index ke 4 yaitu juni menggunakan pop:')
# listHari.pop(4)
# print(listHari)

# # pop = menghapus nilai item sesuai terakhir pada list yaitu kamis
# print('menghapus index terakhir (kamis) menggunakan pop:')
# listHari.pop()
# print(listHari)

# # mencetak nilai yang dihapus menggunakan pop
# print('mencetak nilai yang dihapus pada index ke 0 yaitu senin:')
# print(listHari.pop(0))

# # 7
# nomor = [1, 5, 7, 9, 11]

# # mendapatkan jumlah item pada list menggunakan len
# print('menghitung jumlah item pada list:')
# print(len(nomor))

# # menambahkan item diakhir list menggunakan append
# print('menambahkan angka 13 menggunakan append:')
# nomor.append(13)
# print(nomor)

# # menyisipkan item pada indeks tertentu menggunakan insert
# print('menyisipkan angka 3 pada index ke-1 menggunakan insert:')
# index = 1
# nomor.insert(index, 3)
# print(nomor)

# # menambah list pada list menggunakan extend
# print('menambah list berisi 15, 17, 19 pada list nomor:')
# nomor.extend([15, 17, 19])
# print(nomor)

# # cek index ke berapa
# print('cek angka 1 di index ke berapa? angka 2 di index ke berapa?')
# print(nomor.index(1))
# print(nomor.index(2))

# # 6
# listKata = ['mangga', 'jambu', 'apel', 'anggur']
# print(listKata)

# # mengubah indeks ke 1 pada listKata
# print('sesudah indeks ke 1 diubah:')
# listKata[1] = 'rambutan'
# print(listKata)

# # menambah list pada listKata tetapi tidak disimpan
# print('list juga bisa ditambahkan:')
# print(listKata + ['delima', 'melon', 'pear'])

# # menambah list pada listKata lalu disimpan
# print('list juga bisa ditambahkan kemudian disimpan:')
# listKata = listKata + ['delima', 'melon', 'pear']
# print(listKata)

# # mengalikan list pada listKata
# print('list juga bisa dikalikan:')
# print(listKata*2)

# # memeriksa item dalam list
# print("mangga" in listKata)
# print("salak" not in listKata)
# if "melon" in listKata:
#     print("ada melon di dalam listKata")

# # 5
# listKata = ['mangga', 'jambu', 'apel', 'anggur']

# print(listKata[0:])
# print(listKata[1:])
# print(listKata[2:])
# print(listKata[3:])
# print(listKata[:0])
# print(listKata[:1])
# print(listKata[:2])
# print(listKata[:3])
# print(listKata[:4])
# print()
# print(listKata[-1:])
# print(listKata[-2:])
# print(listKata[-3:])
# print(listKata[:0])
# print(listKata[:-1])
# print(listKata[:-2])
# print(listKata[:-3])
# print(listKata[:-4])

# 4
# asd = ['nol', 'satu', 'dua', 'tiga', 'empat', 'mintiga', 'mindua', 'minsatu']

# print(asd[1:3])
# print(asd[0:-1])
# print(asd[-1:-3])
# print(asd[-1:3])
# print(asd[-3:-1])
# print(asd[-4:-1])
# print(asd[-4:-2])

# 3
# listKata = ['mangga', 'jambu', 'apel', 'anggur']

# print(listKata[0:1])
# print(listKata[0:2])
# print(listKata[1:3])
# print(listKata[0:-1])
# print(listKata[-1:-3])
# print(listKata[-1:3])
# print(listKata[-3:-1])

# 2
# # membuat list kosong
# listKosong = []

# contohKata = "Workshop"
# contohAngka = 12345678

# print(contohKata[5])
# print(contohAngka[5])

# 1
# # membuat list kosong
# listKosong = []

# # membuat list berisi 1 item
# listSatuItem = ['satu item']

# # membuat list dengan banyak item dengan sati tipe data
# listKata = ['mangga', 'jambu', 'apel', 'anggur']
# listAngka = [23, 11, 94]

# # membuat list dengan berbagai tipe data
# listMix = [23, 'November', 94]

# # membuat list berisi list (list bersarang)
# listNested = ['Mahasiswa', ['Dian', 17, 160.5], 'Lulus']
# listGabungan = [listKata, listAngka]

# # # mencetak list
# # print(listKosong)
# # print(listSatuItem)
# # print(listKata)
# # print(listAngka)
# # print(listMix)
# # print(listNested)
# # print(listGabungan)

# # # mencetak index dari list
# # print(listKata[0])
# # print(listKata[1])
# # print(listKata[2])
# # print(listKata[3])

# # # mencetak index dari list
# # print(listKata[-0])
# # print(listKata[-1])
# # print(listKata[-2])
# # print(listKata[-3])
# # print(listKata[-4])

# # mencetak index dari list
# print(listNested[0])
# print(listNested[1])
# print(listNested[1][0])
# print(listNested[1][1])
# print(listNested[1][2])
# print(listNested[2])