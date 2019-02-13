"""
******************************************************************************
* Purpose: Program To Implement Stack to print cal of month.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   21-01-2019
*
*******************************************************************************
"""
from Utility.UtilityTest import TestFunctional
from Utility_DataStructure.DataStructureOperations import LinkedList

l1 = LinkedList()
l2 = LinkedList()


class StackCal:
    try:
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]  # storing months
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # storing days of the each month
        weeks = ["Sun", "Mon", "Tue", "Wen", "Thur", "Fri", "Sat"]
        print("Enter the Value of the Month:")
        m = input()  # read month value
        while not m.isdigit() or int(m) > 12:  # validating month
            print("Please Provide Valida input for month")
            m = input()
        print("Enter the Value of Year")
        year = input()  # read year value
        while not year.isdigit() or int(year) < 999:  # validating year
            print("Please Provide Valid Input")
            year = input()
        month = int(m)
        if month == 2 and TestFunctional.TestLeapYear_OR_NotLeapYear(int(year)):  # check its leap year
            days[month] = 29

        day = TestFunctional.dayOfTheWeek(month, 1, int(year))  # get day of the week
        weeks.reverse()
        for i in range(len(weeks)):
            l1.sPush(weeks[i])  # invoking push method to add weeks
        res = days[month-1]
        for i in range(res, 0, -1):
            l2.sPush(i)  # invoking push method to add dates
        print()
        print("      ", months[month - 1], "-", year)
        print("---------------------------")
        for i in range(1, 8):
            print(l1.sPop(), end=" ")       # invoking pop method to remove elements
        print()
        for i in range(day * 4):     # to print number of space to get particular day
            print(end=" ")

        for i in range(1, res + 1):
            if i <= 5:
                print("", l2.sPop(), " ", end="")   # invoking pop method to remove elements
            if 5 < i < 10:
                print("", l2.sPop(), " ", end="")   # invoking pop method to remove elements
            if i > 9:
                print("", l2.sPop(), "", end="")    # invoking pop method to remove elements

            if (i + day) % 7 == 0:  # after 7 col print next line
                print()
    except ValueError:
        print(".....................oops Something Went Wrong..........................")