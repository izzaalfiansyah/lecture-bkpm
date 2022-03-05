reRun = True

while reRun:
    try: 
        size = int(input("Masukkan ukuran: "))
        reRun = False

        for i in range(size):
            initNumber = size
            initSeparator = size

            while initSeparator > 0:
                print('', end= ' ')
                initSeparator -= 2

            while initNumber > 0:
                print('*', end=' ')
                initNumber -= 1

            print('')
    except:
        print("ukuran yang anda masukkan harus berupa angka")