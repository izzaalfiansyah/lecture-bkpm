def line():
    print("========================================================")

def tambah(x, y):
    return x + y
    
def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'undefined'

def pilihan():
    print('Silahkan pilih operasi kalkulator')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')

line()
print("WORKSHOP PEMROGRAMAN DASAR")
print("Selamat Datang di Program Kalkulator Sederhana")
line()

pilihan()

lanjut = True

while(lanjut):
    line()
    pilih = input("Silahkan masukkan pilihan anda (1, 2, 3, dan 4): ")
    line()

    if pilih in ['1', '2', '3', '4']:
        bil1 = int(input('Masukkan bilangan pertama : '))
        bil2 = int(input('Masukkan bilangan kedua   : '))

        line()

        print("Hasil dari", end=' ')

        if pilih == '1':
            print(bil1, '+', bil2, '=', tambah(bil1, bil2))
        elif pilih == '2':
            print(bil1, '-', bil2, '=', kurang(bil1, bil2))
        elif pilih == '3':
            print(bil1, '*', bil2, '=', kali(bil1, bil2))
        else:
            print(bil1, '/', bil2, '=', bagi(bil1, bil2))
            
        lagi = input('Lakukan operasi kalkulator lagi [y/n]: ')

        line()
        if lagi not in ['y', 'Y']:
            print("Selamat tinggal! Semoga hari anda menyenangkan")
            lanjut = False
        else:
            pilihan()
    else:
        print("maaf, opsi yang anda masukkan salah")