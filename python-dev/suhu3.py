import tkinter as tk
from tkinter import messagebox

# data
data_satuan = ['Celcius','Fahrenheit','Kelvin','Reamur']

# function
def konversiSuhu(evt = ''):
    inputan = satuan_variable.get()[0]

    try:
        derajat = int(temperature.get())
    except:
        messagebox.showwarning('Warning', 'Temperatur suhu harus diisi dengan angka')
        return 0

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
        messagebox.showwarning('Warning', 'Opsi satuan belum dipilih!')
        return 0

    messagebox.showinfo('Sukses', ('\
        Hasil konversi suhu dari ' + str(derajat) + jenis[0] + '\n\
        =======================\n\
        ' + jenis1 + '  = ' + str(hasil1) + jenis1[0].upper() + '\n\
        ' + jenis2 + '  = ' + str(hasil2) + jenis2[0].upper() + '\n\
        ' + jenis3 + '  = ' + str(hasil3) + jenis3[0].upper()) + '\
        ')


# process
window = tk.Tk()
window.title('Konversi Suhu - Workshop Pemrograman Dasar')

tk.Label(text="Program Konversi Suhu").grid(row=0, column=0, pady=6, padx=2)

temperature = tk.Entry(borderwidth=5, relief=tk.FLAT, width=20, font=('Arial', 15), justify=tk.CENTER)
temperature.grid(row=1, column=0, padx=5, pady=2)
temperature.bind('<Return>', konversiSuhu)

satuan_variable = tk.StringVar()
satuan_variable.set('Pilih Satuan')
satuan = tk.OptionMenu(window, satuan_variable, *data_satuan)
satuan.config(bg='#FEFEFE', width=17, relief=tk.FLAT, font=('Arial', 15))
satuan.grid(row=2, column=0, padx=5, pady=2)

tk.Button(text='SUBMIT', width=25, padx=5, pady=5, command=konversiSuhu).grid(row=3, column=0, pady=9, padx=2)

window.mainloop()