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
        while 1:
            print("Enter value for the Year:")
            year = input()     # Reading input
            try:
                    if year.isnumeric():
                        print("Invalid Input")
                        year = input()

            except ValueError:
                print("Please provide valida Input")
                continue

        c1.TestLeapYear_OR_NotLeapYear(year)    # Invoking function it takes One arguments As Integer
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")

