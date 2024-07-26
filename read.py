def read():
    print('---------------------------------------------------------------------------------------------')
    print("S.N.\t\tName\t\tBrand\t\tPrice\t\tStock\t\tProcessor\t\tGPU ")
    print('---------------------------------------------------------------------------------------------')

    f = get_file()
    sn = 0
    for line in f:
        sn = sn + 1
        x = line.replace(",", "\t\t")
        print(sn, "\t\t", x)
    print('---------------------------------------------------------------------------------------------')

def get_file():
    f = open("inventory.txt", "r+")
    return f