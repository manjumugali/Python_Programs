"""
******************************************************************************
* Purpose:  Program to compute the square root of a non-negative number.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   17-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
obj = UtilityTest.TestFunctional()

class SquareRoot:
    try:
        print("Enter The Non-Negative Number:")
        num = int(input())

        while num <= 0:  # Validating num > 1 might not be  Negative Value
            num = int(input("Please Provide Valid Value(Positive Number)\n"))
        obj.findSquareRoot(num)
    except ValueError:
        print("-------Please Provide Valid input(Positive Number)")