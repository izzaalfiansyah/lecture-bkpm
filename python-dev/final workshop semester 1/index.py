# import package
import requests as req
import json
import time
from tabulate import tabulate

# fungsi membuat garis
def getMakanan():
    # mengambil data dari REST api
    data = req.get('https://masak-apa-tomorisakura.vercel.app/api/recipes')

    # inisialisasi makanan
    makanan = []
    for item in json.loads(data.text)['results']:
        nama = item['title'][:item['title'].find(',')]
        makanan.append({
            'nama': nama.replace('Resep ', ''),
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

#konversi interval ke menit dan detik
def getMenitDanDetik(interval):
    interval_menit, interval_detik = divmod(interval, 60)
    interval_menit = interval_menit % 60
    
    if interval_menit > 0:
        if interval_detik > 0:
            return str(int(interval_menit)) + ' menit & ' + str(int(interval_detik)) + ' detik'
        else:
            return str(int(interval_menit)) + ' menit'
    else:
        return str(int(interval_detik)) + ' detik'

# menampilkan garis
def line():
    print("==========================================================================================")

# fungsi utama
def main():
    # inisialisasi variabel
    makanan = getMakanan()
    grand_total = 0
    makanan_pilihan_total = []

    # ucapan selamat datang untuk user
    line()
    print("                 APLIKASI HAYALAN KAPSUL MAKANAN INSTAN MASA DEPAN")
    
    while True:
        # menampilkan daftar makanan
        line()
        print("-- Daftar Makanan --\n")

        no = 1
        data = []
        for item in makanan:
            data.append([
                no,
                item['nama'],
                'Rp.' + str(item['harga']),
                item['waktu']
            ])
            no += 1

        header = ['No', 'Nama Menu', 'Harga', 'Waktu Penyajian']
        print(tabulate(data, headers=header))

        while True:
            line()
            print('-- Pilih Menu --\n')
            try:
                pilihan = int(input("Menu Pilihan (No. Menu)    : "))

                if pilihan > len(makanan) or pilihan < 1:
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
        makanan_pilihan['jumlah'] = jumlah
        total_harga = makanan_pilihan['harga'] * jumlah

        # menambahkan diskon jika jumlah 5 atau lebih
        diskon = 0
        if jumlah >= 5:
            diskon = 5
        elif jumlah >= 10:
            diskon = 15
        elif jumlah >= 20:
            diskon = 25
        elif jumlah >= 50:
            diskon = 50
        
        line()
        print('-- Menu Terpilih --\n')
        print('Makanan Pilihan  : %s' % makanan_pilihan['nama'])
        print('Waktu Tunggu     : %s x %i' % (makanan_pilihan['waktu'], jumlah))
        print('Harga            : Rp.%i' % makanan_pilihan['harga'])
        print('Jumlah           : %i' % jumlah)
        print('Harga Keseluruhan: Rp.%i' % total_harga)
        print('Diskon           : ' + str(diskon) + '%')
        total_bayar = total_harga - (total_harga * (diskon / 100))
        print('Total Harga      : Rp.%i' % total_bayar)

        #konfirmasi pesanan
        line()
        print('-- Konfirmasi Pesanan --\n')
        konfirmasi = input('Apakah pesanan anda sudah benar [Y/N]? ')
        if konfirmasi in ['y', 'Y']:
            makanan_pilihan_total.append(makanan_pilihan)
            grand_total += total_bayar
        else:
            continue

        #total sementara
        line()
        print('-- Total Sementara --\n')
        print('Total Bayar      : Rp.%i' % grand_total)
        pesan_lagi = input('Pesan lagi [Y/N]? ')
        if not pesan_lagi in ['y', 'Y']:
            break
    
    # jasa boost proses pembuatan makanan apabila waktu tunggu 3 menit lebih
    interval = 0
    for item in makanan_pilihan_total:
        interval += getInterval(item['waktu'], item['jumlah'])
    
    boost = False
    if interval >= (60 * 3):
        line()
        print('-- Jasa Boost Pemrosesan --\n')
        print('Pemrosesan untuk pesanan anda memakan waktu selama %s' % getMenitDanDetik(interval))
        print('Jasa boost akan mempersingkat waktu pemrosesan 3x lebih cepat \nAnda akan dikenakan biaya tambahan sebesar Rp.10000')
        boost = input('Gunakan jasa boost pemrosesan [Y/N]? ')

        if boost in ['Y', 'y']:
            interval = interval / 3
            print('\nPemrosesan dipercepat menjadi %s' % getMenitDanDetik(interval))

    # proses scheduling hidangan
    line()
    print('-- Memproses Pesanan --\n')
    oldTick = 0
    while True:
        tick = time.time()
        if tick > oldTick:
            oldTick = tick + 1
            if interval > 0:
                print('waktu tunggu : %s lagi' % getMenitDanDetik(interval))
                interval -= 1
            else:
                break
    
    #pesanan selesai dihidangkan
    line()
    print("-- Pemrosesan selesai --\n")
    for item in makanan_pilihan_total:
        print('%ix %s' % (item['jumlah'], item['nama']))
    print('\nSelesai dihidangkan')

    # melakukan pembayaran
    while True:
        try:
            line()
            print('-- Pembayaran --\n')

            if boost in ['y', 'Y']:
                print('Harga Total Pesanan      : Rp.%i' % grand_total)
                print('Jasa Boost Pemrosesan    : Rp.10000')
                grand_total += 10000

            print('Total Bayar              : Rp.%i' % grand_total)
            uang = int(input('Masukkan uang anda       : Rp.'))
            hasil = uang - grand_total
            
            print()
            if hasil < 0:
                print('Uang anda tidak cukup!')
            elif hasil == 0:
                print('Uang anda pas.')
            else:
                print('Kembalian anda adalah Rp.%i' % hasil)
                break
        except:
            line()
            print('Uang yang dimasukkan harus berupa angka!')

    line()
    print("                                 TERIMA KASIH")
    line()

# cek jadwal kapan buka
statusHidup = False
waktuBuka = waktuTutup = 0

def cekJadwal():
    global statusHidup, waktuBuka, waktuTutup

    buka = 6, 0
    tutup = 21, 30

    waktu = time.time() + (7 * 3600)
    menit, detik = divmod(waktu, 60)
    jam, menit = divmod(menit, 60)
    hari, jam = divmod(jam, 24)

    waktuBuka = (hari * 86400) + (buka[0] * 3600) + (buka[1] * 60)
    waktuTutup = (hari * 86400) + (tutup[0] * 3600) + (tutup[1] * 60)

    if waktu > waktuBuka:
        statusHidup = True
        waktuBuka = ((hari + 1) * 86400) + (buka[0] * 3600) + (buka[1] * 60)
    if waktu > waktuTutup:
        statusHidup = False
        waktuTutup = ((hari + 1) * 86400) + (buka[0] * 3600) + (buka[1] * 60)

tick = tickLama = 0

while True:
    cekJadwal()
    tick = time.time() + (7 * 3600)

    if tick > tickLama:
        tickLama = tick + 1
        if statusHidup:
            main()
            input('\nPress Enter to continue.....')
            print('Loading.....\n')
        else:
            siswaWaktu = waktuBuka - tick
            menit, detik = divmod(siswaWaktu, 60)
            jam, menit = divmod(menit, 60)
            jam = jam % 24
            print('Toko sedang tutup. silahkan tunggu selama %i:%i:%i' % (jam, menit, detik))
