from . node import Node
from model.student import Student
import random

class ListSE_circule:
    def __init__(self):
        self.head = None

    def numero_aleatorio(self):
        contador=0
        for x in range(1):
            print(random.randint(1, 101))
            temp = self.head
            while temp != None:
                if contador == x:
                    return temp.data
                temp = temp.next
                contador= contador+1


    #Adicionar
    def add_to_last(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            #Posicionado en la ultima posicion
            temp.next = Node(data)

            #Coger la cabeza
            temp.next.next = self.head

    #Adicionar al inicio en circular
    def add_to_star(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            # Posicionado en la ultima posicion
            temp.next = Node(data)
            # Coger la cabeza
            temp.next.next = self.head
            #El dato que trae se convierte en la cabeza
            self.head = temp.next

#Listar
    def listar (self):
        list_student_circule = []
        temp = self.head
        list_cp=ListSE_circule
        cont = 0
        if self.head != None:
            temp = self.head
            while temp.next != self.head:
                list_student_circule.append(temp.data)
                temp= temp.next
                cont=cont+1
                list_student_circule.append(temp.data)
        return cont
