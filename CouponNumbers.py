"""
******************************************************************************
* Purpose:  To count the No of times Random method is Called to generate five distinct coupon
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class Coupon:
    try:
        print("Enter Distinct Coupon Number :")
        n = int(input())  # Reading Integer number

        while n < 0:    
            n = int(input("Please Provide Positive Number"))

        obj.generateCouponNumbers(n)    # Invoking function it takes One arguments As Integer
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")