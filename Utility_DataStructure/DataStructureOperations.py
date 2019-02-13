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
from Utility.UtilityTest import TestFunctional
from DataStructurePrograms.Node import Node


class LinkedList:

    def __init__(self):

        self.first = None
        self.last = None
        self.size = 0
        self.top = None
        self.front = None
        self.rear = None

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
        my_list = []
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
        temp = self.first  # temp is pointing to first
        if self.size == 0:  # if size == 0 Add node at 1 position
            self.first = node
            self.last = node
        else:  # if size !=0 then add it to next
            while temp is not None:  # it loops util temp == Null
                if temp.data > data:  # if temp.data > data use bubble sort technique to swap it
                    d1 = node.data
                    node.data = temp.data
                    temp.data = d1

                temp = temp.next
            self.last.next = node
            self.last = node

        self.size += 1  # increment size value

    '''**************************************************************************************************************'''

    '''------------------------------Stack Implementation------------------------------------------------------------'''

    '''----------------------Function To push() Method Implementation of stack---------------------------------------'''

    my_list = []
    cap = -1
    head = -1

    def push(self, exp):  # it takes item as parameter
        if self.head == self.cap:  # if top == cap then push the elements
            self.head += 1  # increment top by 1
            self.my_list.append(exp)  # add the element to array
            self.cap += 1  # increment size by 1
        return self.my_list

    '''**************************************************************************************************************'''
    '''-------------------------------Function To pop() method Implementation ---------------------------------------'''
    x = 0

    def pop(self):
        if self.head != -1:  # if top != -1 remove elements from stack
            self.x = self.my_list[self.head]
            self.my_list.remove(self.my_list[self.head])
            self.head -= 1  # decrement top by 1
            self.cap -= 1  # decrement size by 1
            return self.x

    '''**************************************************************************************************************'''
    '''-------------------------------Function To size of the stack--------------------------------------------------'''

    def stackSize(self):
        print("Size Of Stack is : ", self.cap)

    '''**************************************************************************************************************'''
    '''-------------------------------Function To check Stack is Empty-----------------------------------------------'''

    def stackIsEmpty(self):
        if self.cap == 0:  # if size == 0 stack is empty else there are elements in stack
            print("Stack Is Empty")
        else:
            print("Stack Is Not Empty")

    '''**************************************************************************************************************'''
    '''-------------------------------Function To check peek element-----------------------------------------------'''

    def peek(self):
        if self.head != -1:
            print("Top item in Stack is:", self.my_list[len(self.my_list) - 1])

    '''**************************************************************************************************************'''
    '''-------------------------------------------Queue Implementation-----------------------------------------------'''
    f = -1
    r = -1
    qsize = 3
    my_list1 = []
    ava_amount = 1000
    str1 = ''
    '''-----------------------------------------Function To Push Element in Queue------------------------------------'''

    def qPush(self, amount):  # it takes amount as parameter
        if self.f == -1:
            self.f += 1
            self.r += 1
            self.my_list1.append(amount)
            self.qsize -= 1
            self.ava_amount += amount
            return self.ava_amount
        else:
            if self.qsize != 0:
                self.r += 1
                print(self.r)
                self.my_list1.append(amount)
                self.qsize -= 1
                self.ava_amount += amount
                return self.ava_amount
            else:
                print("..................Queue is Full..............")
                return self.ava_amount

    '''**************************************************************************************************************'''
    '''-----------------------------Function To pop the Elements From queue------------------------------------------'''

    def qPop(self):
        if self.qsize == 0:  # if size != 0
            self.rear -= 1  # decrement rear by 1
            self.qsize += 1  # decrement size by 1
            for i in range(len(self.my_list1)):
                self.my_list1.remove(self.my_list1[i])  # remove element from queue
                break
        for i in self.my_list1:
            print(i, end="->")
        print()
        return self.my_list1

    '''**************************************************************************************************************'''
    '''-----------------------------Function To Print calendar of the month------------------------------------------'''
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]  # storing months
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # storing days of the each month

    def printCalOfMonth(self, month, year):  # it takes 2 parameters

        if month == 2 and TestFunctional.TestLeapYear_OR_NotLeapYear(year):  # check its leap year
            self.days[month - 1] = 29

        day = TestFunctional.dayOfTheWeek(month, 1, year)  # to get day of the month
        print("          ", self.months[month - 1], "  ", year)  # to print month and year
        print("Sun   Mon   Tue   Wed   Thur   Frd   Sat")  # to print weeks
        var = self.days[month - 1]
        for i in range(day * 5):
            print(end=" ")

        for i in range(1, var + 1):  # to get month dates
            if i <= 5:
                print("  ", i, " ", end="")
            if 5 < i < 10:
                print(" ", i, "  ", end="")
            if i > 9:
                print("", i, "  ", end="")

            if (i + day) % 7 == 0:  # after 7 col print next line
                print()

    '''**************************************************************************************************************'''
    '''-----------------------------Function To Print Prime Numbers in 2D Array ------------------------------------'''
    prime_list = []

    def printPrimeNu2D(self, number):  # it takes 1 parameters as Integer
        p_list = []
        self.prime_list = TestFunctional.PrimeNumbers(number)  # get all the Prime Numbers
        print("Print All Prime Numbers In 2-D array:")
        for i in self.prime_list:
            p_list.append(int(i))
        row = 10  # initialise row value
        col = 25  # initialise col value
        matrix = [[0 for j in range(col)] for i in range(row)]  # Creating 2-D Array
        limit = 100  # initialise limit value
        k = 0  # initialise k value to 0
        for i in range(row):  # it loops until row value
            for j in range(col):  # it loops until row value
                if k < len(p_list):  # if k < length of the array list enters loop
                    if p_list[k] <= limit:  # k should be <= limit value
                        matrix[i][j] = p_list[k]  # store it into matrix array
                        k += 1  # increment k value by 1
            limit += 100  # increment limit value by 1
        var = 0
        var1 = 100
        for i in range(row):  # it executes until i reach to row value
            print("[", var, "-", var1, "]", end=" -> ")
            for j in range(col):  # it executes until j reach to col value
                if matrix[i][j] != 0:
                    print(matrix[i][j], end=" ")  # to print matrix format
            print()
            var = var + 100
            var1 = var1 + 100

    '''**************************************************************************************************************'''
    '''----------------------Function To Print anagram prime numbers in 2-D array------------------------------------'''

    @staticmethod
    def printAnagramPrimeNumbers(number):
        pm_list = TestFunctional.PrimeNumbers(number)  # get all the prime numbers
        an_list = TestFunctional.anagramPrime(pm_list)  # get all anagram prime numbers
        print("-------------------------------Print All Anagram Prime Numbers In 2-D array:(0-1000)-----------------\n")
        an_list1 = []
        for i in an_list:
            an_list1.append(int(i))
        row = 10  # initialise row value
        col = 100  # initialise col value
        matrix = [[0 for j in range(col)] for i in range(row)]  # Creating 2-D Array
        limit = 100
        k = 0
        for i in range(row):
            for j in range(col):
                if k < len(an_list1):  # k should be <= limit value
                    if an_list1[k] <= limit:
                        matrix[i][j] = an_list1[k]  # store it into matrix array
                        k += 1
            limit += 100
        var = 0
        var1 = 100
        for i in range(row):  # it executes until i reach to row value
            print("[", var, "-", var1, "]", end="->")
            for j in range(col):  # it executes until j reach to col value
                if matrix[i][j] != 0:
                    print(matrix[i][j], end=" ")  # to print matrix format
            print()
            var = var + 100
            var1 = var1 + 100

        print("-------------------------Print All Not Anagram Prime Numbers In 2-D array:(0-1000)------------------\n")
        pm_list1 = []
        for i in pm_list:
            pm_list1.append(int(i))
        for i in an_list1:
            if i in pm_list1:
                pm_list1.remove(i)  # removing anagram prime numbers From prime Numbers

        matrix1 = [[0 for j in range(col)] for i in range(row)]  # Creating 2-D Array
        limit1 = 100
        k1 = 0
        for i in range(row):
            for j in range(col):
                if k1 < len(pm_list1):  # k should be <= limit value
                    if pm_list1[k1] <= limit1:
                        matrix1[i][j] = pm_list1[k1]  # store it into matrix array
                        k1 += 1
            limit1 += 100

        var = 0
        var1 = 100
        for i in range(row):  # it executes until i reach to row value
            print("[", var, "-", var1, "]", end="->")
            for j in range(col):  # it executes until j reach to col value
                if matrix1[i][j] != 0:
                    print(matrix1[i][j], end=" ")  # to print matrix format
            print()
            var = var + 100
            var1 = var1 + 100

    '''**************************************************************************************************************'''
    '''----------------------Stack Implementation To Print Prime Numbers Using Linked List---------------------------'''

    '''----------------------Function To push() Method Implementation of stack---------------------------------------'''

    def sPush(self, data):  # it takes 1 parameter
        node = Node(data)

        if self.top is None:  # if is -1 push node else increment top value then push it
            self.top = node
        else:
            node.next = self.top
            self.top = node  # assign node to top
        self.size += 1  # increment size

    '''----------------------Function To pop() Method Implementation of stack---------------------------------------'''

    def sPop(self):
        if self.top is None:  # if top=-1 stack is empty
            print("Stack is Empty")
        temp = self.top  # temp holds top node
        self.top = self.top.next  # assign top.next to top
        self.size -= 1  # decrement size by 1
        return temp.data  # return removed item

    '''----------------------Function To print() Method Implementation of stack---------------------------------------'''

    def sDisplay(self):
        temp = self.top  # temp is pointing to first
        while temp is not None:  # it loops util temp == Null
            print(temp.data, "->", end="")
            temp = temp.next  # each time temp pointing to temp.next

    '''**************************************************************************************************************'''
    '''----------------------Queue Implementation To Print Prime Numbers Using Linked List---------------------------'''

    '''----------------------Function To add() Method Implementation of Queue---------------------------------------'''

    def enQueue(self, data):  # it takes 1 parameter
        node = Node(data)
        if self.rear is None:  # if rear == None assign front and rear to node
            self.front = node
            self.rear = node
        else:  # else increment Rear value
            self.rear.next = node
            self.rear = self.rear.next
        self.size += 1

    '''----------------------Function To remove() Method Implementation of Queue---------------------------------------'''

    def deQueue(self):
        if self.front is not None:  # if front != null remove front node from Queue else queue is empty
            temp = self.front
            self.front = self.front.next  # assign front.next to front
            self.size -= 1
            return temp.data
        else:
            if self.rear is not None:  # rear != null assign to null
                self.rear = None
            print("Queue Is Empty:")

    '''----------------------Function To print() Method Implementation of stack---------------------------------------'''

    def print_dQueue(self):
        temp = self.front
        while temp:  # it loops until temp != null
            print(temp.data, end=" -> ")
            temp = temp.next  # increment temp

    '''**************************************************************************************************************'''
    '''--------------------- Binary Search To Print Prime Numbers---------------------------------------------'''

    @staticmethod
    def BinaryTree(number):  # it takes 1 parameter as integer
        fact = 1  # initialise fact=1
        for i in range(1, number + 1):  # loop over numbers
            fact = fact * i  # multiply fact*i
        return fact  # return fact

    '''**************************************************************************************************************'''
    '''--------------------- Binary Search To Print Prime Numbers----------------------------------------------------'''

    @staticmethod
    def hash_Function(key, size):
        index = key % size
        return index


s1 = LinkedList()
