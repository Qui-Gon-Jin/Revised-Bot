import random

class initiative:

    def __init__(self, message, author):
        self.author = author
        self.roll = message.split(" ")
        self.result = 0

    def init(self):
        del self.roll[0]
        if len(self.roll) == 1:
            self.roll.append(self.roll[0])
        self.roll.append(random.randint(1, 10))
        self.init_value = "\nInitiative rating: " +  int(self. roll[0]) + int(self. roll[1])
        self.result = "\nInitiative: " + str(self.init_value + int(self.roll[2]))
        self.values = "\nValues: [" + str(self. roll[0]) + ", " + str(self. roll[1]) + ", " + str((self. roll[2])) + "]"
        return("```" + self.author + self.result + self.init_value + self.values + "```")