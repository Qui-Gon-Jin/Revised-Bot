import log
import random
import settings

class roll:
	def __init__(self, message, author):
		self.message = message
		self.author = author
		self.crit_fail_check = True
		self.difficulty = 6
		self.dice = [0, 10]
		self.roll_result = []
		self.params = []
		self.roll = message.split(" ")


	def rolling(self):
		del self.roll[0]

		if "-" in self.roll[-1]:
			self.params.append(self.roll[-1][1:])
			del self.roll[-1]

		if len(self.roll) > 1:
			self.difficulty = self.roll[-1]
			del self.roll[-1]

		if "d" in self.roll[0]:
			self.dice[0] = int(self.roll[0].split("d")[0])
			self.dice[1] = int(self.roll[0].split("d")[1])
		else:
			self.dice[0] = int(self.roll[0].split("d")[0])



		return("```dices: " + str(self.dice) + "\ndiff: " + str(self.difficulty) + "\nparams: " + str(self.params) + "```")