class Message:
    messages = []
    def __init__(self, author: str, text: str):
        self.author = author;
        self.text = text;
    def add_user_message(self, text):
        message = Message('user', text)
        Message.messages.append(message)
        return message
    def add_bot_message(self, text):
        message = Message('bot', text)
        Message.messages.append(message)
        return message
    def retrieve_all_messages(self):
        return Message.messages
    