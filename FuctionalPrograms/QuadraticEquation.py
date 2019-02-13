"""
******************************************************************************
* Purpose:  To Find the roots of the equation a*x*x + b*x + c.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   13-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class Quadratic:
    try:
        print("Enter The Value Of a :")
        a = int(input())    # Reading input a
        print("Enter The Value Of b :")
        b = int(input())    # Reading input b
        print("Enter The value Of c :")
        c = int(input())    # Reading input c

        c1.findRoots(a, b, c)   # Invoking function it takes Three arguments As Integer

    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")