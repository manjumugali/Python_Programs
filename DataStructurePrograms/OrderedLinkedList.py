"""
******************************************************************************
* Purpose: Program To Implement OrderedLinkedList.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   19-01-2019
*
******************************************************************************
"""
from Utility_DataStructure.DataStructureOperations import LinkedList

l1 = LinkedList()


class OrderedLinkedList:
    try:
        newfile = open("numbers", "r+")  # File IO open() function to Opens the file with read mode
        number = newfile.readline()  # reading file data and it converts to single String
        num = number.split()  # It splits the Given String Sentence into Words(by Space)
        my_list = []
        newfile.close()  # close the file
        print("****************************After Reading From The File:*************************************\n ")
        for i in num:
            print(i, end=" ",)
        print()

        print("*******************************Ordered Linked List Elements********************************** \n")
        for i in num:
            my_list.append(int(i))
        for i in my_list:
            s1 = l1.orderedAdd(i)  # Invoking add Method to add element to linked list

        l1.display()  # Invoking display() Method to print element of linked list
        print()
        print()
        print("***************************Enter The Number To Search******************************************\n")
        num5 = input()  # reading Number to search in LinkedList
        while not num5.isdigit():
            print("Enter only Number")
            num5 = input()
        num1 = int(num5)
        res = l1.search(num1)  # Invoking search() Method to search element in linked list

        if res is True:  # if element present in linked list  else not present
            result = l1.remove(num1)  # Invoking remove() Method to remove element from linked list
        else:
            l1.orderedAdd(num1)  # Invoking add Method to add element to linked list
            print()
            print(num1, "Its Added To Linked List \n")

        print("***************************Updated Linked list Is ***************************")
        nums1 = l1.display()  # Invoking display() Method to print element of linked list
        print()

        newfile = open("numbers", "r+")  # open file in read and write mode
        newfile.truncate(0)  # file IO truncate() method to remove all tha data from file
        newfile.close()  # close file

        newfile = open("numbers", "r+")  # open file in read and write mode
        for nums in nums1:
            num2 = str(nums) + " "
            newfile.write(num2)  # file IO write() to write data into file
        newfile.close()  # close file

        my_list.clear()
    except FileNotFoundError:
        print("-------------------------Oops Something Went Wrong Went--------------------------")
