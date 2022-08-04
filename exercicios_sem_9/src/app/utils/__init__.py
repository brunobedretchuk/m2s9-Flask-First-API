import re

def exist_value(request_json, data_in_db):
  for json in data_in_db:
    if json['id'] == request_json['id'] or json['tech'] == request_json['tech']:
      return True
  return False

def exist_key(request_json, list_keys):
  keys_not_have_in_request = []
  for key in list_keys:
    if key in request_json:
      continue
    else:
      keys_not_have_in_request.append(key)
  if len(keys_not_have_in_request) == 0:
    return request_json
  return {"error":  f"Está faltando o item {keys_not_have_in_request}" }

def is_req_valid(req):
    req_ids = list(req.keys())
    valid_req = ['id' , 'nome' , 'email' , 'senha' , 'cpf']
    req_ids.sort()
    valid_req.sort()
    if req_ids == valid_req:
        return True

def is_req_repeated(req , users):
    repeated_user = []
    print(users)
    for user in users['users']:
      if user['id'] == req['id']:
        repeated_user.append(user)
    
    if len(repeated_user) == 0:
      return True

def is_name_valid(req):
  if len(req['nome']) > 2:
    return True

def is_email_valid(req):
  pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
  if re.match(pattern , req['email']):
    return True

def is_password_valid(req):
  repeated_digits = False
  digit_list = []
  for char in req['senha']:
    for digit in digit_list:
      if char == digit:
        repeated_digits = True
    digit_list.append(char)
  
  if not repeated_digits and len(req['senha']) > 7:
    return True

def is_cpf_valid(req):
  repeated_digits = False
  digit_list = []
  for char in req['senha']:
    for digit in digit_list:
      if char == digit:
        repeated_digits = True
    digit_list.append(char)
  
  if not repeated_digits and len(req['cpf']) == 11:
    return True
