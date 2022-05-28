from .node import Node

class ListDEC:

    def __init__(self):
        self.head = None
        self.last = None

    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def addtostart(self,data):
        if self.empty():
            self.head = self.last = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head.previous = temp
            self.head = temp
        self.__unite_node()
        self.count = +1

    def addtoend(self,data):
        if self.empty():
            self.head = self.last =Node(data)
        else:
            temp = self.last
            self.last = temp.next = Node(data)
            self.last.previous = temp
        self.__unite_node()
        self.count = +1

    def __unite_node(self):
        self.head.previous = self.last
        self.last.next = self.head