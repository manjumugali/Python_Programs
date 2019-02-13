"""
******************************************************************************
* Purpose: It Contains All The DQueue Linked List Implementation Methods.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   23-01-2019
*
******************************************************************************
"""
from DataStructurePrograms.Node import Node


class TestDQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueueRear(self, data):   # it takes 1 parameter as data
        node = Node(data)
        if self.front is None and self.rear is None:
            self.front = node  # if front and rear == None
        else:   #
            node.next = self.front  # add using front
            self.front = node
        print(node.data)

    def enQueueFront(self, data):    # it takes 1 parameter as data
        node = Node(data)

        if self.front is None and self.rear is None:
            self.rear = node    # # if front and rear == None

        else:

            self.rear.next = node  # add using rear
            self.rear = node

    def removeFromFront(self):
        if self.front.next is None:
            temp = self.front
            self.front = None  # if only one element in queue
            return temp.data

        temp = self.front
        self.front = self.front.next  # delete element of queue which is on front
        return temp.data

    def removeFromRear(self):
        traverse = self.front
        if self.rear == self.front:
            self.rear = None  # if queue contains only one element
            self.front = None
            return traverse.data

        while traverse.next is not self.rear:
            traverse = traverse.next  # go till second last position

        rear_value = self.rear
        self.rear = traverse  # delete last element
        traverse.next = None
        return rear_value.data

