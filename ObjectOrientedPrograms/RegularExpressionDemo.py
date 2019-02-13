"""
******************************************************************************
* Purpose:  Program To Demonstration Regular Expression
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   27-01-2019
*
******************************************************************************
"""
import datetime
import re
from OOPS_Utility.Test_Oops_Utility import RegularExp


class RegularExpression:
    try:
        print("Enter the user name")
        name = str(input()).title()  # read input as name

        while not name.isalpha() or len(name) <= 0:  # validating name
            print("Please Provide Valid User name:")
            name = str(input())
        print("Enter the full Name")
        last_name = input().title()  # read input as full name
        while not last_name.isalpha() or len(last_name) <= 0:  # validating full name
            print("Please Provide Valid full name:")
            last_name = input()

        print("Enter the Contact Number in this Format(91-XXXXXXXXXX)")
        p_num = input()  # read input as mob_no

        while not re.match("(91-)[7-9][0-9]{9}", p_num) or len(p_num) > 13:  # validating mob_no using regex match()
            print("Please Provide Valid Phone-Number(91-XXXXXXXXXX)")
            p_num = input()

        date = datetime.date.today().strftime("%d/%m/%Y")  # generating current date in format(dd/mm/yyyy)
        r1 = RegularExp(name, last_name, p_num,
                        date)  # creating RegularExpression class object and passing passing parameters
        r1.useOfRegex()  # invoking useOfRegex() function on r1 object
    except RuntimeError:
        print("-----------Program Crash--------------")


if __name__ == "__main__":
    RegularExpression()
