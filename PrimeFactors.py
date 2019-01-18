"""
******************************************************************************
* Purpose:  Computes the prime factorization of N
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   13-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class PrimeFactors:
    try:
        print("Enter Number to find the prime factors :")
        n = int(input())    # Reading input

        while n < 0:    # # Validating N might not be less < 0 (Negative Number)
            n = int(input("Please Provide Positive Number\n"))

        obj.findPrimeFactors(n)     # Invoking function it takes One arguments As Integer

    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")