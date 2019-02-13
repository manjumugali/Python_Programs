"""
******************************************************************************
* Purpose:  Program To Inventory Management
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   29-01-2019
*
******************************************************************************
"""
from OOPS_Utility.Test_Oops_Utility import StockDetails

s = StockDetails()


class StockAccount:
    print("!.......Welcome To Stock Account........!")
    print("-----------------------------------------")
    s.displayStocks()  # on s object invoking displayStocks() function
    while True:
        try:
            print("Enter Choice:\n1.Login\n2.User_Registrations\n3.Exit")
            choice = int(input())  # read user choice as number
            if choice == 1:
                result = s.login()  # if choice == 1 invoke login() function
                if result is False:
                    result = s.registration()
                    continue
            elif choice == 2:
                s.registration()  # if choice == 2 invoke registration() function
                continue
            elif choice == 3:  # if choice == 3 exit from the program
                exit()
            else:  # else invalid choice
                print("Enter the valida choice")
                continue
            break
        except ValueError:
            print("invalid choice(only Number)")
            continue
