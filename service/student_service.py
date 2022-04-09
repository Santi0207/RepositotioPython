from model.student import Student
import json

class StudentService:
    students = []
    cities = ['Manizales','Pereira','Chinchina', 'Armenia']

    def __init__(self):
        self.students = []
        self.students.append(Student("363763763", 1, 22020202,True, "Nick Alejandro villa", 21, True,"Armenia"))
        self.students.append(Student("1283839122", 2, 0, False, "Valentina Hurtado", 19, False,"Manizales"))
        self.students.append(Student("128839220", 1, 100000, True, "Kevin Sánchez", 28, True,"Pereira"))
        self.students.append(Student("123884922", 1, 200000000, True, "Santiago Lopez", 19, False,"Manizales"))
        self.students.append(Student("122931228", 1, 1498899, True, "Alejandro libreros",19, False,"Armenia"))
        self.students.append(Student("198281012", 2, 123913883, True, "Laura Alayon",19, True,"Pereira"))
        self.students.append(Student("283222311", 2, 28991222, True, "Manuela Tabares",19, False,"Manizales"))

    def get_all_students(self):
        return self.students

    def get_percentage_students_by_gender(self,gender):
        count =0
        for student in self.students:
            if student.gender == gender:
                count = count + 1
        return count / len(self.students)

    def get_percentage_students_job_avg_salary(self,gender):
        count=0
        sum_salary=0
        for student in self.students:
            if student.job == True and student.gender == gender:
                count= count +1
                sum_salary = sum_salary + student.salary
        if count > 0 :
            return {"Salario promedio": sum_salary/count,"Cantidad": count,"% trabajan": count/len(self.students)}
        else:
            return {"Error":"la consulta no generó resultados"}
#EJERCICIO 1

    def get_salary_students(self,gender,salary):

        list_gender =[]
        for student in self.students:
            if student.gender == gender and student.salary > salary:
                list_gender.append(student.__dict__)
        return(list_gender)

#EJERCICIO 2

    def get_student_most_payed(self,gender):
        list_gender=[]
        for student in self.students:
            if student.gender == gender and student.gender == gender:
                list_gender.append(student.salary)

        salary_mayor=list_gender[0]
        for salary in list_gender:
            if salary > salary_mayor:
                salary_mayor = salary

        for student_mayor in self.students:
            if student_mayor.salary == salary_mayor:
                return (student_mayor)

#EJERCICIO 3

    def get_students_range_salary(self,Minsalary, Topsalary):
        list_range=[]
        for student in self.students:
            if student.salary >= Minsalary and student.salary <= Topsalary:
                list_range.append(student.__dict__)
        return(list_range)

#EJERCICIO 4

    def get_average_salary(self, gender):
        person_work = 0
        salary_acum = 0
        for students in self.students:
            if students.gender == gender:
                if students.job == True:
                    person_work = person_work+1
                    salary_acum = salary_acum + students.salary
        average = salary_acum/person_work
        if gender == 1:
            return("Los hombres tienen un salario de:",average)
        elif gender == 2:
            return ('Las mujeres tienen un salario de:',average)

#EJERCICIO CLASE #1

    def age_prom(self):
        sum = 0
        list = []
        for student in self.students:
            if student.age == student.age:
                sum = sum + student.age
                prom = sum / len(self.students)
        for student in self.students:
            if student.zone == True and student.age > prom:
                list.append(student.__dict__)
        return (list)

#EJERCICIO CLASE 2

    def get_dict_cities(self):
        dict_cities={}
        for city in self.cities:
            dict_cities[city] = [0, 0]
        return dict_cities

    def get_students_by_city(self):
        dict_cities = self.get_dict_cities()
        for student in self.students:
            if student.job:
                dict_cities[student.city][0] = dict_cities[student.city][0] + 1
            else:
                dict_cities[student.city][1] = dict_cities[student.city][1] + 1

        return dict_cities


















