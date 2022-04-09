from model.student import Student
from model.list_se import ListSE

class ListSE_Service:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']

    def __init__(self):
        self.students = ListSE()

    def get_all_students(self):
        return self.students.head

    def add_student(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add(student)
        else:
            raise Exception("La ciudad que ingresaste no es valida")
