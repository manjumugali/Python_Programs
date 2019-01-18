"""
******************************************************************************
* Purpose:  Read The Input From The File And Search The Word In that list
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

class ReadFile:
    try:
        newfile = open("txtfile", "r")  # File IO open() function to Opens the file with read mode
        word = newfile.read()      # reading file data and it converts to single String
        onlystr = re.sub('[^A-Za-z]+', ' ', word)   # Remove The All Special Characters
        my_list = onlystr.split()   # It splits the Given String Sentence into Words(by Space)
        print("Before Sorting :")
        print(my_list)
        print("After Sorting :")
        res = c1.insertionSort(my_list)     # Invoking function it takes One arguments As list
        print(res)
        print("Enter The Word To Search :")
        word = input()      # Reading Word To Search
        c1.searchElement(res, word)     # Invoking function it takes Two arguments As list,String
    except IOError:
        print("...........oops Something Went Wrong.........")
