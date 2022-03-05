import time
timezone = 7 * 3600

def garis(kecil = False):
    if kecil:
        print("------------------------------------------------------------------------")
    else:
        print("========================================================================")

def cek_waktu(jam_mulai, menit_mulai):
    tick = time.time() + timezone
    menit, detik = divmod(tick, 60)
    jam, menit = divmod(menit, 60)
    hari, jam = divmod(jam, 24)

    waktu_mulai = (hari * 86400) + (jam_mulai * 3600) + (menit_mulai * 60)
    if waktu_mulai < tick:
        waktu_mulai = ((hari + 1) * 86400) + (jam_mulai * 3600) + (menit_mulai * 60)
    
    return waktu_mulai

def ambil_waktu(tick):
    menit, detik = divmod(tick, 60)
    jam, menit = divmod(menit, 60)
    jam = jam % 24

    return ('%i:%i:%i' % (jam, menit, detik))

garis()
print("                   APLIKASI PEMESANAN TIKET BIOSKOP")
garis()

nama    = input("Masukkan Nama      : ")
kota    = input("Asal Kota          : ")

while True:
    garis()
    print("Halo", nama, "dari", kota,"! Selamat datang di Loket Pemesanan Tiket")
    print("Silahkan pilih film yang akan kamu tonton!")

    garis()
    print("   Kode  | Nama Film                     | Waktu | Harga")
    garis(True)
    print("   101   | Encanto                       | 06:00 | Rp.12000")
    print("   102   | Venom: Let There Be Carnage   | 08:00 | Rp.15000")
    print("   103   | 365 Days                      | 10:00 | Rp.12000")
    print("   104   | Red Notice                    | 12:00 | Rp.14000")
    print("   105   | Jungle Cruise                 | 14:00 | Rp.13000")
    print("   106   | The Conjuring: Made Me Do It  | 16:00 | Rp.12000")
    print("   107   | Escape Room                   | 18:00 | Rp.14000")
    print("   108   | The Amazing Spiderman         | 20:00 | Rp.24000")
    print("   109   | Anunnaki                      | 22:00 | Rp.50000")
    garis()

    while True:
        pilihan = input("Kode Film Pilihan      : ")
        if pilihan == '101':
            film_pilihan = 'Encanto'
            jam_mulai, menit_mulai = 6, 0
            harga = 12000
        elif pilihan == '102':
            film_pilihan = 'Venom: Let There Be Carnage'
            jam_mulai, menit_mulai = 8, 0
            harga = 15000
        elif pilihan == '103':
            film_pilihan = '365 Days'
            jam_mulai, menit_mulai = 10, 0
            harga = 12000
        else:
            print('Kode Film tidak ditemukan!')
            continue
        break

    jumlah      = int(input("Jumlah Beli            : "))
    diskon = 0

    if jumlah > 5:
        diskon = harga * (5 / 100)
    elif jumlah > 10:
        diskon = harga * (10 / 100)
    elif jumlah > 20:
        diskon = harga * (25 / 100)

    total = harga * jumlah - diskon

    print("\n\n")
    garis()
    print("                     S T R U K   T I K E T")
    garis()
    print("Identitas Pemesan    :")
    garis(True)
    print("Nama                     :", nama)
    print("Asal Kota                :", kota)
    garis()
    print("Tiket Pesanan        :")
    garis(True)
    print("Film Pilihan             :", film_pilihan)
    print("Waktu Mulai              : %i:%i" % (jam_mulai, menit_mulai))
    print("Harga                    : Rp", harga)
    print("Jumlah                   :", jumlah)
    print("Potongan Harga           : Rp", diskon)
    print("Total                    : Rp", total)
    garis()
    print("\n\n")

    benar = input("Apakah pesanan anda sudah benar [Y/N]? ")
    if benar in ['Y', 'y']:
        break

garis()
print("Pembayaran Tiket")
while True:
    print("Total Pembayaran         : Rp", total)
    uang    = int(input("Masukkan Uang Anda       : Rp "))

    if uang < total:
        print("Uang anda tidak cukup!")
    else:
        kembalian = uang - total
        print("Kembalian                : Rp", kembalian)
        break

garis()
print("Silahkan menunggu...\n")

tick = tick_lama = 0
while True:
    waktu_mulai = cek_waktu(jam_mulai, menit_mulai)
    tick = time.time() + timezone
    if tick > tick_lama:
        tick_lama = tick + 1
        sisa_waktu = waktu_mulai - tick
        waktu_tunggu = ambil_waktu(sisa_waktu)
        if sisa_waktu > 1:
            print("Film akan dimulai dalam", waktu_tunggu)
        else:
            break

print("\nMemulai Film...")
garis()
print("             SELAMAT MENIKMATI FILM ANDA, TERIMA KASIH")
garis()