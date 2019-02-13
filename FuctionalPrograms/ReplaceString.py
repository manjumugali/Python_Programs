"""
******************************************************************************
* Purpose:  To Replace Username
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest

c1 = UtilityTest.TestFunctional()


class StringReplace:
    try:
        print("Enter The Username :")
        name = input()  # Reading input

        while len(name) <= 3 or name.isdigit():  # Validating Name might not be less < 3 and not Digits
            name = input("Please Provide Valid Name\n")

        c1.replaceUsername(name)    # Invoking function it takes One arguments As String

    except RuntimeError:
        print("oops Something Went Wrong")
