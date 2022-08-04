from flask import json

def save(data):
  json_object = json.dumps(data, indent=4)
  with open("src/app/db/users.json", "w") as outfile:
      outfile.write(json_object)
def read():
  try:
    with open('src/app/db/users.json', 'r') as openfile:
      json_object = json.load(openfile)
      return json_object
  except:
     return None