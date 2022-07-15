from zilogmusic.controllers.login import Login as controllersLogin

################################### READ PATH ###################################
path  = __file__
splited = path.split("/")
directory=""
for i in splited[1:-1]:
    directory+= "/"+i
#################################################################################

class app():
    def __init__(self):
        self.path = directory
        pass

    def app(self):
       print("masuk app")

    def Login(self):
        controllersLogin(self.path)