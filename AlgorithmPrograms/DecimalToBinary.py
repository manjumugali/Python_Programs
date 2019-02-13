"""
******************************************************************************
* Purpose:  To Convert Decimal To Binary
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   15-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()

class DecimalToBinary:
    try:
        print("Enter The Number:")
        n = int(input())    # Read Number
        while n <= 0:       # Validating n > 1 might not be  Negative Value
            n = int(input("Please Provide Valid Value\n"))

        res = c1.covertDecimalToBinary(n)     # Invoking function it takes One arguments As number
        print("Decimal To Binary: ", res)
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")
