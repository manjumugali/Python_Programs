"""
******************************************************************************
* Purpose: Program To Implement Queue for Simple Balanced Cash.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   21-01-2019
*
*******************************************************************************
"""
from Utility_DataStructure.DataStructureOperations import LinkedList

l1 = LinkedList()


class Queue:
    try:
        bank_cash = 1000
        print("----------------Creates Banking Cash Counter For deposit Cash and withdraw Cash-----------------------")
        print("Enter Number of People in the Queue:")
        peoples = input()   # read Queue Size
        while not peoples.isdigit():    # validation size mush be Number
            print('Number Only')
            peoples = input()

        for i in range(0, int(peoples)):    # push operation
            l1.enQueue(i)
        for i in range(0, int(peoples)):
            print("Enter Your Choice:\n 1.Deposit\n 2.Withdraw\n 3.Exit\n")
            choice = input()    # read choice of user
            while not choice.isdigit():     # validation choice must be number
                print('Number Only')
                choice = input()
            if int(choice) == 1:    # if choice = 1 then deposit
                while True:
                    try:
                        print("Enter Deposit Amount: ")
                        deposit = int(input())  # read the deposit amount
                        bank_cash = bank_cash + deposit     # increment bank bal
                        l1.deQueue()    # pop operation
                        break
                    except ValueError:
                        print("InValid Input")
                        continue
            elif int(choice) == 2:  # if choice = 2 the withdraw cash
                if bank_cash != 0:  # bank cash should >0
                    print("Enter Amount To Withdraw")
                    withdraw = input()  # read withdraw amount
                    while not withdraw.isdigit():   # validation withdraw amount in Number
                        print("Enter Number Only")
                        withdraw = input()
                    if int(withdraw) <= bank_cash:  # if withdraw amount <=  bank bal process transaction
                        bank_cash = bank_cash - int(withdraw)   # decrement bank bank bal
                        l1.deQueue()

                    else:  # if withdraw amount >  bank bal show alert msg to user
                        print("Alert msg:---->Insufficient Fund in Bank")
                        print("1. Kindly Enter Cash within " + str(bank_cash) + " range\n2. If you do not want and leave")
                        w_choice = input("Enter choice:")   # read  withdraw choice from user

                        while not w_choice.isdigit():   # validate w_choice must be Number
                            print("Please Enter Valid Choice:")
                            w_choice = input()

                        if int(w_choice) == 1:  # if w_choice =  1
                            print('Enter Withdraw Amount:')
                            withdraw = input()  # read withdraw amount from user once again
                            while not withdraw.isdigit():   # validate amount must be in number
                                print("Please Enter Amount in Number")
                                withdraw = input()
                        if int(withdraw) <= bank_cash:  # if withdraw amount <=  bank bal process transaction
                            bank_cash = bank_cash - int(withdraw)   # decrement bank bank bal
                            l1.deQueue()

                        if int(w_choice) == 2:  # if w_choice = 2 leave the bank
                            l1.deQueue()
                else:
                    print("Server Unavailable.........!!!!!!!!!")
            elif int(choice) == 3:  # if choice = 3 exit from bank
                print("Bank Has Been Closed.................!!!!!!!!!!!!!!")
                exit()
            if i <= int(peoples):   # if i < size welcome next person
                print("..................Next Person...................!!!!!!!")
            print('Bank Balance ........ - >' + str(bank_cash))

    except RuntimeError:
        print("-----------------")
