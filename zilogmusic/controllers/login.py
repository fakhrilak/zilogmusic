import requests
import json
from getpass import getpass
class Login():
    def __init__(self,path):
        self.name = input("Username or Email : ")
        self.passwd = getpass("Password : ")
        config = {
            "username" : self.name,
            "password" : self.passwd
        }

        self.headers = {
            'Content-Type': 'application/json'
        }

        res = requests.post("https://v2-blogger-server.zilog.club/blogger/api/v2.1/login",data=config,headers=self.headers)
        print(res.text)

        ######################### WRITE JSON CONFIG #####################
        jsonString = json.dumps(config,indent=4,sort_keys=True)
        jsonFile = open(path+"/config/config.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        #################################################################
        print(config,"this is path root program")