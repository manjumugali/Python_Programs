"""
******************************************************************************
* Purpose:  To Find Whether The Year Is Leap Year Or Not
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class LeapYear:
    try:
        print("Enter value for the Year:")
        year = int(input())     # Reading input

        while year < 999:    # Validating Year might not be less < 999
            year = int(input("Enter value for the Year\n"))

        c1.TestLeapYear_OR_NotLeapYear(year)    # Invoking function it takes One arguments As Integer
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")

