"""
******************************************************************************
* Purpose:  Program to find day of the week that date falls on.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   17-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
obj = UtilityTest.TestFunctional()

class DayOfWeek:
    try:
        print("Enter Value for Month:")
        m = int(input())    # reading Input

        while m <= 0:  # Validating m > 1 might not be  Negative Value
            m = int(input("Please Provide Valid Value(Month)\n"))

        print("Enter Value for Day:")
        d = int(input())    # reading input
        while d <= 0:  # Validating d > 1 might not be  Negative Value
            d = int(input("Please Provide Valid Value(Day)\n"))

        print("Enter Value for Year:")
        y = int(input())    # reading input
        while y <= 999:  # Validating y > 1 might not be  Negative Value
            y = int(input("Please Provide Valid Value(Year)\n"))
        obj.dayOfTheWeek(m, d, y)    # Invoking function it takes 3 arguments As Integer

    except ValueError:
        print("-------Please Provide Valid input(Positive Number)")