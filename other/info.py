import json

class info:
    def __init__(self, firstname, lastname, discord):
        self.firstname  = firstname
        self.lastname   = lastname
        self.discord    = discord
                                       
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
        
def setUserFirst():

    with open('info.json') as f:
        data = json.load(f)
    list = []
    for person in data['people']:
        list.append(person['firstname'])
    return list
    
def setUserLast():

    with open('info.json') as f:
        data = json.load(f)
    list = []
    for person in data['people']:
        list.append(person['lastname'])
    return list
    
def setUserDiscord():
    
    with open('info.json') as f:
        data = json.load(f)
    list = []
    for person in data['people']:
        list.append(person['discord'])     
    return list
    
def getBotId():
    with open('bot.json') as f:
        data = json.load(f)
    list = []
    for bot in data['bots']:
        list.append(bot['id'])
    return list