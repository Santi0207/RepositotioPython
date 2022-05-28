from service.list_de_circule_service import ListDECService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_dec = Blueprint("app_list_dec",__name__)
list_de_circle_service = ListDECService()

@app_list_dec.route('/list_dec/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_de_circle_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_dec.route('/list_dec',methods=['POST'])
def save_student():
    data = request.json
    try:

        list_de_circle_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")

    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                    mimetype="application/json")