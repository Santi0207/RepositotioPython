from . node import Node

class ListSE:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.excisting_identification(data.identification):
                raise Exception("Ya hay un estudiante con ese numero de identificacion")
            temp = self.head
            while temp.next != None:
                temp = temp.next

#Posicionados en el ultimo
            temp.next = Node(data)

    def excisting_identification(self, id):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next

        return False