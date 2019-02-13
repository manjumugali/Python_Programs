"""
******************************************************************************
* Purpose:  Program to Question to find your number,Use Binary Search to find the number
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   16-01-2019
*
******************************************************************************
"""
from Utility import UtilityTest
obj = UtilityTest.TestFunctional()

class Binary:
    try:
        print("Enter The Number :")
        num = int(input())  # Reading Input as Integer

        while num <= 0:  # Validating n > 1 might not be  Negative Value
            num = int(input("Please Provide Valid Value\n"))

        res = obj.covertDecimalToBinary(num)  # Invoking function it takes One arguments As number
        var = int(res)
        len = len(res)
        len1 = len // 2
        str1 = res[0:len1]
        str2 = res[len1:len]
        str3 = str2 + str1
        print("Decimal To Binary", str3)
        print("***********************************************")
        print("Before Swapping  : ", str3)
        print("After Swapping  :", var)
        res1 = obj.binaryToDecimal(var)    # Invoking function it takes One arguments As number
        print("Binary To Decimal", res1)
        flag = obj.isPowerOf2(res1)
        if flag:  # if flag Set to True Means It's Power Of 2
            print(res1, "is Power Of 2 Yes")
        else:
            print(res1, "is Power Of 2 No")
    except RuntimeError:
        print(".....................oops Something Went Wrong.........")