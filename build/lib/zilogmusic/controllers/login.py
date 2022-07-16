from lib2to3.pytree import Base
import requests
import json
from getpass import getpass
class Login():
    def __init__(self,path):
        try:
            readjson = open(path+"/config/user.json")
            user = json.load(readjson)
            self.user = user["username"]
        except BaseException as err :
            self.user = None
        if self.user:
            self.name = input("Username or Email ("+self.user+") : ")
        else:
            self.name = input("Username or Email : ")
        self.passwd = getpass("Password : ")
        config = {
            "email" : self.name,
            "password" : self.passwd
        }

        self.headers = {
            'Content-Type': 'application/json'
        }

        res = requests.post("http://192.168.100.38:5001/blogger/api/v2.1/login",json=config,headers=self.headers)
        jsoned = json.loads(res.text)
        if res.status_code != 200:
            print(jsoned["message"])
        else:
            self.headers["Authorization"] = "Bearer "+jsoned["token"]
            auth  = requests.get("http://192.168.100.38:5001/blogger/api/v2.1/auth",headers=self.headers)
            jsonedAuth = json.loads(auth.text)
            print(jsonedAuth["massage"])
            jsonedAuth["data"]["token"] = jsoned["token"]
            ######################### WRITE JSON CONFIG #####################
            jsonString = json.dumps(jsonedAuth["data"],indent=4,sort_keys=True)
            jsonFile = open(path+"/config/user.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            #################################################################
        return None