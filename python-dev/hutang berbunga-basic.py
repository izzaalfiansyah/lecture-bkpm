hutang = float(input('Masukkan Hutang      : '))
bunga = float(input('Masukkan Bunga       : '))
jumlah_hari = int(input('Masukkan jumlah hari : '))

hutang_akhir = hutang * ((1 + (bunga / 100)) ** jumlah_hari)

print('====================================')
print('Total Hutang         : %i' % hutang_akhir)
print('Terima kasih! Silahkan hutang lagi!')