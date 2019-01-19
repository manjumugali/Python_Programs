"""
******************************************************************************
* Purpose: It Contains All The Linked List Implementation Methods.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   18-01-2019
*
******************************************************************************
"""

from DataStructurePrograms.Node import Node


class LinkedList:

    def __init__(self):

        self.first = None
        self.last = None
        self.size = 0

    '''**************************************************************************************************************'''
    '''------------------------------Function To add() Method Implementation-----------------------------------------'''

    def add(self, data):  # it takes data as parameter
        n = Node(data)  # creating Node class object and passing data
        if self.size == 0:  # if size == 0 Add node at 1 position
            self.first = n
            self.last = n
        else:  # if size !=0 then add it to next
            self.last.next = n
            self.last = n
        self.size += 1  # incrementing size value

    '''**************************************************************************************************************'''
    '''------------------------------Function To search() Method Implementation--------------------------------------'''

    def search(self, item):  # it takes data as parameter
        temp = self.first  # temp variable to hold first node
        res = None
        while temp is not None:
            if temp.data == item:  # check first node data == item if true set True else False
                res = True
                break
            else:
                res = False
            temp = temp.next  # temp is point to temp.next Node
        if res is True:  # if Element is present print msg else not found
            print("*******************************Element Found :", item, "*********************\n")
            return True
        else:
            print()
            print("**********************Element Is Not Found***********************************")
        return False

    '''**************************************************************************************************************'''
    '''------------------------------Function To isEmpty() Method Implementation-------------------------------------'''

    def isEmpty(self):
        if self.size == 0:  # size == 0 empty list else there are elements
            print("List is Empty")
        else:
            print("List Is Not Empty")

    '''**************************************************************************************************************'''
    '''------------------------------Function To sizeOfList() Method Implementation----------------------------------'''

    def sizeOfList(self):  # print size of the list
        print("Size Of The List is", self.size)

    '''**************************************************************************************************************'''
    '''------------------------------Function To display() Method Implementation-------------------------------------'''

    def display(self):  # to print elements from List
        my_list= []
        temp = self.first  # temp is pointing to first
        while temp is not None:  # it loops util temp == Null
            print(temp.data, "->", end=" ")
            my_list.append(temp.data)
            temp = temp.next
        return my_list

    '''**************************************************************************************************************'''
    '''------------------------------Function To index() Method Implementation---------------------------------------'''

    def index(self, item):  # it takes item as Parameter
        temp = self.first  # temp is pointing to first
        res = True
        pos = 0  # initialise position = 0
        for i in range(self.size):  # it loops until i reach to size
            if temp.data == item:  # if temp == item then element found set pos = i else temp points next Node
                pos = i
                res = True
                break
            else:
                res = False
            temp = temp.next

        if res is True:  # if its True print the Position of item else not found
            print("*--------------------------------------------------*")
            print("Position Of Given Element '", item, "' is :", pos)
        else:
            print("*--------------------------------------------------*")
            print("Given Element is Not In List:")

    '''**************************************************************************************************************'''
    '''------------------------------Function To remove() Method Implementation--------------------------------------'''

    def remove(self, item):  # it takes item as parameter
        temp = self.first  # temp is pointing to first
        prev = None  # prev is pointing to Null
        if temp.data == item:  # if element is found at 1st position only then return true else loop over until null
            self.first = temp.next  # first = temp.next
            temp.next = self.first  # temp.next = first
            self.size -= 1
            return True
        else:
            while temp:  # it loops util temp == Null
                if temp.data == item:  # check first node data == item if true set True else temp points to next node
                    prev.next = temp.next
                    temp.next = None
                    return True
                    break
                else:
                    prev = temp
                    temp = temp.next
            self.size -= 1  # Decrement Size value

    '''**************************************************************************************************************'''
    '''------------------------------Function To insert() Method Implementation--------------------------------------'''

    def insert(self, data, pos):  # it takes two parameter as data and position
        prev = None  # prev is pointing to Null
        temp = self.first  # temp is pointing to first
        new_node = Node(data)  # creating Node class object and passing data

        if pos > 0 or pos < self.size:  # if pos > 0 and < size then insert node in between two nodes
            for i in range(0, self.size):
                if i == pos:  # if pos==i then we got position
                    self.size += 1  # increment size value
                    new_node.next = temp  # set new node to temp
                    prev.next = new_node  # prev to new node
                    break
                else:  # else point temp and prev to next node
                    prev = temp  # prev = temp
                    temp = temp.next  # temp = temp.next

    '''**************************************************************************************************************'''
    '''----------------------Function To add() Method Implementation of Ordered LinkedList---------------------------'''

    def orderedAdd(self, data):  # it takes Data as parameter
        node = Node(data)  # creating Node class object and passing data
        temp = self.first   # temp is pointing to first
        if self.size == 0:  # if size == 0 Add node at 1 position
            self.first = node
            self.last = node
        else:  # if size !=0 then add it to next
            while temp is not None:     # it loops util temp == Null
                if temp.data > data:    # if temp.data > data use bubble sort technique to swap it
                    d1 = node.data
                    node.data = temp.data
                    temp.data = d1

                temp = temp.next
            self.last.next = node
            self.last = node

        self.size += 1      # increment size value


s1 = LinkedList()
