#NAMA :
#GOL :
#NIM :
import time

# INPUT
# membuat garis
def garis(kecil = False):
    if kecil:
        print('-----------------------------------------------------')
    else:
        print('=====================================================')


# menampilkan kalimat pembuka aplikasi
while True:
    while True:
        garis()
        print('          SELAMAT DATANG DI COFFEE SHOP')
        garis()
        print(" List coffee ")
        print(" 1. Americano        : Rp 20.000")
        print(" 2. Mochaccino       : Rp 20.000")
        print(" 3. Cappuccino       : Rp 20.000")
        print(" 4. Espresso         : Rp 20.000")
        print(" 5. Latte            : Rp 20.000")
        print(" 6. Vanilla Latte    : Rp 23.000")
        print(" 7. Caramel Latte    : Rp 23.000")
        print(" 8. Hazelnut Latte   : Rp 23.000")
        garis()

        while True:
            listMenu        = str(input(" Masukkan nomor minuman yang ingin di pesan    = "))
            jumlahPesanan   = int(input(" Jumlah dibeli                                 = "))

            if listMenu == "1":
                namaMenu = "Americano"
                hargaSatuan = 20000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "2":
                namaMenu = "Mochaccino"
                hargaSatuan = 20000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "3":
                namaMenu = "Cappuccino"
                hargaSatuan = 20000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "4":
                namaMenu = "Espresso"
                hargaSatuan = 20000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "5":
                namaMenu = "Latte"
                hargaSatuan = 20000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "6":
                namaMenu = "Vanilla Latte"
                hargaSatuan = 23000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "7":
                namaMenu = "Caramel Latte"
                hargaSatuan = 23000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            elif listMenu == "8":
                namaMenu = "Hazelnut Latte"
                hargaSatuan = 23000
                harga = hargaSatuan * jumlahPesanan
                pajak = int(harga * 0.1)
                totalHarga = int(harga + pajak)
            else:
                print(" Maaf,Menu yang dipilih tidak tersedia ")
                continue
            break
        


        garis(kecil=True)
        print(" Menu                :", namaMenu)
        print(" Harga Satuan        : Rp", hargaSatuan)
        print(" Jumlah Pesanan      :", jumlahPesanan)
        print(" Harga Total         : Rp", harga)
        print(" Pajak               : Rp", pajak)
        garis(kecil=True)
        print(" Total Pembayaran    : Rp", totalHarga)
        garis(kecil=True)

        garis()
        benar = input("Apakah pesanan anda sudah benar [Y/N]? ")
        if benar in ['Y', 'y']:
            break
    
    garis()
    print("Silahkan konfirmasi pembayaran anda terlebih dahulu!")
    print()
    print("Total Pembayaran         : Rp", totalHarga)
    while True:
        uang = int(input("Masukkan uang anda       : Rp "))
        if uang < totalHarga:
            print("Uang anda tidak cukup!")
        else:
            kembalian = uang - totalHarga
            print("Kembalian                : Rp", kembalian)
            break

    # menunggu pembuatan minuman
    garis()
    print("Pesanan sedang diproses. Mohon menunggu...")
    print()
    menit = 5
    interval = (menit * 60) * jumlahPesanan # 5 * 60 detik * jumlahPesanan
    tick = tickLama = 0
    while True:
        tick = time.time()
        menit, detik = divmod(interval, 60)
        jam, menit = divmod(menit, 60)
        if tick > tickLama:
            tickLama = tick + 1
            if interval > 0:
                print("Pesanan akan selesai dalam %i:%i" % (menit, detik))
                interval -= 1
            else:
                break
    print()
    print("Pesanan selesai dihidangkan...")

    # konfirmasi penggunaan aplikasi sekali lagi
    garis()
    lagi = input('Ingin memesan lagi [Y/N]? ')

    #PERULANGAN
    if lagi in ['Y', 'y']:
        print()
        print('Menunggu...')
        print()

        time.sleep(3)
    else:
        garis()
        print('         TERIMA KASIH, SELAMAT MENIKMATI')
        garis()
        break