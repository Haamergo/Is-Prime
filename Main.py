def checkprime():
    print("===========Cek Bilangan Prima=============")
    angka = int(input("Masukkan Angka:"))
    if angka > 1:
        for i in range(2, int(angka/2)+1):
            if (angka % i) == 0:
                print("{num} bukan angka prima".format(num = angka))
                break
        else:
            print("{num} adalah angka prima".format(num = angka))
    else :
        print("{num} bukan angka prima".format(num = angka))

while True:
    checkprime()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
    
###hadjshajkfhkash