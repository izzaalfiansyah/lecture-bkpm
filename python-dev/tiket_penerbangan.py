#TIKET PENERBANGAN
import time
timezone = 7 * 3600

def garis():
    print("----------------------------------------------------------")

def ambilWaktuTerbang(jam_berangkat, menit_berangkat):
    global waktu_berangkat
    tick = time.time() * timezone
    menit, detik = divmod(tick, 60)
    jam, menit = divmod(menit, 60)
    hari, jam = divmod(jam, 24)

    waktu_berangkat = (hari * 86400) + (jam_berangkat * 3600) + (menit_berangkat * 60)
    if waktu_berangkat <= tick:
        waktu_berangkat = ((hari + 1) + 86400) + (jam_berangkat * 3600) + (menit_berangkat * 60)
    
    return waktu_berangkat

garis()
print("LIST PENERBANGAN WORKSHOP PEMROGRAMAN AIR")
garis()

print("kode penerbangan | tujuan |  harga tiket  | Jam berangkat")
garis()
print("     101         |   JKT  | Rp. 1.000.000 |  06:00")
print("     102         |   SUB  | Rp. 1.500.000 |  06:30")
print("     103         |   DPS  | Rp. 2.000.000 |  09:00")
print("     104         |   MLG  | Rp. 900.000   |  09:30")
print("     105         |   JOG  | Rp. 800.000   |  12:00")
print("     106         |   CBN  | Rp. 800.000   |  12:30")
print("     107         |   BTH  | Rp. 1.000.000 |  15:00")
print("     108         |   BDO  | Rp. 900.000   |  15:30")
print("     109         |   BKS  | Rp. 2.500.000 |  18:00")
print("     110         |   SRG  | Rp. 900.000   |  18:30")
print("     111         |   UPG  | Rp. 3.000.000 |  21:00")
print("     112         |   LBJ  | Rp. 5.000.000 |  21:30")
garis()

nama    = input("Nama Pembeli               : ")
nohp    = input("Nomor Handphone            : ")
asal    = input("Asal Kota                  : ")

tujuan = harga = 0
while True:
    jurusan = input("Kode Tujuan Penerbangan    : ")
    if jurusan == "101" :
        tujuan = "JAKARTA"
        harga = 1000000
        jam_berangkat, menit_berangkat = 6, 0
        break
    elif jurusan == "102" :
        tujuan = "SURABAYA"
        harga = 1500000
        jam_berangkat, menit_berangkat = 6, 30
        break
    elif jurusan == "103" :
        tujuan = "DENPASAR"
        harga = 2000000
        jam_berangkat, menit_berangkat = 9, 0
        break
    elif jurusan == "104" :
        tujuan = "MALANG"
        harga = 900000
        jam_berangkat, menit_berangkat = 9, 30
        break
    elif jurusan == "105" :
        tujuan = "JOGYAKARATA"
        harga = 800000
        jam_berangkat, menit_berangkat = 12, 0
        break
    elif jurusan == "106" :
        tujuan = "CIREBON"
        harga = 800000
        jam_berangkat, menit_berangkat = 12, 30
        break
    elif jurusan == "107" :
        tujuan = "BATAM"
        harga = 1000000
        jam_berangkat, menit_berangkat = 15, 0
        break
    elif jurusan == "108" :
        tujuan = "BANDUNG"
        harga = 900000
        jam_berangkat, menit_berangkat = 15, 30
        break
    elif jurusan == "109" :
        tujuan = "BEKASI"
        harga = 2500000
        jam_berangkat, menit_berangkat = 18, 0
        break
    elif jurusan == "110" :
        tujuan = "SEMARANG"
        harga = 900000
        jam_berangkat, menit_berangkat = 18, 30
        break
    elif jurusan == "111" :
        tujuan = "MAKASSAR"
        harga = 3000000
        jam_berangkat, menit_berangkat = 21, 00
        break
    elif jurusan == "112" :
        tujuan = "LABUHAN BAJO"
        harga = 5000000
        jam_berangkat, menit_berangkat = 21, 30
        break
    else:
        print('Kode salah!')

jumlah  = int(input("Jumlah beli pembelian      : "))

print()
if jumlah >= 3:
    potongan = (jumlah * harga) * 0.1
elif jumlah >= 6:
    potongan = (jumlah * harga) * 0.12
elif jumlah >= 9:
    potongan = (jumlah * harga) * 0.15
else:
    potongan = 0

total = int(jumlah * harga - potongan)
pajak = int(total * (10 / 100))
jumlah_bayar = total + pajak

garis()
print("WORKSHOP PEMROGRAMAN AIR")
garis()
print("Nama Pembeli         :", nama)
print("Nomor Handphone      :", nohp)
print("Asal Kota            :", asal)
print("Jumlah Beli          :", jumlah)
garis()
print("Harga Tiket          : Rp", harga)
print("Potongan             : Rp", potongan)
print("PPN 10%              : Rp", pajak)
garis()
print("Pelunasan pembayaran Tiket")

while True:
    print("Jumlah bayar         : Rp", jumlah_bayar)
    uang = int(input("Masukkan pembayaran  : Rp "))
    if uang < jumlah_bayar:
        print('Uang anda kurang!')
    else:
        break

garis()
kembalian = uang - jumlah_bayar
print("Uang kembalian       : Rp", kembalian)

garis()
print("Jam Berangkat        : %i:%i" % (jam_berangkat, menit_berangkat))
print()
tick = tick_lama = 0
waktu_berangkat = ambilWaktuTerbang(jam_berangkat, menit_berangkat)

while True:
    tick = time.time() + timezone
    if tick > tick_lama:
        tick_lama = tick + 1

        waktu_sisa = waktu_berangkat - tick
        menit, detik = divmod(waktu_sisa, 60)
        jam, menit = divmod(menit, 60)
        jam = jam % 24

        if jam > 1 or menit > 1 or detik > 1:
            print('Pesawat berangkat dalam %i:%i:%i' % (jam, menit, detik))
        else:
            print()
            print('Pesawat melakukan penerbangan...')
            break

garis()
print("             NIKMATI PERJALANANMU           ")
print("               JAGA KESELAMATAN             ")
garis()