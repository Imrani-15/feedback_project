import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'retrieve/'
# def get_resource(id):
#     resp = requests.get(BASE_URL+ENDPOINT+id+'/')
#     print(resp.status_code)
#     print(resp.json())
# id = input("Enter the id here")
# get_resource(id)

# def get_all():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
#get_all()

# def create_resource():
#     new_emp = {
#         'eno': 900,
#         'ename': 'Imrani',
#         'esal': 15000,
#         'eaddr': 'Bangulore',
#     }
#     resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

# def update_resource(id):
#     new_emp = {
#         'esal':70000,
#         'eaddr':'Pune',
#     }
#     resp = requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
#     print(resp.status_code)
#    print(resp.json())
# id = input('Enter the id here')
# update_resource(id)

def delete_resource():
    r=requests.delete(BASE_URL+ENDPOINT+'8/')
    print(r.status_code)
    print(r.json())
delete_resource()