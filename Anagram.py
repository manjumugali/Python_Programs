"""
******************************************************************************
* Purpose:  To Check Two String Are Anagram Or Not
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   14-01-2019
*
******************************************************************************
"""
import re

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class Anagram:
    try:
        print("Enter The First String :")
        str1 = input()  # Read First String
        onlystr = re.sub('[^A-Za-z]+', '', str1)  # Remove The All Special Characters using RegularEx

        print("Enter The Second String :")
        str2 = input()  # Read Second String
        onlystr1 = re.sub('[^A-Za-z]+', '', str2)  # Remove The All Special Characters

        c1.checkTwoStringsAnagram(str1, str2)   # Invoking function it takes Two arguments As String

    except ValueError:
        print("...........oops Something Went Wrong.........")
