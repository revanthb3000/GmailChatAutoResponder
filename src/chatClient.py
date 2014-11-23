"""
This guy contains everything to do with connecting, sending, receiving messages. Basically everything your IM Client does.
"""

import xmpp
import conversationHandler
from clientParameters import *

"""
Returns a new client object after connecting to the gmail servers. Play around with that handle.
"""
def getNewGmailClient(debug = False):
    if(debug):
        client = xmpp.Client(GTALK_CLIENT_NAME)
    else:
        client = xmpp.Client(GTALK_CLIENT_NAME, debug = [])
    client.connect(server=(GTALK_SERVER_NAME,GTALK_PORT_NUMBER))
    return client
    
"""
You have a client and you now want to log into your account. That's what this guy does.
"""
def login(client):
    fileHandle = open(CREDENTIALS_FILENAME,'r')
    username = str(fileHandle.readline()).strip()
    password = str(fileHandle.readline()).strip()
    fileHandle.close()
    
    client.auth(username, password, 'RBBot')
    client.sendInitPresence()
    client.getRoster()
    client.RegisterHandler('message', handleMessage)

"""
Given a toAddress and a messageString, this guy tries to send a message.

Note : Obviously Google won't let you send a message to anyone. Should I maybe report errors in that case ? I'll ignore for now given that I'm the only user.
"""
def sendMessage(client, toAddress, messageString):
    message = xmpp.Message(toAddress, messageString)
    message.setAttr('type', 'chat')
    client.send(message)

"""
You get a message and you want to do something with it ? This is the function for you !
"""
def handleMessage(client, receivedMessage): 
#     print receivedMessage
    fromAddress = receivedMessage.getFrom()
    messageBody = receivedMessage.getBody()
    if(messageBody!=None):
        message = str(messageBody)
        responseMessage = conversationHandler.getResponse(str(fromAddress), message)
        conversationHandler.printConversations()
        sendMessage(client, fromAddress, "-------")
        sendMessage(client, fromAddress, responseMessage)
