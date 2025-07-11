import json 


import requests

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    params = {}
    if id is not None:
        params['id'] = id  # Pass ID in query string
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers,params=params)
    data = r.json()
    print(data)

get_data(2)

def update_data():
    data={'id': 5,
          'name':'ahmad',
          'city': 'lahore'}
    json_data = json.dumps(data)
    r=requests.put(url= URL, data= json_data)
    data = r.json()
    print(data)
#update_data() 
def post_data():
    data={
          'name':'raima',
        'roll': 129,
          'city': 'lahore','profile': {
            'bio': 'Loves coding',
            'age': 21
        }}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    
    r=requests.post(url= URL, headers= headers, data= json_data)
    data = r.json()
    print(data)
#post_data()
def delete_data():
    data={'id': 5}
    json_data = json.dumps(data)
    r=requests.delete(url= URL, data= json_data)
    data = r.json()
    print(data)
#delete_data() 