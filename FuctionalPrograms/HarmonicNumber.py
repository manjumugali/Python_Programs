"""
******************************************************************************
* Purpose:  To Print Nth harmonic number
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class HarmonicNumber:
    try:
        print("Enter The Harmonic Value")
        n = int(input())    # Reading input
        while n == 0:   # Validating n might not be  Negative Value
            n = int(input("Please Provide Valid Value\n"))

        c1.harmonicNumbers(n)   # Invoking function it takes One arguments As Integer

    except RuntimeError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")
