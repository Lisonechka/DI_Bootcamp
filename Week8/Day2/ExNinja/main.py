# Exercise 1 : Call History
class Phone:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        self.call_history.append(other_phone)
        print(f"{self.phone_number} called {other_phone}")

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, to, fro, content):
        self.messages.append({'to': to, 'from': fro, 'content': content})

    def show_outgoing_messages(self):
        print("The outgoing messages are:")
        for i in self.messages:
            if i.get('from') == self.phone_number:
                print(i)
            else:
                print("0")

    def show_incoming_messages(self):
        print("The incoming messages are:")
        for i in self.messages:
            if i.get('to') == self.phone_number:
                print(i)
            else:
                print("0")

    def show_messages_from(self, phone_number):
        print(f"The messages from {phone_number} are:")
        for i in self.messages:
            if i.get('from') == phone_number:
                print(i)
            else:
                print("0")


number1 = Phone("0525631221")
number1.call("0558826829")
print(number1.call_history)
number1.show_call_history()
number1.send_message('0558826829', '0525631221', 'love you')
number1.show_outgoing_messages()
number1.show_incoming_messages()
