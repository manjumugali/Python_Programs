"""
******************************************************************************
* Purpose:  Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   13-01-2019
*
******************************************************************************
"""

from Utility import UtilityTest
obj = UtilityTest.TestFunctional()


class StopWatchTimer:
    try:
        print("Enter 1 To Start :")
        choice = int(input())   # Reading input
        while choice != 1:  # Validating choice should be 1
            choice = int(input("Please Provide Valid Input(Enter 1 Only)\n"))

        start = obj.startWatch(choice)  # Invoking function it takes One arguments As Integer
        print("Enter 2 To StopWatch :")
        n = int(input())    # Reading input
        obj.stopWatch(n, start)     # Invoking function it takes Two arguments As Integer
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values.......")