"""
******************************************************************************
* Purpose:  Program to Sort Array Elements using Marge Sort Algorithm
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   17-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class MargeSort:
    try:
        print("Enter Array Size :")
        size = int(input())  # Reading Array Size

        while size <= 0:  # Validating Size might not be  Negative Value
            size = int(input("Please Provide Valid Value(Positive Number)\n"))

        print("Enter The Array Elements : ")
        arr = []  # Empty List To store Array Elements
        for i in range(size):  # it loops until to reach to array size
            arr.append(input())  # reading Array Elements and Storing it into list
        print("Before Sorting :")
        print(arr)
        sort = obj.mergeSort(arr)    # Invoking function it takes Array List
        print("After Sorting :")
        print(sort)

    except ValueError:
        print("-------Please Provide Valid input(Positive Number)")