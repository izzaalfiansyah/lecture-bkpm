# import package
import requests as req
import json
import time

# fungsi membuat garis
def getMakanan():
    # mengambil data dari REST api
    data = req.get('https://masak-apa-tomorisakura.vercel.app/api/recipes')

    # inisialisasi makanan
    makanan = []
    for item in json.loads(data.text)['results']:
        makanan.append({
            'nama': item['title'].replace('Resep ', ''),
            'harga': int(item['portion'].replace(' Porsi', '') + '0000'),
            'waktu': item['times'].replace('mnt', ' detik').replace('jam', ' menit')
        })

    return makanan

# mengambil jarak waktu / interval waktu pemrosesan
def getInterval(waktu, jumlah):
    timezone = 7
    tick = time.time() + timezone * 60 * 60
    menit, detik = divmod(tick, 60)
    jam, menit = divmod(menit, 60)
    hari, jam = divmod(jam, 24)

    waktu = waktu.split(' ')
    interval = {'menit': 0, 'detik': 0}
    
    if 'menit' in waktu:
        interval['menit'] = int(waktu[waktu.index('menit') - 1]) * jumlah
    if 'detik' in waktu:
        interval['detik'] = int(waktu[waktu.index('detik') - 1]) * jumlah

    tickSelesai = (hari * 86400) + (jam * 3600) + ((menit + interval['menit']) * 60) + (detik + interval['detik'])
    return tickSelesai - tick

# menampilkan garis
def line():
    print("==========================================================================================")

# fungsi utama
def main():
    # inisialisasi variabel
    makanan = getMakanan()

    # ucapan selamat datang untuk user
    line()
    print("                 APLIKASI HAYALAN KAPSUL MAKANAN INSTAN MASA DEPAN")
    
    while True:
        # menampilkan daftar makanan
        line()
        print("-- Daftar Makanan --")

        no = 1
        for item in makanan:
            if no <= 3:
                print()
                print('No               : %s' % no)
                print('Nama Menu        : %s' % item['nama'])
                print('Harga            : Rp.%s' % item['harga'])
                print('Waktu Penyajian  : %s' % item['waktu'])
                no += 1

        while True:
            line()
            print('-- Pilih Menu --')
            try:
                pilihan = int(input("Menu Pilihan (No. Menu)    : "))

                if pilihan > 3:
                    line()
                    print("Menu pilihan tidak ditemukan!")
                    continue

                jumlah  = int(input("Jumlah                     : "))
                
                break
            except:
                line()
                print('Menu pilihan dan jumlah harus diisi angka!')
        
        # menampilkan menu yang dipilih user
        makanan_pilihan = makanan[pilihan - 1]
        total_harga = makanan_pilihan['harga'] * jumlah

        # menambahkan diskon jika jumlah pesanan >= 10
        diskon = 0
        if jumlah >= 10:
            diskon = 20
        
        line()
        print('-- Menu Terpilih --')
        print('Makanan Pilihan  : %s' % makanan_pilihan['nama'])
        print('Jumlah           : %i' % jumlah)
        print('Waktu Tunggu     : %s x %i' % (makanan_pilihan['waktu'], jumlah))
        print('Harga            : Rp.%i' % makanan_pilihan['harga'])
        print('Total Harga      : Rp.%i' % total_harga)
        print('Diskon           : ' + str(diskon) + '%')

        total_bayar = total_harga - (total_harga * (diskon / 100))
        print('Grand Total      : Rp.%i' % total_bayar)

        #konfirmasi pesanan
        line()
        print('-- Konfirmasi Pesanan --')
        konfirmasi = input('Apakah pesanan anda sudah benar [Y/N]? ')
        if konfirmasi in ['y', 'Y']:
            break
    
    # jasa boost proses pembuatan makanan apabila waktu tunggu 3 menit lebih
    interval = getInterval(makanan_pilihan['waktu'], jumlah)
    boost = False
    if interval >= (60 * 3):
        line()
        print('-- Jasa Boost Pemrosesan --')
        print('Pemrosesan untuk pesanan anda memakan waktu selama %i detik' % interval)
        print('Jasa boost akan mempersingkat waktu pemrosesan 3x lebih cepat \nAnda akan dikenakan biaya tambahan sebesar Rp.10000')
        boost = input('Gunakan jasa boost pemrosesan [Y/N] ?')

        if boost in ['Y', 'y']:
            interval = interval / 3
            print('Pemrosesan dipercepat menjadi %i detik' % interval)

    # proses scheduling hidangan
    line()
    print('-- Memproses Pesanan --')
    oldTick = 0
    while True:
        tick = time.time()
        if tick > oldTick:
            oldTick = tick + 1
            if interval > 0:
                print('waktu tunggu : %i detik lagi' % interval)
                interval -= 1
            else:
                break

    print()
    print("SELAMAT!!!")
    print('"%s" selesai dihidangkan' % makanan_pilihan['nama'])

    # melakukan pembayaran
    while True:
        try:
            line()
            print('-- Pembayaran --')

            if boost in ['y', 'Y']:
                print('Harga Pesanan            : Rp.%i' % total_bayar)
                print('Jasa Boost Pemrosesan    : Rp.10000')
                total_bayar += 10000

            print('Total Bayar              : Rp.%i' % total_bayar)
            uang = int(input('Masukkan uang anda       : Rp.'))
            hasil = uang - total_bayar
            
            if hasil < 0:
                line()
                print('Uang anda tidak cukup!')
                continue

            print()    
            print('Kembalian anda adalah Rp.%i' % hasil)
            break
        except:
            line()
            print('Uang yang dimasukkan harus berupa angka!')

    line()
    print("                                 TERIMA KASIH")
    line()

def app():
    main()

app()
