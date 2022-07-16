import json
import vlc
import time
import requests
import random
class PlayMusic():
    def __init__(self,path) -> None:
        try:
            readjson = open(path+"/config/user.json")
            self.user = json.load(readjson)
        except:
            pass
        self.player = None
        self.isPlaying = False
        self.index = 0
        self.dataPlayMode = [
            "order",
            "orderLoop",
            "shufflePlay",
            "singleLoop"
        ]
        self.PlayMode = "order"
        pass
    
    def renderPlaylist(self,data):
        # print(data,"from event socket")
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.headers["Authorization"] = "Bearer "+self.user["token"]
        resPlaylist = requests.get("http://192.168.100.38:5001/blogger/api/v2.1/playlist/"+data["id"],headers=self.headers)
        jsoned = json.loads(resPlaylist.text)
        self.playlist = jsoned["data"]["Music"]
        
    def renderPlayIndex(self,data,socket,user):
        try:
            self.index = data["index"]
            play = self.playlist[data["index"]]["title"]
            self.player = vlc.MediaPlayer(("http://192.168.100.38:5001/blogger/api/v2.1/music/"+play+".mp3").replace(" ","%20"))
            self.player.play()
            self.isPlaying = True
            time.sleep(1)
            while self.player.is_playing():
                    # s = vlc.MediaStats()
                    # m = self.player.get_media()
                    # print(self.player.get_media(),self.player.get_length(),m.get_stats(s),s)
                    time.sleep(1)
            else:
                print("SELESAI")
                if(self.PlayMode == "order"):
                    if(self.index < len(self.playlist)):
                        socket.emit("reqPlayIndex",{"email":user["email"],"index":self.index})
                    else:
                        socket.emit("reqPlayIndex",{"email":user["email"],"index":0})
                if(self.PlayMode == "shufflePlay"):
                    maxx = len(self.playlist)-1
                    value = random.randint(0,maxx)
                    print(value,len(self.playlist))
                    socket.emit("reqPlayIndex",{"email":user["email"],"index":value})
            self.player.release()
        except BaseException as err:
            print(str(err))
