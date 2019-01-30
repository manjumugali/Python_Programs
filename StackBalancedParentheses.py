"""
******************************************************************************
* Purpose: Program To Implement Stack for Simple Balanced Parentheses.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   20-01-2019
*
*******************************************************************************
"""
from Utility_DataStructure.DataStructureOperations import LinkedList

l1 = LinkedList()


class Stack:
    try:
        print("Enter Arithmetic Expression to check balanced or not: ")
        exp = input()  # read Expression from user
        exp.strip()
        while len(exp) <= 0:
            print("Please Enter Arithmetic Expression")
            exp = input()
        var = len(exp)
        if exp[0] == '}' or exp[0] == ')' or exp[0] == ']':
            print("Arithmetic Expression is Not Balanced")
        else:
            result = True
            st1 = []
            for i in range(len(exp)):
                if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':  # if exp[i] == (,{,[ push it
                    st1 = l1.push(exp[i])

                elif exp[i] == ')':  # if exp[i]== ) pop it
                    res = l1.pop()
                    if res != '(':
                        result = False
                elif exp[i] == '}':     # if exp[i]== } pop it
                    res = l1.pop()
                    if res != '{':
                        result = False

                elif exp[i] == ']':     # if exp[i]== ] pop it
                    res = l1.pop()
                    if res != '[':
                        result = False

            if '(' not in st1 and '{' not in st1 and '[' not in st1:
                if result is True:
                    print("Arithmetic Expression is Balanced")
                else:
                    print("Arithmetic Expression is Not Balanced")
            else:
                print("Arithmetic Expression is Not Balanced")

    except ValueError:
        print("-------------------------Oops Something Went Wrong Went--------------------------")
