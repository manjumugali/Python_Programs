"""
******************************************************************************
* Purpose:  Program To Temperature Conversion
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   17-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class TemperatureConversion:
    try:
        print("Enter Your Choice :\n1 - Fahrenheit\n2 - Celsius")
        choice = int(input())

        while choice <= 0:  # Validating num > 1 might not be  Negative Value
            choice = int(input("Please Provide Valid Value\n"))

        c1.temperatureConversion(choice)
    except ValueError:
        print("...........oops Something Went Wrong.........")