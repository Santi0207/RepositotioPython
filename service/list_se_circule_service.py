from model.student import Student
from model.list_se_circule import ListSE_circule

class ListSE_Service_circule:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']

    def __init__(self):
        self.students = ListSE_circule

#Adicionar
    def add_to_last(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_last(student)
        else:
            raise Exception("La ciudad que ingresaste no es valida")

#Añadir al inicio
    def add_to_star(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_star(student)
        else:
            raise Exception("La ciudad que ingresaste no es valida")

#Invertir extremos
    def swap_ends(self):
        if self.students.head == None:
            return{"Message":"La lista esta vacia"}
        else:
            self.students.swap_ends()
            return {"Message":"Se han invertido los extremos"}

#Eliminar por dato
    def delete_for_data(self, id):
        if self.students.head == None:
            return {"message": "La lista está vacía"}
        else:
            deleted_student = self.students.delete_for_data(id)
            if deleted_student == None:
                return {"message": "El estudiante no existe"}
            else:
                return {"message": "Se ha eliminado el estudiante exitosamente"}

#Eliminar por posicion
    def delete_for_position(self, p):
        self.students. delete_for_position(p)
        return{"message":"Se ha eliminado exitosamente "}

#Mujeres primero
    def woman_first(self):
        if self.students.head== None:
            return {"message":" No existen datos "}
        else:
            self.students.woman_first()
            return {"message":"Se han colocado las mujeres primero"}

#Intercalar por genero
    def interleave_genders(self):
        self.students.interleave_genders()
        return {"message": "Se ha intercalado la lista"}


