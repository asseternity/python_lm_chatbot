from tkinter import *
from message import Message
from ai_response import AI_Chatter

class Interface_Creator:
    def __init__(self):
        self.root = Tk()
        self.messages_area = Frame(master=self.root, relief=RAISED, borderwidth=5)
        self.message_entry = None
        self.ai = None
        pass
    def window_main_settings(self, title, height, width):
        self.root.title(title)
        dimensions = str(height) + 'x' + str(width)
        self.root.geometry(dimensions)
    def new_AI_message_label(self, message_object):
        message_frame = Frame(master=self.messages_area, relief=RAISED, borderwidth=5)
        message_frame.pack(anchor='w', padx=10, pady=10)
        message_label = Label(message_frame, text=message_object.text)
        message_label.pack()
    def new_USER_message_label(self, message_object):
        message_frame = Frame(master=self.messages_area, relief=RAISED, borderwidth=5)
        message_frame.pack(anchor='e', padx=10, pady=10)
        message_label = Label(message_frame, text=message_object.text)
        message_label.pack()
    def start_window(self):
        self.messages_area.pack(side=TOP, expand=TRUE, fill=BOTH, padx=10, pady=10)

        bottom_frame = Frame(self.root)
        bottom_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)
        self.message_entry = Text(bottom_frame, height=5)
        self.message_entry.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        send_button = Button(bottom_frame, text="Send", command=self.handle_send)
        send_button.grid(row=0, column=1, sticky='ns', padx=5, pady=5)

        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)

        self.ai = AI_Chatter()

        self.root.mainloop()
    def handle_send(self):
        #"1.0": start of the text widget. "1" = first line, and "0" = first character of that line.
        # "end-1c": end of the text widget but exclude the final newline character. 
        # "end" is a special index that represents the position just after the last character. 
        # "-1c" = "minus one character," so it effectively excludes the last newline from the result.
        message_text = self.message_entry.get("1.0", "end-1c")
        new_message_object = Message('User', message_text)
        self.new_USER_message_label(new_message_object)
        
        ai_response = self.ai.generate_response(new_message_object.text)
        ai_message = Message('AI', ai_response)
        self.new_AI_message_label(ai_message)

        self.message_entry.delete("1.0", "end")