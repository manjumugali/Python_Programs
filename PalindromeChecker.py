"""
******************************************************************************
* Purpose: Program To Implement DQueue to check Palindrome Checker.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   23-01-2019
*
*******************************************************************************
"""
import re
from builtins import ValueError

from Utility_DataStructure.TestDQueue import TestDQueue

l1 = TestDQueue()

class DQueue:
    try:
        print("Enter the String :")
        str2 = input()  # read string from user
        str2.strip()
        while str2.isdigit() or len(str2) <= 0:
            print("Please Provide Input as String")
            str2 = input()
        str1 = re.sub('[^A-Za-z]', '', str2)
        for i in range(len(str1)):
            l1.enQueueRear(str1[i])    # push front one one character in DQueue
            print()
        print()
        print("Removing Elements From Rear:")
        str2 = ""
        for i in range(len(str1)):
            str2 = str2 + l1.removeFromFront()   # remove from Rear one one by character from DQueue

        if str2.upper() == str1.upper():    # check string is Palindrome or not
            print("String is palindrome")
        else:
            print("Not Palindrome")

    except ValueError:
        print("----------------------Oops Something Went Wrong----------------------")

