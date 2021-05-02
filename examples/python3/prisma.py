import requests
import json


class prismaAPI:
    ##initialize the class with the Username and API key
    def __init__(self,user,apikey):
        self.user=user
        self.apikey=apikey
        self.API_HOSTNAME = 'prisma.cubedhost.com';
        self.API_PATH = '/api/';
        self.headder={
            'Content-Type': 'application/json',
            'X-Api-Key': API_KEY,
            'X-Api-User': API_USER
            }
    def getServers(self):
        ##gives servers your account has access to
        path="http://{}{}servers".format(self.API_HOSTNAME,self.API_PATH)
        print(path)
        response  = requests.post(path,params={'q': 'requests+language:python'}, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def getServersConfig(self,serverId):
        ##returns server config for serverID
        path="http://{}{}servers/{}".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response  = requests.post(path,params={'q': 'requests+language:python'}, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def getServersUsers(self,serverId):
        ## returns User accounts for serverID
        path="http://{}{}server/{}/users".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response  = requests.post(path,params={'q': 'requests+language:python'}, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def getServersDatabase(self,serverId):
        #returns server data base info for serverID
        path="http://{}{}server/{}/database".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response  = requests.post(path,params={'q': 'requests+language:python'}, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def getServersPlayers(self,serverId):
        ##returns server players and player info for serverID
        path="http://{}{}server/{}/players".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response  = requests.post(path,params={'q': 'requests+language:python'}, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def stopServer(self,serverID):
        ##stops serverID
        path="https://{}{}server/{}/stop".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response = requests.post(path, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def startServer(self,serverID):
        ##starts serverID
        path="https://{}{}server/{}/start".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response = requests.post(path, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def restartServer(self,serverID):
        ##restarts serverID
        path="https://{}{}server/{}/restart".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response = requests.post(path, headers=self.headder)
        serverlist = response.json()
        return serverlist
    def sendCommand(self, serverId,command):
        ##sends command to serverID
        data=json.dumps({"command":command})
        
        path="https://{}{}server/{}/console".format(self.API_HOSTNAME,self.API_PATH,serverId)
        response = requests.post(path, headers=self.headder,data=data)
        serverlist = response.json()
        return serverlist

