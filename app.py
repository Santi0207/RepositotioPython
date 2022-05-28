from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.list_se_controller import app_list_se

#from controller.list_se_circule_controller import app_list_se_circule

app = Flask(__name__)
app.register_blueprint(app_student)

app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
#app.register_blueprint(app_list_se_circule)




if __name__ == '__main__':
    app.run()
