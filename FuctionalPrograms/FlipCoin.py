"""
******************************************************************************
* Purpose:  To Find Percentage of Head vs Tails
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class FlipCoin:
    try:
        print("Enter The number of times to Flip Coin :")
        n = int(input())    # Reading Number
        while n < 0:     # Validating N might not be  Negative Value
            n = input("Please Provide Valid Input(Positive Number)\n")

        c1.percentageOfHead_Vs_Tails(n)     # Invoking function it takes One arguments As Integer

    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")
