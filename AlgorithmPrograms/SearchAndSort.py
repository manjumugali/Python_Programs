"""
******************************************************************************
* Purpose:  Program To Search Element using Binary Search and Sort The Element Using Insertion Sort And Bubble Sort
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   15-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class SearchAndSort:
    try:
        print("Enter Array Size :")
        size = int(input())     # Reading Array Size

        while size <= 0:  # Validating Size might not be  Negative Value
            size = int(input("Please Provide Valid Value(Positive Number)\n"))

        print("**************************First Just Try With Integers Only******************************")
        print("Enter The Array Elements : ")
        arr = []  # Empty List To store Array Elements as Integer numbers
        for i in range(size):   # it loops until to reach to array size
            arr.append(int(input()))  # reading Array Elements and Storing it into list

        print("**********************Sorted list Of Elements: Using Insertion Sort*****************")
        sort = c1.insertionSort(arr)        # Invoking function it takes One arguments As list
        print(sort)
        print("Enter The Element To Search :")
        ele = int(input())  # Reading Number To Search
        c1.searchElement(sort, ele)     # Invoking function it takes Two arguments As list,Integer
        print("***********************Sorted list Of Elements: Using Bubble Sort******************")
        barr = c1.bubbleSort(arr)   # Invoking function it takes One arguments As list
        print(barr)

        print("***************************Now Try With String Input*****************")
        print("Enter The Array Elements : ")
        arr = []    # Empty List To store Array Elements as Strings
        for i in range(size):   # it loops until to reach to array size
            arr.append(input())     # reading Array Elements and Storing it into list
        print("**********************Sorted list Of Elements: Using Insertion Sort*****************")
        sort = c1.insertionSort(arr)    # Invoking function it takes One arguments As list
        print(sort)
        print("Enter The Element To Search :")
        ele = input()   # Reading Word To Search
        c1.searchElement(sort, ele)     # Invoking function it takes Two arguments As list,Integer
        print("***********************Sorted list Of Elements: Using Bubble Sort******************")
        barr = c1.bubbleSort(arr)   # Invoking function it takes One arguments As list
        print(barr)
    except ValueError:
        print("...........oops Something Went Wrong.........")