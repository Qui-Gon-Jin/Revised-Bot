import log
import random
import settings

class initiative:
    def __init__(self, message, author):
        self.author = author
        self.roll = message.split(" ")
        self.result = 0

    def init(self):
        del self.roll[0]
        self.roll.append(random.randint(1, 10))
        if len(self.roll) == 2:
            self.result = int(self.roll[0]) + int(self.roll[0]) + int(self.roll[1])
            output = (self.author + "\nInitiative: " + str(self.result) + "\nValues: [" + str(self. roll[0]) + ", " + str(self. roll[0]) + ", " + str(self. roll[1]) + "]")

        if len(self.roll) == 3:
            self.result = int(self.roll[0]) + int(self.roll[1]) + int(self.roll[2])
            output = (self.author + "\nInitiative: " + str(self.result) + "\nValues: [" + str(self. roll[0]) + ", " + str(self. roll[1]) + ", " + str((self. roll[2])) + "]")
        
        return("```" + output + "```")