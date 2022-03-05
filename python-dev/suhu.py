def konversiSuhu(suhu):
    derajat = int(suhu[:-1])
    inputan = suhu[-1]

    if inputan.upper() == 'C':
        jenis = 'Celcius'

        hasil1 = float((9 * derajat) / 5 + 32)
        hasil2 = float(derajat + 273.15)
        hasil3 = float(4 / 5 * derajat)

        jenis1 = 'Fahrenheit'
        jenis2 = 'Kelvin'
        jenis3 = 'Reamur'
    elif inputan.upper() == 'F':
        jenis = 'Fahrenheit'

        hasil1 = float((derajat - 32) * 5 / 9)
        hasil2 = float(((derajat - 32) * 5 / 9) + 273.15)
        hasil3 = float(4 / 9 * (derajat - 32))

        jenis1 = 'Celcius'
        jenis2 = 'Kelvin'
        jenis3 = 'Reamur'
    elif inputan.upper() == 'K':
        jenis = 'Kelvin'

        hasil1 = float(derajat - 273.15)
        hasil2 = float(((derajat - 273.15) * 9 / 5) + 32)
        hasil3 = float(4 / 5 * (derajat - 273))

        jenis1 = 'Celcius'
        jenis2 = 'Fahrenheit'
        jenis3 = 'Reamur'
    elif inputan.upper() == 'R':
        jenis = 'Reamur'

        hasil1 = float((5 / 4) * derajat)
        hasil2 = float((9 / 4 * derajat) + 32)
        hasil3 = float((5 / 4 * derajat) + 273)

        jenis1 = 'Celcius'
        jenis2 = 'Fahrenheit'
        jenis3 = 'Kelvin'
    else:
        print("Maaf, inputan tidak sesuai. Sesuaikan inputan dengan kriteria yang ada!")
        return 0

    print(derajat, jenis, '=', '{:.1f}'.format(hasil1), jenis1)
    print(derajat, jenis, '=', '{:.1f}'.format(hasil2), jenis2)
    print(derajat, jenis, '=', '{:.1f}'.format(hasil3), jenis3)


i = 0
print("=============================================")
print("WORKSHOP PEMROGRAMAN DASAR")
print("Selamat Datang di Program Konversi Suhu Sederhana")
print("=============================================")

while i == 0:
    temp = input("Masukkan suhu, diikuti dengan satuannya (Misal: 0C, 200F, 273K, 60R) = ")
    konversiSuhu(temp)

    lagi = int(input('Hitung lagi? [1 = ya, 0 = tidak]: '))
    if lagi == 1:
        print()
    else:
        i = 1