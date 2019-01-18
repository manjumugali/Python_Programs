"""
******************************************************************************
* Purpose:  Reads in strings from standard input and prints them in sorted order.Uses insertion sort.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   16-01-2019
*
******************************************************************************
"""
import re

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()

class InsertionSort:
    try:
        print("Enter The String")
        str1 = input()      # read The String
        onlystr = re.sub('[^A-Za-z]+', ' ', str1)   # Remove The All Special Characters
        word = onlystr.split()  # It splits the Given Sentence into Words(by Space)
        print("Before Sorting:")
        print(word)
        print("After Sorting:")
        sort = c1.insertionSort(word)   # Invoking function it takes One arguments As list
        print(sort)
    except ValueError:
        print("...........oops Something Went Wrong.........")