"""
******************************************************************************
* Purpose:  Program To Print 2D array in Matrix format
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   13-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class TwoDimensionalArray:
    try:
        print("number of rows :")
        row = int(input())    # Reading input for row
        print("number of columns :")
        col = int(input())    # Reading input for col

        while row < 0:    # Validating row might not be less < 0
            m = int(input("Please Provide +ve Row size\n"))

        while col < 0:    # Validating col might not be less < 0
            n = int(input("Please Provide +ve Cols size"))

        array = row * col   # how many elements array holds
        print("Enter the Array ", array, " Elements")
        matrix = []     # Empty Array list to Store Array Elements

        for i in range(row):     # it loops until to reach to row value
            row_list = []   # Temporary array to store row Elements
            for j in range(col):     # it loops until to reach to col value
                row_list.append(int(input()))   # adding Array Elements to list
            matrix.append(row_list)  # adding row elements to matrix Array list

        obj.printMatrixArray(matrix, row, col)  # Invoking function it takes Three arguments As list and 2 Integer

    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values.......")
