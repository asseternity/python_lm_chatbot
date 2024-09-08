from message import Message
from interface import Interface_Creator

message1 = Message('Aigul', 'Hello, Dauren!')

chatbot1 = Interface_Creator()
chatbot1.window_main_settings('Awesome Chatbot', 500, 500)
chatbot1.new_AI_message_label(message1)
chatbot1.start_window()