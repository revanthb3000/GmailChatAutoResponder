"""
The starting bot. Just starts the bot and sits idle.
"""
import chatClient

def main():
    client = chatClient.getNewGmailClient()
    chatClient.login(client)
    while client.Process(1):
        pass

if __name__ == '__main__':
    main()