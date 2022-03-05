def tambah(x, y):
    return x + y
    
def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

print('Silahkan pilih operasi kalkulator')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')

print("========================================================")
pilih = input("Masukkan pilihan anda: ")

print("========================================================")
bil1 = int(input('Masukkan bilangan pertama : '))
bil2 = int(input('Masukkan bilangan kedua   : '))

print("========================================================")
print("Hasil dari", end=' ')

if pilih == '1':
    print(bil1, '+', bil2, '=', tambah(bil1, bil2))
elif pilih == '2':
    print(bil1, '-', bil2, '=', kurang(bil1, bil2))
elif pilih == '3':
    print(bil1, '*', bil2, '=', kali(bil1, bil2))
elif pilih == '4':
    print(bil1, '/', bil2, '=', bagi(bil1, bil2))
else:
    print('maaf, opsi yang anda masukkan salah')