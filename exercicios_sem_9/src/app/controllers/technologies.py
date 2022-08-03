from flask import Blueprint , request
import json
from src.app.utils import exist_key , exist_value
from src.app.db import read, save

technology = Blueprint('technology', __name__, url_prefix="/technology")

@technology.route('/' , methods = ['GET'])
def list_all_technologies():
    technologies = json.dumps(read()["technologies"])
    return technologies


@technology.route("/" , methods = ['POST'])
def add_new_technology():
    technologies = read()
    req = request.get_json()
    technologies["technologies"].append(req)
    data = technologies
    save(data)

    return f'You added {req["name"]} to the database!'

@technology.route("/" , methods = ['POST'])
def add_new_technology():
    technologies = read()
    req = request.get_json()
    technologies["technologies"].append(req)
    data = technologies
    save(data)

    return f'You added {req["name"]} to the database!'

@technology.route("/<int:id>" , methods = ['DELETE'])
def delete_technology():
    technologies = read()
    req = request.get_json()
    technologies["technologies"].append(req)
    data = technologies
    save(data)

    return f'You added {req["name"]} to the database!'
