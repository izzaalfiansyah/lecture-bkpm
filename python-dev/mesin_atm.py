import time

Pin = '123456'
Saldo = 100000

def garis():
    print("==================================================================================")

garis()
print("                     SELAMAT DATANG DI ATM BANK BRI-CLUB")
garis()

for i in range(3):
    print()
    inPin = input("SILAHKAN MASUKAN 6 Digit Pin Anda          : ")
    if inPin == Pin:
        print()
        print("Pin yang Anda Masukkan Benar")
        print()
        break
    else :
        print("PIn Salah")
        if i==2:
            garis()
            print("ANDA TELAH SALAH MEMASUKKAN PIN SEBANYAK 3X")
            print("UNTUK KEAMANAN, KARTU ANDA KAMI BLOKIR")
            print("SILAHKAN HUBUNGI BANK BRI-CLUB TERDEKAT")
            garis()
            exit()

while True:
    garis()
    print()
    print("01. Silahkan Pilih 1 Untuk Informasi Saldo")
    print("02. Silahkan Pilih 2 Untuk Penarikan Uang Tunai")
    print("03. Silahkan Pilih 3 Untuk Setor Tabungan")
    print("04. Silahkan Pilih 4 Untuk Keluar")
    print()

    Menu = input("Silahkan Pilih Menu yang Anda Inginkan         : ")
    print()
    garis()

    if Menu=='1':
        print()
        print("Sisa Saldo Anda      : ", Saldo)
        print()
        garis()
        Pilihan = input("Apakah Ingin Melanjutkan Program? (y/n)        : ")
        if Pilihan == 'n' :
            garis()
            print("Kartu anda akan keluar dari ATM")
            print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
            print()
            garis()
            break
        print()
        print()
    elif Menu=='2':
        if Saldo < 50000:
            print()
            print("Maaf Saldo Anda Tidak Cukup")
            print("Silahkan Isi Saldo Terlebih Dahulu")
            print()
            garis()
            Pilihan = input("Apakah Ingin Melanjutkan Program? (y/n)        : ")
            if Pilihan == 'n' :
                garis()
                print("Kartu anda akan keluar dari ATM")
                print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
                print()
                garis()
                break
            print()
        else:
            print("Jumlah Nominal Penarikan Sebesar 50000, 100000, 250000, 300000, 500000, 1000000")
            print()
            Tunai=int(input("Jumlah Penarikan Anda  : "))
            print()

            if Tunai > Saldo:
                garis()
                print("Maaf Saldo Anda Tidak Cukup")
                print("Silahkan Isi Saldo Terlebih Dahulu")
                print()
                garis()
                Pilihan = input("Apakah Ingin Melanjutkan Program? (y/n)        : ")
                if Pilihan == 'n' :
                    garis()
                    print("Kartu anda akan keluar dari ATM")
                    print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
                    print()
                    garis()
                    break
                print()

            if (Tunai==50000) or (Tunai==100000) or (Tunai==250000) or (Tunai==300000) or (Tunai==500000) or (1000000):
                Saldo=Saldo-Tunai

                garis()
                print("Melakukan penarikan saldo...")
                print()
                interval = 5
                tick = tick_lama = 0
                while True:
                    tick = time.time()
                    if tick > tick_lama:
                        tick_lama = tick + 1
                        if interval > 0:
                            print("Proses akan selesai dalam %i detik" % interval)
                            interval -= 1
                        else:
                            break
                print()
                print("Penarikan saldo berhasil...")
                garis()

                print()
                print("Saldo Ditarik        :", Tunai)
                print("Sisa Saldo Anda      :", Saldo)
                print()
                garis()
                Pilihan = input("Apakah Ingin Melanjutkan Program? (y/n)        : ")
                if Pilihan == 'n' :
                    garis()
                    print("Kartu anda akan keluar dari ATM")
                    print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
                    print()
                    garis()
                    break
            else:
                print("Nominal Tidak Diketahui")
                garis()
                Pilihan = input("Apakah Ingin Melanjutkan Program? (y/n)        : ")
                if Pilihan == 'n' :
                    garis()
                    print("Kartu anda akan keluar dari ATM")
                    print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
                    print()
                    garis()
                    break
    elif Menu=='3':
        print()
        Setor=int(input("Silahkan Masukan Nominal yang Ingin Anda Setor : "))
        Saldo += Setor
        
        print("Jumlah storan        :", Setor)
        print("Sisa Saldo Anda      :", Saldo)
        print()
        garis()
        Pilihan = input("Apakah Ingin Melanjutkan Program? (y/n)        : ")
        if Pilihan == 'n' :
            garis()
            print("Kartu anda akan keluar dari ATM")
            print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
            print()
            garis()
            break
    elif Menu=='4':
        print("Kartu anda akan keluar dari ATM")
        print("Terima Kasih Sudah Menggunakan Layanan Bank BRI-CLUB")
        print()
        garis()
        break


print("                     SEMOGA HARI ANDA MENYENANGKAN")
garis()