"""
******************************************************************************
* Purpose: Program To Implement Node Structure.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   18-01-2019
*
******************************************************************************
"""


class Node:
    try:
        def __init__(self, data):
            self.data = data
            self.next = None

        def getData(self):
            return self.data

        def setData(self, val):
            self.data = val

        def setNext(self, val):
            self.next = val

        def getNext(self):
            return self.next

    except ValueError:
        print("----------------------Oops Something Went Wrong----------------------")
