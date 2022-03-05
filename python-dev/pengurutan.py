# import library kebutuhan
import time

# fungsi untuk mengurutkan data
def urutkanData(data, tipe):
    i = 0
    while i < len(data):
        j = 0
        while j < len(data) - 1:
            if tipe == '1':
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            j += 1
        i += 1
    return data

# membuat garis
def garis():
    print('=====================================================')

# menunggu pemrosesan berdasarkan interval yang ditentukan
def loading():
    garis()
    print('Menunggu...')
    
    tick = tickLama = 0
    interval = 3
    while True:
        tick = time.time()
        if tick > tickLama:
            if interval > 0:
                tickLama = tick + 1
                print('Pengurutan akan selesai dalam %i detik' % interval)
                interval -= 1
            else:
                break

# fungsi utama
def main():
    # menampilkan kalimat pembuka aplikasi
    garis()
    print('             APLIKASI PENGURUTAN DATA')
    
    # memilih bentuk data yang akan diurutkan
    while True:
        garis()
        print('Pilih tipe data yang akan diurutkan')
        print('1. String (karakter atau kata)')
        print('2. Integer (angka atau bilangan)')
        bentuk = input('Tipe data pilihan   : ')

        if bentuk in ['1', '2']:
            break
        else:
            garis()
            print('Pilihan harus 1 atau 2!')

    # memasukkan jumlah data
    while True:
        try:
            garis()
            jumlah = int(input('Masukkan jumlah data         : '))

            if jumlah <= 1:
                garis()
                print('Jumlah data harus lebih dari 1!')
                continue

            break
        except:
            garis()
            print('Jumlah data harus berisi angka!')
    
    # push data ke list data
    garis()
    i, data = 1, []
    for item in range(jumlah):
        # cek bentuk tipe data yang akan diurutkan
        if bentuk == '1':
            val = input('Data ke %s                   : ' % i)
        else:
            while True:
                try:
                    val = int(input('Data ke %s                   : ' % i))
                    break
                except:
                    print('Data harus berupa angka!')
        
        data.append(val)
        i += 1
    
    # memilih tipe pengurutan apakah ASC atau DESC
    while True:
        garis()
        print('Pilih tipe pengurutan')
        print('1. Dari terkecil ke terbesar')
        print('2. Dari terbesar ke terkecil')
        pilihan = input('Tipe pengurutan pilihan  : ')
        
        if pilihan in ['1', '2']:
            break
        else:
            garis()
            print('Pilihan harus 1 atau 2!')

    # memanggil fungsi loading
    loading()

    # mengurutkan data dengan fungsi urutkanData
    garis()
    data_urut = urutkanData(data, pilihan)
    print('Data berhasil diurutkan')
    
    print('Bentuk tipe data adalah ', end='')
    if pilihan == '1':
        print('String (karakter atau kata)')
    else:
        print('Integer (angka atau bilangan)')
    
    print('Tipe pengurutan adalah ', end='')
    if pilihan == '1':
        print('dari terkecil ke terbesar')
    else:
        print('dari terbesar ke terkecil')

    # menampilkan data yang telah diurutkan
    garis()
    i = 1
    for item in data_urut:
        print('Data ke %s                   : %s' % (i, item))
        i += 1

while True:
    main()

    # konfirmasi penggunaan aplikasi sekali lagi
    garis()
    lagi = input('Lakukan pengurutan data lagi [Y/N]? ')
    if lagi in ['Y', 'y']:
        print()
        print('Menunggu...')
        print()

        time.sleep(3)
    else:
        garis()
        print('     TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI')
        garis()
        break