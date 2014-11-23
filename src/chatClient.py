import xmpp

def getNewGmailClient():
    client = xmpp.Client('gmail.com')
    client.connect(server=('talk.google.com',5223))
    return client
    
def login(client):
    fileHandle = open('credentials.dat','r')
    username = str(fileHandle.readline()).strip()
    password = str(fileHandle.readline()).strip()
    fileHandle.close()
    
    client.auth(username, password, 'Android')
    client.sendInitPresence()
    client.getRoster()
    client.RegisterHandler('message', handleMessage)
    
def sendMessage(client, toAddress, messageString):
    message = xmpp.Message(toAddress, messageString)
    message.setAttr('type', 'chat')
    client.send(message)
    
def handleMessage(client, receivedMessage): 
    print receivedMessage
    fromAddress = receivedMessage.getFrom()
    messageBody = receivedMessage.getBody()
    if(messageBody!=None):
        message = str(messageBody)
        sendMessage(client, fromAddress, "Yo")