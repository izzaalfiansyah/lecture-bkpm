def garis():
    print("-----------------------------------------------------------------------------------")

total_semua = 0
semua_produk = []

def foto():
    global total_semua
    global semua_produk

    garis()
    print(" FotoGraphy ")
    garis()
    print("  Kode Paket  |  Nama Paket  |  Harga   ")
    print("       1      |    Standar   |  1000000 ")
    print("       2      |    Medium    |  2000000 ")
    print("       3      |     BIG      |  3000000 ")
    garis()

    while True:
        kode = int(input("Masukkan Kode Paket yang akan dipesan      :  "))
        if kode not in [1, 2, 3]:
            print('Kode paket tidak valid!')
            continue
        else:
            break
    
    f_graphy = int(input("Masukkan Banyak paket yang akan dipesan    :  "))

    if kode == 1:
        total = f_graphy * 1000000
        produk_pilihan = str(f_graphy) + ' Paket photography Standar        Rp.' + str(total)
    elif kode == 2:
        total = f_graphy * 2000000
        produk_pilihan = str(f_graphy) + ' Paket photography Medium         Rp.' + str(total)
    elif kode == 3:
        total = f_graphy * 3000000
        produk_pilihan = str(f_graphy) + ' Paket photography BIG            Rp.' + str(total)

    garis()
    print(produk_pilihan)
    total_semua += total
    semua_produk.append(produk_pilihan)

def video():
    global total_semua
    global semua_produk

    garis()
    print(" VideoGraphy ")
    garis()
    print("  Kode Paket  |              Nama Paket          |  Harga   ")
    print("       1      |    Dokumentasi                   |  1000000 ")
    print("       2      |    Cinematic                     |  2000000 ")
    print("       3      |    Dokumentasi & Cinematic       |  3000000 ")
    garis()

    while True:
        kode = int(input("Masukkan Kode Paket yang akan dipesan      :  "))
        if kode not in [1, 2, 3]:
            print('Kode paket tidak valid!')
            continue
        else:
            break

    v_graphy = int(input("Masukkan Banyak paket yang akan dipesan    :  "))

    if kode == 1:
        total = v_graphy * 1000000
        produk_pilihan = str(v_graphy) + ' Paket videography Dokumentasi    Rp.' + str(total)
    elif kode == 2:
        total = v_graphy * 2000000
        produk_pilihan = str(v_graphy) + ' Paket videography Cinematic      Rp.' + str(total)
    elif kode == 3:
        total = v_graphy * 3000000
        produk_pilihan = str(v_graphy) + ' Paket videography Campuran       Rp.' + str(total)
    
    garis()
    print(produk_pilihan)
    total_semua += total
    semua_produk.append(produk_pilihan)

def bayar():
    global total_semua
    totalsemua = total_semua
    print()
    print("Total harus Dibayar  : Rp", totalsemua)
    uang = int(input("Uang Tunai Pembeli   : Rp "))
    kembalian = int(uang - totalsemua)
    print("Kembalian            : Rp", kembalian)

    print()
    print("=================================================================")
    print("====================== S T R U K   B E L I ======================")
    print("=================================================================")
    print(" Produk              :")

    print('-----------------------------------------------------------------')
    for item in semua_produk:
        print("", item)
    print('-----------------------------------------------------------------')

    print(" Tagihan                            : Rp.", totalsemua)
    print(" Uang                               : Rp.", uang)
    print(" Kembalian                          : Rp.", kembalian)
    print("=================================================================")
    print("==================== T E R I M A   K A S I H ====================")
    print("=================================================================\n\n")


#fungsi utama
def main():

    # menampilkan kalimat pembuka aplikasi
    garis()
    print('         APLIKASI STUDIO PHOTO        ')

    # memilih menu yang akan digunakan
    while True:
        garis()
        print('Pilih menu yang akan digunakan')
        print('1. Fhotography')
        print('2. VideoGraphy')
        print('3. Exit       ')

        while True:
            menu = input('Menu yang dipilih   : ')

            if menu in ['1', '2', '3']:
                if menu == "1":
                    foto()
                elif menu == "2":
                    video()
                elif menu == "3":
                    exit()
                
                break
            else:
                garis()
                print('Pilihan salah!')
                continue

        pilih = input("\nKonfirmasi lanjutan pembayaran |  (1) = tambah pesanan, (2) bayar pesanan? ")
        if pilih not in ['1', '2']:
            garis()
            print("Pilihan harus 1/2 ")
        else: 
            if pilih == '1':
                continue
            if pilih == '2':
                bayar()
                break


while True:
    main()

    # konfirmasi penggunaan aplikasi sekali lagi
    # garis()
    # lagi = input('Lakukan pemesanan studio photo lagi [Y/N]? ')
    # if lagi in ['Y', 'y']:
    #     print()
    #     print('Menunggu...')
    #     print()

    #     import time
    #     time.sleep(3)
    #     continue

    # garis()
    # print('              TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI')
    # garis()
    break
