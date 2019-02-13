"""
******************************************************************************
* Purpose:  Write a program To find WindChill and print the result
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   13-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class WindChill:
    try:
        print("Enter The Air Temperature :")
        t = int(input())    # Reading input for temperature
        while t > 50:   # Validating temperature might not be > 50
            t = int(input("Enter The Air Temperature Value Less Than 50 "))

        print("Enter The Wind Speed value: ")
        v = int(input())    # Reading input for speed
        while v > 130 or v < 3:     # Validating Speed might not be less < 3 and > 130
            v = int(input("Enter The Wind Speed value grater than 3 and less than 130"))

        c1.resultOfWindChill(t, v)  # Invoking function it takes Two arguments As Integer

    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")