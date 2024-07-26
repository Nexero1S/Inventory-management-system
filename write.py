def new_inventory(lines, sn_number, old_stock, stock):
    nf = open("inventory.txt", "w")
    for i in range(len(lines)):
        x = lines[i].split(',')
        if i == sn_number - 1:
            x[3] = str(old_stock - stock)
        nf.write(x[0] + ',' + x[1] + ',' + x[2] + ',' + x[3] + ',' + x[4] + ',' + x[5])
    nf.close()


def update_inventory(lines, sn_number, old_stock, stock):
    #the code below updates the inventory according to the input
    nf = open("inventory.txt", "w")
    for i in range(len(lines)):
        x = lines[i].split(',')
        if i == sn_number - 1:
            x[3] = str(old_stock + stock)
        nf.write(x[0] + ',' + x[1] + ',' + x[2] + ',' + x[3] + ',' + x[4] + ',' + x[5])
    nf.close()