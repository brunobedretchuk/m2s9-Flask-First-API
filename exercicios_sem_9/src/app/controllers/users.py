from operator import indexOf
from flask import Blueprint , request
import json
from src.app.utils import *
from src.app.db import read, save

user = Blueprint('user', __name__, url_prefix="/user")




@user.route('/' , methods = ['GET'])
def list_all_users():
    users = json.dumps(read()["users"])
    return users , 200


@user.route("/" , methods = ['POST'])
def add_new_user():
    users = read()
    req = request.get_json()

    if not is_req_valid(req):
        return 'Use o formato correto: id - nome - email - senha - cpf' , 400
    if not is_name_valid(req):
        return 'Nome deve conter no mínimo 3 caracteres' , 400
    if not is_email_valid(req):
        return 'Email deve ser no formato "xxxxxxxx@.com"' , 400
    if not is_password_valid(req):
        return 'Senha deve conter ao menos 8 dígitos e nenhum caracter repetido"' , 400
    if not is_cpf_valid(req):
        return 'CPF deve conter 11 dígitos e nenhum caracter repetido"' , 400
    if not is_req_repeated(req , users):
        return 'Usuário já adicionado ao DB' , 400
    else:
        users["users"].append(req)
        data = users
        is_req_valid(req)
        save(data)
        return f'You added {req["nome"]} to the database!' , 201


@user.route("/<int:cpf>" , methods = ['DELETE'])
def delete_user(cpf):
    users = read()
    print(cpf)
    for index , user in enumerate(users['users']):

        if int(user['cpf']) == cpf:
            users['users'].pop(index)
            data = users
            save(data)
            return f'Usuário {user["nome"]} removido do DB!' , 200

    return 'Usuário não encontrado!' , 400
        

    
