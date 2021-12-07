import flask

import Receipt
from Collection import collection
from Validation import Validation
from flask import Flask,jsonify,request
import json
from users import users
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import jwt
from functools import wraps
from orders import orders


app = Flask(__name__)
database = "data.txt"
collect = collection.read_file(database)
users_db="users.txt"
us=users.read_file(users_db)
ord="orders.txt"
od=orders.read_file(ord)

def token_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token=None
        if 'token' in flask.request.headers:
            print("smth")
            token=flask.request.headers['token']
            print("smth")
            print(token)
        else:
            return jsonify({'message': 'token not found'}), 404
        data=jwt.decode(token,"my_secret_word",algorithms=["HS256"])
        curreent_user=us.col[us.search_email(data['email'])]
        return f(curreent_user,*args,**kwargs)
    return decorator
@app.route("/get_all",methods=['GET'])
@token_required
def get_all():
    print(collect.all_data_to_json())
    return collect.all_data_to_json()


@app.route("/receipt/<string:id>",methods=['GET'])
@token_required
def get(id):
    if collect.search_id(id)!= False:
        out = collect.col[int(collect.search_id(id))].data_to_json()
        return out
    return jsonify({'message':'not found'}), 404
@app.route("/get",methods=['GET'])
@token_required
def get_sort():
    sort_type = request.args.get('sort_type')
    if Validation.str_to_sort_num(sort_type)!=False:
        collect.sort(Validation.str_to_sort_num(sort_type), database)
        return collect.all_data_to_json()
    return jsonify({'message':'type not found'}), 404

@app.route("/receipt",methods=['POST'])
@token_required
def add(current_user):
    if not current_user.is_admin:
        flask.make_response(flask.abort(jsonify({'message': 'You are not admin'}), 400))
    if Validation.valid_name(request.json["recipient_name"]):
        if Validation.valid_bank(request.json["bank"]):
            if Validation.valid_iban(request.json["recipient_iban"]):
                if Validation.valid_paymant_type(request.json["payment_type"]):
                    if Validation.valid_time(request.json["payment_datetime"]):
                        if Validation.positive_num(request.json["amount"]):
                            id=request.json["id"]
                            name=request.json["recipient_name"]
                            iban=request.json["recipient_iban"]
                            bank=request.json["bank"]
                            type=request.json["payment_type"]
                            amount=request.json["amount"]
                            time=request.json["payment_datetime"]
                            collect.col.append(Receipt.receipt(id,name,iban,bank,type,amount,time))
                            collect.update_file(database)
                            return jsonify({'message': 'Success'})
    return jsonify({'message': 'not valid info'}), 500
@app.route("/reciept/<string:id>",methods=['DELETE'])
@token_required
def delete(current_user,id):
    if not current_user.is_admin:
        flask.make_response(flask.abort(jsonify({'message': 'You are not admin'}), 400))
    if collect.search_id(id) != False:
        collect.remove(id,database)
        return jsonify({'message': 'Success'}), 404
    return jsonify({'message': 'not found'}), 404

@app.route("/receipt",methods=['GET'])
@token_required
def get_by():
    sort_type = request.args.get('sort_type')
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    search = request.args.get('search')
    if (Validation.positive_num(offset) or offset=='0') and Validation.positive_num(limit)  and Validation.str_to_sort_num(sort_type)!=False:
        if int(offset)*int(limit)<len(collect.col):
            out=""
            offset=int(offset)
            limit=int(limit)
            collect.sort(Validation.str_to_sort_num(sort_type), database)
            num = collect.search(search)
            out = ""
            outp=collection()
            if len(num) > 0:
                for i in num:
                    outp.col.append(collect.col[i])
                if (offset+1)*limit<len(outp.col):
                    for i in range(offset*limit,(offset+1)*limit):
                        out+=outp.col[i].data_to_json()+'\n'
                else:
                    if offset*limit<len(outp.col):
                        for i in range(offset * limit, len(outp.col)):
                            out += outp.col[i].data_to_json()+'\n'
                        dict={'count':len(collect.col)}
                        out +=json.dumps(dict)
                        return out
                    else:
                        return jsonify({'message': 'not found'}), 404
            else:
                return jsonify({'message': 'not found'}), 404
    else:
        if Validation.str_to_sort_num(sort_type)!=False and limit=='' and offset=='':
            collect.sort(Validation.str_to_sort_num(sort_type), database)
            num = collect.search(search)
            out = ""
            if len(num) > 0:
                for i in num:
                    out += collect.col[i].data_to_json() + "\n"
                dict = {'count': len(collect.col)}
                out += json.dumps(dict)
                return out
            else:
                return jsonify({'message': 'not found'}), 404
    return jsonify({'message': 'not found '}), 404
@app.route("/api/register",methods=['POST'])
def registr():
    data=flask.request.get_json()
    data['password']=generate_password_hash(data['password'],method='sha256')
    us.add_new(users_db,**data)
    print(us)
    return jsonify({'message': 'Succsess'})

@app.route("/api/login",methods=['POST'])
def login():
    data = flask.request.get_json()
    if us.search_email(data["email"]) is False:
        flask.make_response(flask.abort(jsonify({'message': 'not found'}), 404))
    a=us.col[us.search_email(data["email"])]
    print(a)
    if check_password_hash(a.password,data['password']):
        token=jwt.encode({"exp":(datetime.datetime.utcnow()+datetime.timedelta(minutes=30)),"email":a.email},"my_secret_word",algorithm="HS256")
        return jsonify({'message': 'succsess','token':token})
    else:
        return jsonify({'message': 'not found '}), 404

@app.route("/orders",methods=['POST'])
@token_required
def new_ord(current_user):
    if Validation.valid_name(request.json["recipient_name"]):
        if Validation.valid_bank(request.json["bank"]):
            if Validation.valid_iban(request.json["recipient_iban"]):
                if Validation.valid_paymant_type(request.json["payment_type"]):
                    if Validation.valid_time(request.json["payment_datetime"]):
                        if Validation.positive_num(request.json["amount"]):
                            id=request.json["id"]
                            name=request.json["recipient_name"]
                            iban=request.json["recipient_iban"]
                            bank=request.json["bank"]
                            type=request.json["payment_type"]
                            amount=request.json["amount"]
                            time=request.json["payment_datetime"]
                            collect.col.append(Receipt.receipt(id,name,iban,bank,type,amount,time))
                            collect.update_file(database)
                            od.add_new(ord,current_user.email,[id])
                            return jsonify({'message': 'Success'})
@app.route("/orders",methods=['GET'])
@token_required
def all_orders(current_user):
    if od.search_email(current_user.email) is not False:
        str=""
        for i in range(len(od.col[od.search_email(current_user.email)].orders_id)):
            str+=collect.col[collect.search_id(od.col[od.search_email(current_user.email)].orders_id[i])].data_to_json()
        return str
    return jsonify({'message': 'not found '}), 404

@app.route("/orders/<string:id>",methods=['GET'])
@token_required
def id_orders(current_user,id):
    if od.search_email(current_user.email) is not False:
        str=""
        for i in range(len(od.col[od.search_email(current_user.email)].orders_id)):
            if collect.col[collect.search_id(od.col[od.search_email(current_user.email)].orders_id[i])].id==id:
                str+=collect.col[collect.search_id(od.col[od.search_email(current_user.email)].orders_id[i])].data_to_json()
        return str
    return jsonify({'message': 'not found '}), 404


if __name__ == '__main__':
    app.run(debug=True)