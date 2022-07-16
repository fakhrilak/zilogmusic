import socketio
import json
import vlc
import time
from zilogmusic.controllers.PlayMusic import PlayMusic
class SOCKET_IO():
    sio = socketio.Client()
    def __init__(self,path):
        self.path = path
        self.user = None
        self.playmusic = PlayMusic(self.path)
        pass
    
    def setup(self):
        try:
            readjson = open(self.path+"/config/user.json")
            user = json.load(readjson)
            self.user = user
        except:
            return 0
        if self.user:
            self.sio.connect("http://192.168.100.38:5001",namespaces=['/'])
        else:
            return 0
    def SocketJoin(self):
        if(self.user):   
            self.sio.emit("joinMusic",{
                "email" : self.user["email"],
                "mode" : "speaker",
                "socketId" : self.sio.eio.sid
            })
        else:
            p = vlc.MediaPlayer(("http://192.168.100.38:5001/blogger/api/v2.1/music/pleaseLogin.mp3").replace(" ","%20"))
            p.play()
            time.sleep(1)
            while p.is_playing():
                    time.sleep(1)
            p.release()
            print("Please Login")
    
    def call_backs(self):
        @self.sio.on("onRes-reqToSpeakerRenderPlaylist")
        def on_connect(data):
            print(data)
            self.playmusic.renderPlaylist(data)
            
        @self.sio.on("onRes-reqPlayIndex")
        def onPlayIndex(data):
            if(self.playmusic.isPlaying == True):
                self.playmusic.player.stop()
                self.playmusic.renderPlayIndex(data,self.sio,self.user)
            else:
                self.playmusic.renderPlayIndex(data,self.sio,self.user)
            print(self.playmusic.player.get_state())
                
        @self.sio.on("onRes-reqPlayStatus")
        def onPlayStatus(data):
            try:
                if data["status"] == False:
                    self.playmusic.player.pause()
                    self.playmusic.isPlaying == data["status"]
                elif data["status"] == True:
                    self.playmusic.player.play()
                    self.playmusic.isPlaying == data["status"]
            except:
                pass
        
        @self.sio.on("onRes-reqChangePlaymode")
        def onChangePlayMode(data):
            self.playmusic.PlayMode = data["mode"]
            print("Now Mode",self.playmusic.PlayMode)