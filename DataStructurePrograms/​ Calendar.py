"""
******************************************************************************
* Purpose: Write a program ​ Calendar that takes the read month and year from user and prints the Calendar of the month.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   21-01-2019
*
*******************************************************************************
"""
from Utility_DataStructure.DataStructureOperations import LinkedList

l1 = LinkedList()


class Calendar:
        try:
            print("Enter the Value of the Month:")
            month = input()    # read month value
            while not month.isdigit() or int(month) > 12:  # validating month
                print("Please Provide Valida input for month")
                month = input()
            print("Enter the Value of Year")
            year = input()  # read year value
            while not year.isdigit() or int(year) < 999:  # validating year
                print("Please Provide Valid Input")
                year = input()
            l1.printCalOfMonth(int(month), int(year))
        except ValueError:
            print("Please Enter Only Integer Value")

