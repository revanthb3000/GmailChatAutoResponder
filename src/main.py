import chatClient

def main():
    client = chatClient.getNewGmailClient()
    chatClient.login(client)
    chatClient.sendMessage(client, "rcprepdotcom@gmail.com", "Testing the new API !")
    while client.Process(1):
        pass

if __name__ == '__main__':
    main()