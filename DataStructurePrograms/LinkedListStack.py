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
from Utility.UtilityTest import TestFunctional
l1 = LinkedList()

class Stack:
    try:

        my_list = TestFunctional.PrimeNumbers(1000)      # get all the prime numbers
        an_list = TestFunctional.anagramPrime(my_list)      # get all the anagram prime numbers
        print("---------------------------------------LinkedList Prime Numbers:--------------------------------\n")
        for i in an_list:
            l1.sPush(int(i))    # invoking push method to add elements to stack

        print("\n")
        l1.sizeOfList()     # invoking size() method to get size of stack
        print()
        l1.isEmpty()    # invoking isEmpty() to check stack is empty or not
        print()
        print("--------------------------------------Printing in Reverse Order---------------------------------\n")
        l1.sDisplay()   # print all the stack elements

    except ValueError:
        print("-------------------------Oops Something Went Wrong Went--------------------------")