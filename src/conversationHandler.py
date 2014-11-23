"""
This guy stores all the conversations you're having right now and responds appropriately.
"""
from botResponses import *
from jokesData import *
import re

global conversations 

conversations = {}

"""
Given a new message and the person who sent it, I either create a new mapping or add to the existing one.
"""
def addMessageToConversation(address, newMessage):
    global conversations
    if(isChatNew(address)):
        newDictionary = {"messages" : [newMessage], "state" : 0};
        conversations[address] = newDictionary
    else:
        conversations[address]["messages"].append(newMessage)
        
"""
This function checks if a chat is already in progress.
"""
def isChatNew(address):
    if(address in conversations.keys()):
        return False
    return True

"""
Changes the state of a conversation to a given value.
"""
def changeState(address, newState):
    if(address in conversations.keys()):
        conversations[address]["state"] = newState
        
"""
A basic utility function.
"""
def printConversations():
    global conversations
    for key in conversations.keys():
        print key + " ",
        print conversations[key]

"""
The core of this entire file. Given a message and an address, previous conversation is looked at and a response is generate.
"""
def getResponse(fromAddress, newMessage):
    global conversations
    addMessageToConversation(fromAddress, newMessage)
    userChat = conversations[fromAddress]
    if(userChat["state"]==0): #Means that the user is still in state 0.
        changeState(fromAddress, 1)
        return BOT_INTRO
    else:#In some other state
        userMessageResponse = re.sub("[^0-9]","",newMessage)
        userMessageResponse = "0" + userMessageResponse
        if(int(userMessageResponse)==1):
            return BOT_OWNER_WHEARABOUTS + "\n" + BOT_ASK_FOR_RESPONSE
        elif(int(userMessageResponse)==2):
            return getRandomJoke() + "\n" + BOT_ASK_FOR_RESPONSE
        else:
            return BOT_INVALID_RESPONSE + "\n" + BOT_ASK_FOR_RESPONSE
    