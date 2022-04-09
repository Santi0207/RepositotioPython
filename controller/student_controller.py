from flask import Response, Blueprint, jsonify, json
from service.student_service import StudentService
from util.util_encoder import UtilEncoder

app_student = Blueprint("app_student",__name__)

@app_student.route('/student/all')
def get_all_students():
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_all_students(),cls=UtilEncoder)
                    ,mimetype="application/json")
    #return jsonify(student_service.get_all_students_dict())

@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_students_by_gender(gender):
    student_service = StudentService()
    return str(student_service.get_percentage_students_by_gender(int(gender)))

@app_student.route('/student/per_students_job_avgsalary/<gender>')
def get_percentage_students_job_avg_salary(gender):
    student_service = StudentService()
    return jsonify(student_service.get_percentage_students_job_avg_salary(int(gender)))

#EJERCICIO 1
@app_student.route("/estudiantes/genderbysalary/<gender>/<salary>")
def get_salary_students(gender,salary):
    student_service=StudentService()
    return jsonify(student_service.get_salary_students(int(gender),int(salary)))

#EJERCICIO 2

@app_student.route("/estudiante/salario_mayor/<gender>")
def get_student_most_payed(gender):
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_student_most_payed(int(gender)),
                    cls=UtilEncoder)
                    ,mimetype="application/json")

#EJERCICIO 3
@app_student.route("/student/topsalary/minsalary/<Minsalary>/<Topsalary>")
def get_students_range_salary(Minsalary, Topsalary):
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_students_range_salary(int(Minsalary), int(Topsalary))
                    ,cls=UtilEncoder),
                    mimetype="application/json")

#EJERCICIO 4
@app_student.route("/student/average/salary/<gender>")
def get_average_salary(gender):
    student_service = StudentService()
    return str(student_service.get_average_salary(int(gender)))

@app_student.route("/student/age_prom")
def age_prom():
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.age_prom(),cls=UtilEncoder)
                    , mimetype="application/json")

@app_student.route("/student/cities/job")
def get_students_by_city():
    student_service = StudentService()
    return jsonify(student_service. get_students_by_city())





