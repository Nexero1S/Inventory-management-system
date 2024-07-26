import fileinput
import random
from datetime import date
from datetime import datetime
import read
import write
import operation


def main():
    global val
    a = True
    while a:

        print('-----------------------------------')
        print('EVIL INCORPORATIONS LAPTOPS')
        print('-----------------------------------')
        print('Nayabazar, Kathmandu')
        print('Contact us at evilincorp1@gmail.com')
        print('-----------------------------------')
        print('Welcome to our store')
        print('What can we help you with')
        read.read()
        print('-----------------------------------')
        print('-----------------------------------')
        print('Press 1 to Add to inventory')
        print('Press 2 to Sell products')
        print('Press 3 to exit the program')
        print('-----------------------------------')

        while True:
            try:
                val = int(input("Press any number to continue: "))
            except:
                print("please enter number only")
            if val == 1:
                operation.add_inventory()
                break
            elif val == 2:
                operation.sell_inventory()
                break
            elif val == 3:
                a = False
                break
            else:
                print("The option u chose is invalid")

main()
