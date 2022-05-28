from model.student import Student
from model.list_circle_de import ListDEC

class ListDECService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']
    def __init__(self):
        self.students = ListDEC()
        carloaiza = Student({"idenfication": "75147236", "name": "Carlos Loaiza",
                             "gender": 1, "salary": 2000000, "job": True, "city": self.cities[2]})
        self.students.addtostart(carloaiza)
        self.students.addtostart(Student({"idenfication": "1060456789",
                                   "name": "Valentina Hurtado",
                                   "gender": 2, "salary": 0, "job": False,
                                   "city": self.cities[0]}))

    def get_all_students(self):
        return self.students.head

    def add_student(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add(student)

        else:
            raise Exception("la ciudad ingresada no es valida")