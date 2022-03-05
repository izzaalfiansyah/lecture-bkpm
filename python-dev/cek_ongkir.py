import time

def garis():
    print("===============================================================")

def cek_waktu(jam_tempuh, menit_tempuh):
    tick = time.time()
    waktu_tempuh = tick + (jam_tempuh * 3600) + (menit_tempuh * 60)
    return waktu_tempuh

def mulai():
    garis()
    print("        APLIKASI CEK HARGA PENGIRIMAN KOTA JEMBER")

    garis()
    nama = input("Masukkan Nama    : ")
    print()
    print("Selamat datang", nama, ". Kami akan membantumu")
    print("mengecek harga pengiriman barang")
    
    while True:
        garis()
        print("List Daerah      : ")
        garis()
        print(" Kode    | Kota Tujuan   | Harga per KG  | Waktu Tempuh")
        garis()
        print(" 001     | Tuban         | Rp 12000      | 7 jam")
        print(" 002     | Bojonegoro    | Rp 10000      | 6 jam")
        print(" 003     | Mojokerto     | Rp 7000       | 4 jam 30 menit")
        print(" 004     | Malang        | Rp 6500       | 4 jam")
        print(" 005     | Surabaya      | Rp 9000       | 5 jam")
        print(" 006     | Bondowoso     | Rp 2000       | 1 jam 30 menit")
        print(" 007     | Lumajang      | Rp 1500       | 1 jam")
        print(" 008     | Situbondo     | Rp 3000       | 2 jam")
        print(" 009     | Probolinggo   | Rp 4000       | 2 jam 20 menit")
        
        garis()
        while True:
            tujuan  = input("Masukkan kode kota tujuan      : ")
            if tujuan == '001':
                kota_tujuan = 'Tuban'
                harga = 12000
                jam_tempuh, menit_tempuh = 7, 0
            elif tujuan == '002':
                kota_tujuan = 'Bojonegoro'
                harga = 10000
                jam_tempuh, menit_tempuh = 6, 0
            elif tujuan == '003':
                kota_tujuan = 'Mojokerto'
                harga = 7000
                jam_tempuh, menit_tempuh = 4, 30
            elif tujuan == '004':
                kota_tujuan = 'Malang'
                harga = 6500
                jam_tempuh, menit_tempuh = 4, 0
            elif tujuan == '005':
                kota_tujuan = 'Surabaya'
                harga = 9000
                jam_tempuh, menit_tempuh = 5, 0
            elif tujuan == '006':
                kota_tujuan = 'Bondowoso'
                harga = 2000
                jam_tempuh, menit_tempuh = 1, 30
            elif tujuan == '007':
                kota_tujuan = 'Lumajang'
                harga = 1500
                jam_tempuh, menit_tempuh = 1, 0
            elif tujuan == '008':
                kota_tujuan = 'Situbondo'
                harga = 3000
                jam_tempuh, menit_tempuh = 2, 0
            elif tujuan == '009':
                kota_tujuan = 'Probolinggo'
                harga = 4000
                jam_tempuh, menit_tempuh = 2, 20
            else:
                print("Kode kota tujuan tidak ditemukan!")
                continue
            break

        berat   = int(input("Masukkan berat barang (KG)     : "))

        potongan = 0
        if berat > 10:
            potongan = harga * (5 / 100)
        elif berat > 20:
            potongan = harga * (10 / 100)
        elif berat > 50:
            potongan = harga * (30 / 100)

        total = harga * berat - potongan

        garis()
        print("Konfirmasi Pengiriman")
        print("---------------------------------------------------------------")
        print("Nama             :", nama)
        print("Asal Kota        : Jember")
        print("Kota Tujuan      :", kota_tujuan)
        print("Berat Barang     :", berat, "KG")
        print("Waktu tempuh     : %i jam %i menit" % (jam_tempuh, menit_tempuh))
        print("Harga per KG     : Rp", harga)
        print("Potongan Harga   : Rp", potongan)
        print("Total Bayar      : Rp", total)
        
        garis()
        pilihan = input("Apakah pesanan anda sudah benar [Y/N]? ")
        if pilihan in ['Y', 'y']:
            break

    garis()
    print("Pembayaran Pengiriman")
    print("---------------------------------------------------------------")
    print("Total Bayar          : Rp", total)
    while True:
        uang = int(input("Masukkan uang anda   : Rp "))
        if uang < total:
            print("Uang anda kurang!")
        else:
            break
    
    kembalian = uang - total
    print("Kembalian            : Rp", kembalian)

    garis()
    print("Mengirim Barang...")
    print()

    tick = tick_lama = 0
    waktu_tempuh = cek_waktu(jam_tempuh, menit_tempuh)

    while True:
        tick = time.time()
        if tick > tick_lama:
            tick_lama = tick + 1
            
            waktu_sisa = waktu_tempuh - tick
            menit, detik = divmod(waktu_sisa, 60)
            jam, menit = divmod(menit, 60)
            jam = jam % 24

            if waktu_sisa > 0:
                print("Barang akan sampai dalam %i:%i:%i" % (jam, menit, detik))
            else:
                break
    
    print("\nBarang berhasil dikirim. Sampai ke tujuan...")

    garis()
    print("        TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI")
    print("             SEMOGA HARI ANDA MENYENANGKAN")
    garis()

mulai()