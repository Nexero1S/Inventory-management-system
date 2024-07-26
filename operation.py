import write
import read
from datetime import date
from datetime import datetime
import random


def add_inventory():
    global sn_number, stock
    # the read  below calls reads and displays the  data
    # the int covers the input to make it into a integer
    # input serial number
    sn_number_loop = True
    while sn_number_loop:
        try:
            sn_number = int(input("Input serial number to add to inventory: "))

            if sn_number > 5:
                print('please enter sn number upto 5')
            elif sn_number < 1:
                print('please enter sn number greater than 0')
            else:
                sn_number_loop = False
        except:
            print("please enter number only")
#if and else thapnu parcha hola
    stock_loop = True
    while stock_loop:
        try:
            stock = int(input("Enter the number of stocks: "))
            stock_loop = False
        except:
            print("please enter number only")

    # get_file() opens and reads from above
    f = read.get_file()
    # f.readlines  reads line of inventory
    lines = f.readlines()
    # with the code  it fixes the index numbers on inventory
    selected_item = lines[sn_number - 1]
    # splits  string into a list
    items = selected_item.split(",")
    # storing value in variable
    name = items[0]
    brand = items[1]
    str_price = items[2]
    # replaces $ with null
    price = int(str_price.replace("$", ""))
    old_stock = int(items[3])
    processor = items[4]
    gpu = items[5]

    write.update_inventory(lines, sn_number, old_stock, stock)
    generate_receipt(stock, name, brand, price)


def generate_receipt(stock, name, brand, price):
    global ph_number, now

    net_amount = price * stock
    vat = (13 / 100) * net_amount
    gross_amount = net_amount + vat

    username = input("Enter your Name: ")

    ph_number_lop = True
    while ph_number_lop:
        ph_number = input("Enter your phone number: ")
        if ph_number.isnumeric():
            ph_number_lop = False
        else:
            print("Please enter valid phone number")
    #this code gives the current date and time
    purchase_date = date.today()
    time = datetime.now()
    now = time.strftime("%I:%M:%S")
    #the code below generate a receipt on a txt file
    receipt_number = random.randint(1, 10000)
    f = open("receipt" + str(receipt_number) + ".txt", "w")
    #the code below write the given data on lines
    f.writelines("EVIL INCORPORATIONS LAPTOPS:  " + "\n")
    f.writelines("receipt_numeber:  " + str(receipt_number) + "\n")
    f.writelines("Distributer Name:  " + username + "\n")
    f.writelines("Phone:  " + str(ph_number) + "\n")
    f.writelines("name of laptop:  " + name + "\n")
    f.writelines("brand of laptop:  " + brand + "\n")
    f.writelines("total amount without VAT:  " + str(net_amount) + "\n")
    f.writelines("13% vat of total amount:  " + str(vat) + "\n")
    f.writelines("total amount with vat:  " + str(gross_amount) + "\n")
    f.writelines("date of purchase:  " + str(purchase_date) + "\n")
    f.writelines("time of purchase:  " + str(now) + "\n")
    f.close()

def sell_inventory():
    global sn_number, stock, is_shipping
    sn_number_loop = True
    while sn_number_loop:
        try:
            sn_number = int(input("Input serial number to sell from inventory: "))
            if sn_number > 5:
                print('please enter sn number upto 5')
            elif sn_number < 1:
                print('please enter sn number greater than 0')
            else:
                sn_number_loop = False
        except:
            print("please enter number only")

    stock_loop = True
    while stock_loop:
        try:
            stock = int(input("Enter the number of sold stocks: "))
            stock_loop = False
        except:
            print("please enter number only")

    shipping_loop = True
    while shipping_loop:
        try:
            is_shipping = input("Do you want to include shipping ? (yes / no ): ")

            if is_shipping == 'yes' or is_shipping == 'no':
                print('please enter either yes or no')
            else:
                shipping_loop = False
        except:
            print("please enter number only")

    # get_file() opens and reads from above
    f = read.get_file()
    # fg.readlines  reads line of inventory
    lines = f.readlines()
    # with the code  it fixes the index numbers on inventory
    selected_item = lines[sn_number - 1]
    # splits  string into a list
    items = selected_item.split(",")
    # storing value in variable
    name = items[0]
    brand = items[1]
    str_price = items[2]
    # replaces $ with null
    price = int(str_price.replace("$", ""))
    old_stock = int(items[3])
    processor = items[4]
    gpu = items[5]

    generate_bill(stock, name, brand, price, is_shipping)
    write.new_inventory(lines, sn_number, old_stock, stock)


def generate_bill(stock, name, brand, price, is_shipping):
        #global statement lets access to whole function
        global total_cost, total_amount

        shippingcost_loop =True
        while shippingcost_loop:
            #try catch
            try:
                total_amount = price * stock
                if is_shipping == 'yes':
                    shipping_cost = int(input("type the shipping cost"))
                    total_cost= total_amount + shipping_cost
                else:
                    total_cost = total_amount

                shippingcost_loop = False
                #the code below works if the conditon is false
            except:
                 print("Please enter number only")

        username = input("Enter Customer Name: ")

        purchase_date = date.today()
        time = datetime.now()
        now = time.strftime("%I:%M:%S")
        bill_number = random.randint(1, 10000)
        f = open("bill" + str(bill_number) + ".txt", "w")
        f.writelines("bill_number:  " + str(bill_number) + "\n")
        f.writelines("Customers Name:  " + username + "\n")
        f.writelines("name of laptop:  " + name + "\n")
        f.writelines("brand of laptop:  " + brand + "\n")
        f.writelines("Number of items:  "+ str(stock)+"\n")
        f.writelines("date of purchase:  " + str(purchase_date) + "\n")
        f.writelines("time of purchase:  " + str(now) + "\n")
        f.writelines("total amount without shipping cost:  " + str(total_amount) + "\n")
        f.writelines("total cost with shipping cost:  "+ str(total_cost)+"\n")
        f.close()
