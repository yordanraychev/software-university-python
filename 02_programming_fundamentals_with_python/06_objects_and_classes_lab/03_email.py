class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


final_emails = []
info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    final_emails.append(email_info)
    info = input()
indices = [int(s) for s in input().split(", ")]
for index in indices:
    final_emails[index].send()
for current_email in final_emails:
    print(current_email.get_info())
