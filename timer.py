from datetime import datetime

class timer:

    def __init__(self, message, author):
        self.author = author
        self.roll = message.split(" ")
        self.startup_time = datetime.now()
    
    def start(self):
        return ("```Timer request from" + str(self.author) + "\nAppered at " + str(self.startup_time) + "```")
