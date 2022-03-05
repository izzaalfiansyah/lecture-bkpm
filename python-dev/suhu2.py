def konversiSuhu(derajat, dari, ke):
    hasil = 0
    suhuKonversi = ke[0].upper()

    if dari[0].upper() == 'C':
        if suhuKonversi == 'F':
            hasil = float((9 * derajat) / 5 + 32)
        elif suhuKonversi == 'K':
            hasil = float(derajat + 273.15)
        elif suhuKonversi == 'R':
            hasil = float(4 / 5 * derajat)
    elif dari[0].upper() == 'F':
        if suhuKonversi == 'C':
            hasil = float((derajat - 32) * 5 / 9)
        elif suhuKonversi == 'K':
            hasil = float(((derajat - 32) * 5 / 9) + 273.15)
        elif suhuKonversi == 'R':
            hasil = float(4 / 9 * (derajat - 32))
    elif dari[0].upper() == 'K':
        if suhuKonversi == 'C':
            hasil = float(derajat - 273.15)
        elif suhuKonversi == 'F':
            hasil = float(((derajat - 273.15) * 9 / 5) + 32)
        elif suhuKonversi == 'R':
            hasil = float(4 / 5 * (derajat - 273))
    elif dari[0].upper() == 'R':
        if suhuKonversi == 'C':
            hasil = float((5 / 4) * derajat)
        elif suhuKonversi == 'F':
            hasil = float((9 / 4 * derajat) + 32)
        elif suhuKonversi == 'K':
            hasil = float((5 / 4 * derajat) + 273)

    print(' ==', ke, '==')    
    print('Suhu', ke, '=', hasil)
    print()

i = 0
print("=============================================")
print("WORKSHOP PEMROGRAMAN DASAR")
print("Selamat Datang di Program Konversi Suhu Sederhana")
print("=============================================")

while i == 0:
    suhu = ['Celcius', 'Reamur', 'Fahrenheit', 'Kelvin']

    j = 1
    for item in suhu:
        print(j, '. ', item, sep = '')
        j += 1

    satuan = input("Masukkan satuan yang akan dikonversi: ")
    pilihan = suhu[int(satuan) - 1]
    print()

    print(' ==', pilihan , '==')
    print('Suhu', pilihan, end = '')
    temperatur = input(': ')
    print("Mau diubah ke satuan suhu yang mana?")

    j = 1
    suhu.remove(pilihan)
    for item in suhu:
        print(j, '. ', item, sep = '')
        j += 1
    
    konversiSatuan = input("Pilih: ")
    konversiPilihan = suhu[int(konversiSatuan) - 1]
    print()
    
    konversiSuhu(dari = pilihan, ke = konversiPilihan, derajat = int(temperatur))

    lagi = int(input('Hitung lagi? [1 = ya, 0 = tidak]: '))
    if lagi == 1:
        print()
    else:
        i = 1