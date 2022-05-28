from service.list_se_circule_service import ListSE_Service_circule
from flask import Response, json, jsonify, Blueprint, request
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se", __name__)

list_se_circule_service = ListSE_Service_circule()

#Muestrar toda la lista
@app_list_se.route('/list_se/all')
def get_all_students():

    return Response(status=200, response=json.dumps(list_se_service.get_all_students(),
                    cls=UtilEncoder), mimetype="application/json")

#Añadir
@app_list_se.route('/list_se', methods=['POST'])
def save_student():
    data = request.json
    try:
        list_se_circule_service.add_student(data)
        return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")

#Añadirlos al inicio
@app_list_se.route('/list_se/addtostar', methods=['POST'])
def add_to_star():
    data = request.json
    try:
        list_se_circule_service.add_to_star(data)
        return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")

#Invertir extremos
@app_list_se.route('/list_se/invert_extre')
def swap_ends():
    return Response(status=200,
                    response=json.dumps(list_se_circule_service.swap_ends()),mimetype="application/json")

#Insertar en posicion
@app_list_se.route("/listse/toposition/<position>",methods=["POST"])
def insert_in_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_circule_service.insert_in_position(int(position),request.json)),
                    mimetype="application/json")

#Eliminar por dato
@app_list_se.route("/listse/delete_for_data/<id>")
def delete_for_data (id):
    return Response(status=200,
                    response=json.dumps(list_se_circule_service.delete_for_data(int(id))),
                    mimetype="application/json")

#Eliminar por posicion
@app_list_se.route('listse/delete_for_position/<position>')
def delete_for_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_circule_service.delete_for_position(int(position))),
                    mimetype="application/json")

#Colocar las mujeres primero
@app_list_se.route('listse/mujeres_primero/<gender>')
def woman_firs():
    return Response(status=200,
                    response=json.dumps(list_se_circule_service.woman_first()), mimetype="application/json")

#Intercalar generos
@app_list_se.route('listse/intercalar_generos')
def interleave_genders():
    return Response(status=200,
                    response=json.dumps(list_se_circule_service.interleave_genders()),
                    mimetype="application/json")