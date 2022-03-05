try:
    hutang = float(input('Masukkan Hutang      : '))
    bunga = float(input('Masukkan Bunga       : '))
    jumlahHari = int(input('Masukkan jumlah hari : '))

    hutangAkhir = hutang * ((1 + (bunga / 100)) ** jumlahHari)

    print('====================================')
    print('Total Hutang         : %i' % hutangAkhir)
    print('Terima kasih! Silahkan hutang lagi!')
except:
    print('====================================')
    print('field harus diisi dengan angka, plisss!')