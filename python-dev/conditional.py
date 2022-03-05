try:
    usia = int(input("Masukkan usia anda: "))

    if usia >= 17:
        kerja = input("Apakaha anda sudah bekerja atau masih kuliah [kerja/kuliah]? ")
        if kerja == "kerja":
            print("Anda sudah memiliki penghasilan")
        elif kerja == "kuliah":
            print("Semangat menjalani kuliah")
        else:
            print("Status yang anda masukkan salah")
    elif 4 < usia < 17:
        print("Anda adalah seorang siswa")
    else:
        print("Anda adalah balita")
except:
    print("Usia yang anda masukkan bukan angka")
