from . node import Node
from model.student import Student


class ListSE:
    def __init__(self):
        self.head = None
        self.count=0

#Adicionar
    def add(self, data: Student):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.excisting_identification(data.identification):
                raise Exception("Ya hay un estudiante con ese numero de identificacion")
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)
# Adicionar al inicio
    def add_to_star(self, data: Student):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

#Validar un estudiante con el mismo id
    def excisting_identification(self, id:str):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next

        return False

#Invertir extremos
    def swap_ends(self):
        temp = self.head
        while temp != None:
            temp.next = temp
        datatemp = self.head.data
        self.head.data = temp.data
        temp.data = datatemp

#Eliminar por dato
    def delete_for_data(self):
        if self.head == None:
            return None
        anterior = self.head
        actual = self.head
        while actual.data.identification != id and actual.next != None:
            anterior = actual
            actual = actual.next
        if actual.data.identification == id:
            if actual is self.head:
                if actual.next != None:
                    self.head = actual.next
                else:
                    self.head = None
            else:
                anterior.next = actual.next
            return actual
        else:
            return None

#Eliminar por posicion
    def delete_for_position(self,p):
        posicion = 1
        if p == 1 and self.head.data != None:
            self.head = self.head.next

        temp = self.head
        while temp.next != None:
            posicion = posicion + 1
            if temp.next.data != None and p == posicion:
                temp.next = temp.next.next
                break;
            temp = temp.next

#Insertar en posicion
    def insert_in_position(self,  position: int, student: Student):
        if position > 0 and position <= (self.count + 1):
            if position == 1:
                new_node = Node(student)
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        new_node = Node(student)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count = +1
                        break
                    temp = temp.next
                    count = +1
                self.count = +1
        else:
            raise Exception("La posición no es válida")

#Colocar las mujeres primero
    def woman_first(self):
        list_cp = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 2:
                list_cp.add_to_start(temp.data)
            if temp.data.gender == 1:
                list_cp.add(temp.data)
            temp = temp.next
        self.head = list_cp.head

#Intercalar generos
    def interleave_genders(self):
        hombres = 0
        mujeres = 0
        list_cp_hombres = ListSE()
        list_cp_mujeres = ListSE()
        list_cp_bought = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp_hombres.add(temp.data)
                mujeres = mujeres + 1
            if temp.data.gender == 2:
                mujeres = mujeres + 1
                list_cp_mujeres.add(temp.data)
            temp = temp.next
        if hombres > mujeres:
            mayor = mujeres
        else:
            mayor= mujeres
        temp_hombres = list_cp_hombres.head
        temp_mujeres= list_cp_mujeres.head
        while mayor > 0:
            if temp_mujeres != None:
                if temp_mujeres.data != None:
                    list_cp_bought.add(temp_hombres.data)
                    temp_mujeres = temp_mujeres.next
            if temp_hombres != None:
                if temp_hombres.data != None:
                    list_cp_bought.add(temp_hombres.data)
                    temp_hombres = temp_hombres.next
            mayor = mayor - 1
        self.head = list_cp_bought.head
