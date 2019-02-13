"""
******************************************************************************
* Purpose: Write a program ​ Calendar that takes the read month and year from user and prints the Calendar of the month.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   22-01-2019
*
*******************************************************************************
"""
from Utility_DataStructure.DataStructureOperations import LinkedList

l1 = LinkedList()


class PrimeNumbers:
        while True:  # Never ending loop
            try:
                print("Enter the Range :")
                range = int(input())
                while range <= 0 or range > 1000:
                    print("Range value Should be > 0 and < 1000")
                    print("Enter the Range :")
                    range = int(input())

                l1.printPrimeNu2D(range)
                break
            except ValueError:
                print("Provide Only Integers")
                continue  # This causes it to continue