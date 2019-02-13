"""
******************************************************************************
* Purpose:  To Calculate Euclidean distance from the point (x, y) to the origin (0, 0).
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class Distance:
    try:
        print("Enter The value of X :")
        x = float(input())  # Reading X
        print("Enter The value of Y :")
        y = float(input())  # Reading Y

        while x < 0.0:  # Validating X might not be  Negative Value
            x = float(input("Please Provide valid Input X"))

        while y < 0.0:  # Validating Y might not be  Negative Value
            y = float(input("Please Provide valid Input Y"))

        obj.findEuclideanDistance(x, y)     # Invoking function it takes Two arguments As Float
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Float Values........")
