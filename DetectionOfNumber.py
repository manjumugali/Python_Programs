"""
******************************************************************************
* Purpose:  Program to Question to find your number,Use Binary Search to find the number
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   17-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
obj = UtilityTest.TestFunctional()

class QuestionToFindYourNumber:
    try:
        my_list = []    # Empty Array
        print("Enter the N value")
        num = int(input())  # Reading input

        while num < 0:   # Validating num > 1 might not be  Negative Value
            print("Please Provide Positive Number(only)")
            num = int(input())

        for i in range(1, pow(2, num-1)):
            my_list.append(i)
        print("think of a number between 0 and ", len(my_list)-1)
        print(my_list)
        low = 0     # Initialise low value
        high = len(my_list)-1   # Initialise high value
        obj.guessNumber(my_list, low, high)     # Invoking function it takes 3 arguments As array,Number

    except RuntimeError:
        print(".....................oops Something Went Wrong.........")


