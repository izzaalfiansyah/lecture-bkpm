import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Kalkulator - Workshop Pemrograman Dasar')
window.configure(bg='#BEBEBE')

#style
btn = {
    'width': 6,
    'padding': 8,
    'bg': '#FFFFFF',
    'fg': '#000000'
}

# data

# function
def changeValue(params):
    if value.get().lower() == 'error':
        value.delete(0, tk.END)

    value.insert(tk.END, params)

def resultValue(evt = ''):
    text = value.get()

    if text[0] == '0':
        text = text[1:]

    try:
        result = eval(text)

        value.delete(0, tk.END)
        value.insert(0, result)
    except:
        messagebox.showerror(title="Error", message="Oops... Terjadi kesalahan pada operasi")

        value.delete(0, tk.END)
        value.insert(0, 'Error')

def nullValue():
    value.delete(0, tk.END)

def removeCharValue():
    value.delete(len(value.get()) - 1)

#process
value = tk.Entry(relief=tk.FLAT, width=(btn['width'] * 4 + 3), borderwidth=14, font=('Arial', 15))
value.grid(row=0, columnspan=4, pady=4, padx=4)
value.bind('<Return>', resultValue)

symbol = [
    tk.Button(text='C', command=nullValue, padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='DEL', command=removeCharValue, padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='(', command=lambda:changeValue('('), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text=')', command=lambda:changeValue(')'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='7', command=lambda:changeValue('7'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='8', command=lambda:changeValue('8'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='9', command=lambda:changeValue('9'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='+', command=lambda:changeValue(' + '), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='4', command=lambda:changeValue('4'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='5', command=lambda:changeValue('5'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='6', command=lambda:changeValue('6'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='-', command=lambda:changeValue(' - '), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='1', command=lambda:changeValue('1'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='2', command=lambda:changeValue('2'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='3', command=lambda:changeValue('3'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='*', command=lambda:changeValue(' * '), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='.', command=lambda:changeValue('.'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='0', command=lambda:changeValue('0'), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='=', command=resultValue, padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
    tk.Button(text='/', command=lambda:changeValue(' / '), padx=btn['padding'], pady=btn['padding'], width=btn['width'], bg=btn['bg'], fg=btn['fg'], font=('Arial'), relief=tk.FLAT),
]

i = 2
j = 0
for item in symbol:
    item.grid(row=i, column=j, padx=2, pady=2)
    if j >= 3:
        i += 1
        j = 0
    else:
        j += 1

value.focus()

window.mainloop()