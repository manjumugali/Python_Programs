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
from Utility.UtilityTest import TestFunctional
l1 = LinkedList()


class Queue:
    try:
        my_list = TestFunctional.PrimeNumbers(1000)     # get all the prime numbers
        an_list = TestFunctional.anagramPrime(my_list)  # get all the anagram prime numbers
        print("---------------------------------------LinkedList Prime Numbers:--------------------------------\n")
        for i in an_list:
            l1.enQueue(int(i))  # invoking push method to add elements to queue
        print()
        l1.sizeOfList()     # invoking size() method to get size of queue
        print()
        l1.isEmpty()    # invoking isEmpty() to check queue is empty or not
        print()
        print("Printing Linked List Elements  Prime Numbers\n")
        l1.print_dQueue()   # remove all the elements from queue

        print("\n")
    except ValueError:
        print("-------------------------Oops Something Went Wrong Went--------------------------")