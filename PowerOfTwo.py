"""
******************************************************************************
* Purpose:  Print The Power Value N.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class PowerOfTwo:
    try:
        print("Enter The Power value :")
        n = int(input())    # Reading Input

        while n < 0 or n >= 32:     # Validating N might not be less < 0 and n > 32
            n = int(input("Please Provide Valid Input\n"))

        obj.printPowerOf2(n)    # Invoking function it takes One arguments As Integer
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")