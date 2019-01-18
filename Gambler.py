"""
******************************************************************************
* Purpose:  To Find Number of Wins and Percentage of Win and Loss(Gambler)
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class Gambler:
    try:
        print("Enter The Amount To play :")
        stake = int(input())    # Reading Input
        print("Enter The Target Goal amount :")
        goal = int(input())     # Reading Input
        print("Enter value to play No of times")
        no = int(input())       # Reading Input

        while stake < 0:    # Validating Stake might not be  Negative Value
            stake = int(input("Please Provide Positive Amount to play game\n"))

        while goal < 0:     # Validating Goal might not be  Negative Value
            goal = int(input("Please provide Positive target to win the Game\n"))

        while no < 0:   # Validating Number might not be  Negative Value
            no = int(input("Please provide valid Input\n "))

        obj.getReadyToPlayGame(stake, goal, no)     # Invoking function it takes three arguments as Integers
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")