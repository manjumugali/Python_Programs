"""
******************************************************************************
* Purpose:  Program to Calculate Monthly Payment.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   17-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class MonthlyPayment:
    try:
        print("Enter Value For P:")
        p = int(input())    # reading input
        while p <= 0:  # Validating p > 1 might not be  Negative Value
            p = int(input("Please Provide Valid Value(principal loan)\n"))

        print("Enter Value For Y:")
        y = int(input())    # reading input
        while y <= 0:  # Validating y > 1 might not be  Negative Value
            y = int(input("Please Provide Valid Value\n"))

        print("Enter Value For R:")
        r = int(input())    # reading input
        while r <= 0:  # Validating r > 1 might not be  Negative Value
            r = int(input("Please Provide Valid Value(percent interest)\n"))

        obj.monthlyPayment(p, y, r)     # Invoking function it takes 3 arguments As Integer

    except ValueError:
        print("-------Please Provide Valid input(Positive Number)")