"""
******************************************************************************
* Purpose:  To hold all Utility class,
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   27-01-2019
*
******************************************************************************
"""
import datetime
import json
import random
import re
from Utility.UtilityTest import TestFunctional
from Utility_DataStructure.DataStructureOperations import LinkedList
import numpy as np

t = TestFunctional()
l1 = LinkedList()
l2 = LinkedList()
l3 = LinkedList()
l4 = LinkedList()

'''******************************************************************************************************************'''


class InventoryDetails:
    @staticmethod
    def inventoryDetails(data):
        print()
        print("------------------WELCOME TO INVENTORY DATA MANAGEMENT--------------\n")
        result = 0
        r_kg = 0
        try:
            print("----------------RICE DETAILS-----------------\n")
            print("Rice_Name         Rice_Weight      Rice_Price")
            print("---------------------------------------------")
            j = 0
            for i in data["rice"]:  # to loop over rice details and print rice items
                print(j, i["name"], end="        ")
                j += 1
                print(i["weight"], end="                 ")
                print(i["price"])

            print()

            for i in data["rice"]:  # by using rice key collecting details
                r_kg = r_kg + int(i["weight"])
                result = result + int(i["weight"]) * int(i["price"])  # calculating total Value

            print("Number Of Rice Types           :", len(data["rice"]), "types")  # no of items
            print("Total Rice Weight is           :", r_kg, "kgs")  # weight of all items
            print("Total Price of All the Rice is :", result)  # total value
            print()
            print("----------------PULSES DETAILS-------------------\n")
            print("Pulses_Name      Pulses_Weight      Pulses_Price")
            print("---------------------------------------------------")
            for i in data["pulse"]:  # to loop over pulse details and print pulse items
                print(i["name"], end="        ")
                print(i["weight"], end="                 ")
                print(i["price"])

            print()
            for i in data["pulse"]:  # by using pulse key collecting details
                r_kg = r_kg + int(i["weight"])
                result = result + int(i["weight"]) * int(i["price"])  # calculating total Value

            print("Number Of Pulses Types           :", len(data["pulse"]), "types")  # no of items
            print("Total Pulses Weight is           :", r_kg, "kgs")  # weight of all items
            print("Total Price of All the Pulses is :", result)  # total value
            print()
            print("----------------Wheat's DETAILS-------------------\n")
            print("Wheat's_Name      Wheat's_Weight      Wheat's_Price")
            print("---------------------------------------------------")
            for i in data["wheat"]:  # to loop over wheat details and print wheat items
                print(i["name"], end="              ")
                print(i["weight"], end="                    ")
                print(i["price"])
            print()

            for i in data["wheat"]:  # by using wheat key collecting details
                r_kg = r_kg + int(i["weight"])
                result = result + int(i["weight"]) * int(i["price"])  # calculating total Value

            print("Number Of Wheat's Types           :", len(data["wheat"]), "types")  # no of items
            print("Total Wheat's Weight is           :", r_kg, "kgs")  # weight of all items
            print("Total Price of All the Wheat's is :", result)  # total value
            print()
        except RuntimeError:
            print("--------------")


'''******************************************************************************************************************'''


class RegularExp:
    def __init__(self, name, last_name, phone_no, date):  # constructor takes 4 parameters
        self.my_list = [name, last_name, phone_no, date]  # store into list

    string = "Hello <<name>> , We have your full name as <<full name>> in our system.\nyour contact number is 91-xxxxxxxxxx .\nPlease,let us know in case of any clarification Thank you BridgeLabz 01/01/2019."
    temp = ['<<name>>', '<<full name>>', '91-xxxxxxxxxx.', "01/01/2019"]

    def useOfRegex(self):
        rpl_str = re.sub(self.temp[0], self.my_list[0],
                         self.string)  # replace <<name>> with user input using regex sub()
        rpl_str1 = re.sub(self.temp[1], self.my_list[1],
                          rpl_str)  # replace <<full name>> with user input using regex sub()
        rpl_str2 = re.sub(self.temp[2], self.my_list[2],
                          rpl_str1)  # replace 91-xxxxxxxxxx with user input using regex sub()
        rpl_str3 = re.sub(self.temp[3], self.my_list[3],
                          rpl_str2)  # replace 01/01/2019 with user input using regex sub()
        print(rpl_str3)


'''******************************************************************************************************************'''


class StockReport:
    def __init__(self, share_list):  # constructor takes 1 parameters
        self.share_list = share_list

    def stockReport(self):
        print("--------------------------------------")
        print("Stock_Name   No_Of_Shares  Share_Price")
        print("--------------------------------------")
        list1 = []
        for i in range(len(self.share_list)):  # loop over list
            print(self.share_list[i].getName(), "      ", self.share_list[i].getNoShare(), "           ",
                  self.share_list[i].getPrice(), "\n")
            each_total = str(int(self.share_list[i].getNoShare()) * (
                int(self.share_list[i].getPrice())))  # calculate total value of each stock
            list1.append(each_total)  # append to list

        total = 0
        for i in range(len(list1)):  # loop over list
            print("Stock Report of '", self.share_list[i].getName(), "'is :", list1[i], "\n")
            total = total + int(list1[i])  # calculate total sum of all stocks
        print("Total Stock Value is", total)


'''******************************************************************************************************************'''


class DeckOfCard:
    def __init__(self, rank, suits):  # constructor takes 2 parameters
        self.rank = rank
        self.suits = suits
        self.row = 4  # initialize row value
        self.col = 9  # initialize col value

    def shuffleCards(self):  # function to shuffle cards
        list_cards = []

        for i in range(36):  # list size 36
            for j in range(0, 9):
                random_no = random.randint(0, 12)  # generates the Random number between(0-12)
                cards_rank = self.rank[random_no]  # to pick rank of card
                random_no_s = random.randint(0, 3)  # generates the Random number Between(0-3)
                cards_rank = cards_rank + ' ' + self.suits[random_no_s]  # to pick suits of card
                if list_cards.__contains__(cards_rank) is False:  # check for repeated element
                    if len(list_cards) != 36:
                        list_cards.append(cards_rank)  # if not contains by card_list then add it into list
        return list_cards  # return list

    def dealCard(self, card_list):  # function to deal cards and takes 1 parameter
        count = 0
        matrix = [[0 for j in range(self.col)] for i in range(self.row)]  # create 2D array
        for i in range(self.row):  # loop over row size
            for j in range(self.col):  # loop over col size
                matrix[i][j] = card_list[count]  # assign value to 2D array
                count += 1  # increment count by 1

        a = np.array(matrix)  # assign matrix to a
        print("\n")
        print("Distributing Cards To Players After Shuffle:")
        print(
            "-----------------------------------------------------------------------------------------------------------------------")
        print("Player-1", end=": ")
        for i in a[0]:  # loop over matrix[0][9]
            print(i, end="   ")
        print("\n")
        print("Player-2", end=": ")
        for i in a[1]:  # loop over matrix[1][9]
            print(i, end="   ")
        print("\n")
        print("Player-3", end=": ")
        for i in a[2]:  # loop over matrix[2][9]
            print(i, end="   ")
        print("\n")
        print("Player-4", end=": ")
        for i in a[3]:  # loop over matrix[3][9]
            print(i, end="   ")
        print()
        return a


'''******************************************************************************************************************'''


class InventoryManagement:
    def __init__(self, data):  # constructor takes 1 parameter
        self.data = data

    def inventoryData(self):  # function to take inventory data
        while True:
            try:
                count = 1
                while count > 0:  # loops until user should enter exit optin
                    print("Enter the Choice :\n1.Display\n2.Add_Products\n3.Exit")
                    choice = int(input())  # read choice
                    if choice == 1:  # if choice == 1 print details of the inventory
                        I1 = InventoryDetails()
                        I1.inventoryDetails(self.data)
                    elif choice == 2:  # if choice == 2 add new item to stock
                        print("Enter the Item Name:(rice or pulse or wheat)")
                        item = input()  # read item key
                        while not item.isalpha():  # validating item key
                            print("invalid input........(only letters)")
                            print("Enter the Item Name:(Rice or Pulses or Wheat's)")
                            item = input()

                        print("Enter the name of the '", item)
                        name = input()  # read item name
                        while not name.isalpha():  # validating item name
                            print("invalid input........(only letters)")
                            print("Enter the name of the '", item)
                            name = input()

                        print("Enter the weight of the '", name)
                        weight = input()  # read weight of item

                        while not weight.isdigit():  # validating weight
                            print("invalid input........(only Numbers)")
                            print("Enter the weight of the '", name)
                            weight = input()

                        print("Enter the Price of the '", name)
                        price = input()  # read price of the item

                        while not price.isdigit():  # validating price
                            print("invalid input........(only Numbers)")
                            print("Enter the price of the '", name)
                            price = input()

                        with open("../ObjectOrientedPrograms/Inventory.json",
                                  'w') as norfile:  # open json file with write mode
                            self.data[item].append({
                                "name": name,
                                "weight": weight,
                                "price": price
                            })  # updating json file
                            norfile.write(json.dumps(self.data, indent=2))  # convert python object to json object
                            norfile.close()  # close file
                    elif choice == 3:  # if choice == 3 exit from program
                        exit()
                    else:  # else invalid choice
                        print("Invalid Number(Choice)")
                        continue

                break
            except ValueError:
                print("Invalid Choice(Number Only)")
                continue


'''***************************************************************************************************************** '''


class StockDetails:
    def __init__(self):
        with open("stock.json", "r") as file:
            json_file = file.read()
            file.close()
            self.stock = json.loads(json_file)

        with open("customers.json", "r") as file:
            json_file = file.read()
            file.close()
            self.user = json.loads(json_file)

        with open("BuyStock.json", "r") as file:
            json_file = file.read()
            file.close()
            self.buy = json.loads(json_file)

        with open("DateTime.json", 'r') as file:
            json_file = file.read()
            file.close()
            self.datetime = json.loads(json_file)

    def displayStocks(self):
        print("sl_no    Name     No_of_shares     Price")
        for i in range(len(self.stock['stock'])):
            print(i, "     ", self.stock['stock'][i]['name'], "      ", self.stock['stock'][i]['no_of_share'],
                  "       ", self.stock['stock'][i]['price'])

    def displayCustomers(self):
        print("sl_no     Name      Address      Phone_no        No_of_shares     Amount")
        for i in range(len(self.user['customer'])):
            print(i, "    ", self.user['customer'][i]['name'], "     ", self.user['customer'][i]['address'],
                  "   ", self.user['customer'][i]['phone_no'], "    ", self.user['customer'][i]['no_of_share'],
                  "            ", self.user['customer'][i]['amount'])

    def registration(self):
        print("Enter username:")
        name = input()
        while not name.isalpha():
            print("invalid input........(only letters)")
            print("Enter user name")
            name = input()
        print("Enter address")
        adrss = input()
        while len(adrss) < 0:
            print("invalid input")
            print("Enter address")
            adrss = input()
        print("Enter phone_no")
        phone_no = input()
        while not re.match("(91-)[7-9][0-9]{9}", phone_no) or len(phone_no) > 13:
            print("Please Provide Valid Phone-Number(91-XXXXXXXXXX)")
            phone_no = input()
        print("Enter the no of share")
        no_of_share = input()
        while not no_of_share.isdigit() or len(no_of_share) < 0:
            print("Invalid Data..........")
            print("Enter the no of shares:")
            no_of_share = input()
        print("Enter the Amount")
        amount = input()
        while not amount.isdigit():
            print("Invalid input(only numbers)")
            print("Enter the Amount")
            amount = input()
        with open("../ObjectOrientedPrograms/customers.json", 'w') as norfile:
            self.user['customer'].append({
                "name": name.title(),
                "address": adrss,
                "phone_no": phone_no,
                "no_of_share": int(no_of_share),
                "amount": int(amount)
            })
            norfile.write(json.dumps(self.user, indent=2))
            norfile.close()
        print("User Registered Successfully........!")

    @staticmethod
    def validate(no_of_share, total_share):

        if not no_of_share.isdigit() or len(no_of_share) < 0:
            print("invalid input(only numbers)")
            return True
        elif int(no_of_share) > total_share:
            print("available shares '", total_share, "' please enter within this range")
            return True
        else:
            return False

    def login(self):
        result = False
        print("Enter the username")
        u_name = input()
        while not u_name.isalpha():
            print("invalid input........(only letters)")
            print("Enter user name")
            u_name = input()
        count = 0
        while count < len(self.user['customer']):
            if self.user['customer'][count]['name'] == u_name.title():
                print("login is Successfully done...!")
                result = True
                while True:
                    try:
                        print("Enter Choice:\n1.Buy-Share\n2.Sell-Share\n3.printStock_Report")
                        choice = int(input())
                        if choice == 1:
                            self.buy_shares(count)
                        elif choice == 2:
                            self.sell_share(count)
                        elif choice == 3:
                            self.stockReport()
                        else:
                            print("invalid choice")
                            continue
                        break
                    except ValueError:
                        print("invalid input(number Only)")
                        continue
                return True
            count += 1
        if result is False:
            print("Failed To Login(user is not Registered)...!----->Please First Do Registration")
        return False

    def buy_shares(self, index):
        self.displayStocks()
        print("Enter the sl_no(0-", len(self.stock['stock']) - 1, ")to buy company share")
        sl_no = input()
        while not sl_no.isdigit() or int(sl_no) > len(self.stock['stock']) - 1:
            print("invalid input(Only numbers)")
            print("Enter the sl_no(0-", len(self.stock['stock']) - 1, ")to buy company share")
            sl_no = input()
        print("Enter the no of share to Buy")
        no_of_share = input()
        total_share = self.stock['stock'][int(sl_no)]['no_of_share']
        while self.validate(no_of_share, int(total_share)) is True:
            no_of_share = input()
        share_price = self.stock['stock'][int(sl_no)]['price']
        total_price = int(no_of_share) * int(share_price)
        print("You need to pay this much amount to buy :", total_price)
        bal = int(self.user['customer'][index]['amount']) - total_price
        updated_share = int(self.user['customer'][index]['no_of_share']) + int(no_of_share)
        with open("../ObjectOrientedPrograms/customers.json", 'w') as norfile:
            self.user['customer'][index]['amount'] = bal
            self.user['customer'][index]['no_of_share'] = updated_share
            norfile.write(json.dumps(self.user, indent=2))
            norfile.close()
        print()
        print("-------------------------Updated Customers Details--------------------")
        self.displayCustomers()
        print()
        updated_cmp_share = self.stock['stock'][int(sl_no)]['no_of_share'] - int(no_of_share)
        with open("../ObjectOrientedPrograms/stock.json", 'w') as norfile:
            self.stock['stock'][int(sl_no)]['no_of_share'] = updated_cmp_share
            norfile.write(json.dumps(self.stock, indent=2))
            norfile.close()
        print()
        print("------------------------Updated Stock Details-------------------------")
        self.displayStocks()

        with open("../ObjectOrientedPrograms/BuyStock.json", 'w') as wfile:
            self.buy['buy'].append({
                'result': 'buy'.title(),
                'no_of_share': no_of_share
            })
            wfile.write(json.dumps(self.buy, indent=2))
            wfile.close()
        time = '{0:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())
        with open("../ObjectOrientedPrograms/DateTime.json", 'w') as wfile:
            self.datetime['datetime'].append({
                'result': 'buy'.title(),
                'no_of_share': no_of_share,
                'date_time': time
            })
            wfile.write(json.dumps(self.datetime, indent=2))
            wfile.close()

    def sell_share(self, index):
        self.displayStocks()
        print("Enter the sl_no(0-", len(self.stock['stock']) - 1, ") to sell share for specific company")
        sl_no = input()

        while not sl_no.isdigit() or int(sl_no) > len(self.stock['stock']) - 1:
            print("invalid input(Only numbers)")
            print("Enter the sl_no(0-", len(self.stock['stock']) - 1, ")to buy customer  share")
            sl_no = input()
        print("Enter the no of share to sell(customer to Company)")
        no_of_share = input()
        total_share = self.user['customer'][index]['no_of_share']
        while self.validate(no_of_share, total_share):
            no_of_share = input()

        share_price = self.stock['stock'][int(sl_no)]['price']
        total_amount = int(no_of_share) * share_price
        updated_share = self.user['customer'][index]['no_of_share'] - int(no_of_share)
        updated_amount = self.user['customer'][index]['amount'] + total_amount

        with open("../ObjectOrientedPrograms/customers.json", 'w') as norfile:
            self.user['customer'][index]['no_of_share'] = updated_share
            self.user['customer'][index]['amount'] = updated_amount
            norfile.write(json.dumps(self.user, indent=2))
            norfile.close()

        print("-------------------------Updated Customers Details--------------------")
        self.displayCustomers()

        updated_cmp_share = self.stock['stock'][int(sl_no)]['no_of_share'] + int(no_of_share)
        with open("../ObjectOrientedPrograms/stock.json", 'w') as norfile:
            self.stock['stock'][int(sl_no)]['no_of_share'] = updated_cmp_share
            norfile.write(json.dumps(self.stock, indent=2))
            norfile.close()
        print()
        print("-------------------------Updated Stock Details--------------------")
        self.displayStocks()
        with open("../ObjectOrientedPrograms/BuyStock.json", 'w') as wfile:
            self.buy['buy'].append({
                'result': 'sell'.title(),
                'no_of_share': no_of_share
            })
            wfile.write(json.dumps(self.buy, indent=2))
            wfile.close()
        time = '{0:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())
        with open("../ObjectOrientedPrograms/DateTime.json", 'w') as wfile:
            self.datetime['datetime'].append({
                'result': 'sell'.title(),
                'no_of_share': no_of_share,
                'date_time': time
            })
            wfile.write(json.dumps(self.datetime, indent=2))
            wfile.close()

    def stockReport(self):
        my_list = []
        print()
        print("--------------Stock Details-------------")
        print("sl_no    Name     No_of_shares     Price")
        for i in range(len(self.stock['stock'])):
            print(i, "     ", self.stock['stock'][i]['name'], "      ", self.stock['stock'][i]['no_of_share'],
                  "       ", self.stock['stock'][i]['price'])
            my_list.append(self.stock['stock'][i]['no_of_share'] * self.stock['stock'][i]['price'])

        total_value = 0
        for i in my_list:
            total_value = total_value + i
        print()
        print("Total Stock Value is this mush :", total_value)


'''******************************************************************************************************************'''


class LinkedListQueue:
    def __init__(self, data):  # constructor takes 1 parameter
        self.data = data

    def enqueueCompanyShares(self):  # function to push data into linked list
        for i in range(len(self.data['stock'])):  # loop over stock key data
            l1.add(self.data['stock'][i]['no_of_share'])  # invoke linked list add() function
        print()
        print("-----------Company Share in Linked List------------\n")
        l1.display()  # invoke LinkedList display() function
        print("\n")
        l1.sizeOfList()  # to print size of the LinkedList


'''******************************************************************************************************************'''


class StackStockSymbol:
    def __init__(self, data):  # constructor takes 1 parameter
        self.data = data

    def pushStockSymbols(self):  # function to push details into stack
        my_list = []
        for i in range(len(self.data['buy'])):  # loop over on buy key elements
            str1 = "[" + self.data['buy'][i]['result'] + "-" + self.data['buy'][i]['no_of_share'] + "Shares]"
            my_list.append(str1)  # add concatenated String to list

        my_list.reverse()  # reverse the list
        for i in my_list:  # loop over list
            l1.sPush(i)  # invoke push() function
        print("------------------------------------------")
        print("maintaining the Stock Symbol Buy or Sell\n")
        l1.sDisplay()  # to print invoke display() function
        print()


'''******************************************************************************************************************'''


class DateTimeLinkedListQueue:
    def __init__(self, data):  # constructor takes 1 parameter
        self.data = data

    def enQueueTransaction(self):  # function to push data into queue
        my_list = []
        for i in range(len(self.data['datetime'])):  # loop over on datetime key elements
            str1 = "[" + self.data['datetime'][i]['result'] + "-" + self.data['datetime'][i][
                'no_of_share'] + "shares" + " Transaction_At:" + self.data['datetime'][i]['date_time'] + "]"
            my_list.append(str1)  # add concatenated String to list
        for i in my_list:  # loop over list
            l1.enQueue(i)  # invoke enQueue() function
        print()
        print("---------  DateTime of the transactions ------\n")
        l1.print_dQueue()  # to print invoke display() function
        print()


'''******************************************************************************************************************'''


class LinkedListQueueCards:
    def __init__(self, cards):  # constructor takes 1 parameter as list
        self.cards = cards
        self.my_list = []  # creating 4 empty array list
        self.my_list1 = []
        self.my_list2 = []
        self.my_list3 = []

    def enQueueCards(self):  # function to push cards into Queue
        self.my_list = t.insertionSort(self.cards[0])  # invoking bubbleSort() function to sort cards
        self.my_list1 = t.insertionSort(self.cards[1])
        self.my_list2 = t.insertionSort(self.cards[2])
        self.my_list3 = t.insertionSort(self.cards[3])
        print("\n")
        print("After Sorting and adding into Linked List")
        print(
            "---------------------------------------------------------------------------------------------------------------------------------------")
        print("Player-1", end=": ")
        for i in self.my_list:  # loop over list
            l1.enQueue(i)  # invoke enQueue() function of Queue class
        l1.print_dQueue()  # to print cards invoke print_dQueue() function
        print("\n")

        print("Player-2", end=": ")
        for i in self.my_list1:  # loop over list
            l2.enQueue(i)  # invoke enQueue() function of Queue class
        l2.print_dQueue()  # to print cards invoke print_dQueue() function
        print("\n")

        print("Player-3", end=": ")
        for i in self.my_list2:  # loop over list
            l3.enQueue(i)  # invoke enQueue() function of Queue class
        l3.print_dQueue()  # to print cards invoke print_dQueue() function
        print("\n")

        print("Player-4", end=": ")
        for i in self.my_list3:  # loop over list
            l4.enQueue(i)  # invoke enQueue() function of Queue class
        l4.print_dQueue()  # to print cards invoke print_dQueue() function
        print("\n")
