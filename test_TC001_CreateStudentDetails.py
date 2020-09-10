# import pytest
import requests
import jsonpath
import json

# def test_add_student():
#     API_URL="http://thetestingworldapi.com/api/studentsDetails"
#     request_file=open("G://API testing Practices//StudentsManagement//TC001_Create_new_user.json","r")
#     request_json=json.loads(request_file.read())
#     add_student=requests.post(API_URL,request_json)
#     print(add_student.text)
def test_get_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/54626"
    # parameters={'id':54626}
    get_student=requests.get(API_URL)
    print(get_student.content)
    json_get=json.loads(get_student.text)
    id=jsonpath.jsonpath(json_get,"data.id")
    assert id[0]==54626

def test_update_student_data():
    API_URL='http://thetestingworldapi.com/api/studentsDetails/54626'
    update_file=open("G://API testing Practices//StudentsManagement//TC_001_Update_Status.json","r")
    update_request=json.loads(update_file.read())
    update_student=requests.put(API_URL,update_request)
    print(update_student.text)

def test_get_student_data_aup():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/54626"
    # parameters={'id':54626}
    get_student=requests.get(API_URL)
    print(get_student.content)
    json_get=json.loads(get_student.text)
    lname=jsonpath.jsonpath(json_get,"data.last_name")
    assert lname[0]=='API Automation using Python'


