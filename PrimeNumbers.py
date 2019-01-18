"""
******************************************************************************
* Purpose:  To Find How many Prime Numbers in the range(0-1000) and How many Anagram Numbers and Palindrome
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   15-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
c1 = UtilityTest.TestFunctional()

class PrimeNumber:
    try:
        print("Enter The Range :")
        n = int(input())  # Reading Size(Range)

        while n < 0:    # Validating Size might not be  Negative Value
            print("Please Enter Positive Number Only")
            n = int(input())

        my_list = c1.PrimeNumbers(n)    # Invoking function it takes One arguments As Integer
        my_list1 = c1.anagramPrime(my_list)    # Invoking function it takes One arguments As list
        print("...................List Of All Prime's Palindrome Numbers................")
        for i in range(len(my_list)):    # it loops until to reach to list size
            temp = int(my_list[i])
            res = c1.palindrome(temp)      # Invoking function it takes One arguments As Integer   
            if res is not None:       # if res is None it should not entire into loop
                print(temp, res)

    except ValueError:
        print("....................oops Something Went Wrong......... Please Provide Only Integer Values........")
