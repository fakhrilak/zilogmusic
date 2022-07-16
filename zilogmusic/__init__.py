import argparse
from ast import arg
from zilogmusic.app import app
from zilogmusic.controllers.Socket import SOCKET_IO
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("start",type=str,help="to start app")
    return parser.parse_args()
path  = __file__
splited = path.split("/")
directory=""
for i in splited[1:-1]:
    directory+= "/"+i
def main():
    try:
        args = parse_args()
        apps = app()
        if args.start == "start":
            print("====================== STARTING APP =======================")
            socket = SOCKET_IO(directory)
            socket.setup()
            socket.SocketJoin()
            socket.call_backs()
        if args.start == "login":
            print("====================== STARTING APP =======================")
            apps.Login()
            return 0
            print("this is start")
        if args.start == "play":
            apps.PlayMusic()
    except BaseException as err:
        print(err)