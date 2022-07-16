from zilogmusic.controllers.login import Login as controllersLogin
from zilogmusic.controllers.PlayMusic import PlayMusic
# from zilogmusic.controllers.Socket import SOCKET_IO
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
        # self.socket = SOCKET_IO(self.path)
        # self.socket.setup()
        pass

    def app(self):
       print("masuk app")

    def Login(self):
        controllersLogin(self.path)
        
    def PlayMusic(self):
        print("t")
        # self.socket.SocketJoin()