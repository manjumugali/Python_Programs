"""
******************************************************************************
* Purpose:  Program To Demonstration Regular Expression
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   27-01-2019
*
******************************************************************************
"""
from ObjectOrientedPrograms.StockBean import Stock
from OOPS_Utility.Test_Oops_Utility import StockReport

class StockPortfolio:
    while True:
        try:
            print("Enter the N number of Stocks")
            no_of_stock = int(input())                              # read number of stock as size
            global s1                                               # creating global object of StockBean class
            share_list = []
            i = 0
            while i < no_of_stock:                                  # it loops until i < num of stocks
                print("..........", i+1, "Stock data.......")
                print("Enter the Company Name:")
                name = input()                                      # read company name
                while not name.isalpha() or len(name) < 0:          # validating company name
                    print("Invalid Data..........")
                    print("Enter the Company Name:")
                    name = input()

                print("Enter the no of Share")
                no_of_share = input()                               # read no of shares
                while not no_of_share.isdigit() or len(no_of_share) < 0:        # validating user input
                    print("Invalid Data..........")
                    print("Enter the no of shares:")
                    no_of_share = input()

                print("Enter the Share Price")
                price = input()                                     # read share price
                while not price.isdigit() or len(price) < 0:        # validating share price
                    print("Invalid Data..........")
                    print("Enter the Share price:")
                    price = input()

                s1 = Stock(name, no_of_share, price)    # creating object Stock class and passing parameters
                s1.setName(name)                        # on s1 object invoking setName() function takes 1 parameter
                s1.setNoShare(no_of_share)              # on s1 object invoking setNoShare() function takes 1 parameter
                s1.setPrice(price)                      # on s1 object invoking setPrice() function takes 1 parameter
                share_list.append(s1)
                i += 1                                  # increment i value by 1
            s2 = StockReport(share_list)                # creating object StockReport class and passing parameters
            s2.stockReport()                            # on s2 object invoking stockReport() function
            break
        except ValueError:
            print("Invalid data......->Only Numbers...................!!!!!!!!!!!!!!!")
            continue


if __name__ == "__main__":
    StockPortfolio()