"""
******************************************************************************
* Purpose:  To counts the number of triples that sum to exactly 0.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   13-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()


class Triplets:
    try:
        print("Enter The Array Size :")
        n = int(input())    # Reading input Array Size

        while n < 0:    # Validating n might not be  Negative Value
            n = int(input("Please Provide +ve Number only"))

        arr = list()    # Empty array to Store Array Elements
        print("Enter The Array Elements\n")
        for x in range(n):   # it loops until to reach to array size
            arr.append(int(input()))    # reading Array Elements and Storing it into list

        c1.distinctTriplets(arr)    # Invoking function it takes One arguments As list
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")
