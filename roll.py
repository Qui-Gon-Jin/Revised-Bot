import log
import random
import settings

class roll:
	def __init__(self, message, author):
		self.author = author
		self.crit_fail_check = True
		self.difficulty = 6
		self.dice = [0, 10]
		self.roll_result = []
		self.params = []
		self.roll = message.split(" ")
		self.result = [0, 0, "", 0]

	def rolling(self):
		del self.roll[0]

		if "-" in self.roll[-1]:	#check for parametrs
			self.params.append(self.roll[-1][1:])
			del self.roll[-1]

		if len(self.roll) > 1:		#cut the difficulty
			self.difficulty = int(self.roll[-1])
			del self.roll[-1]

		if "d" in self.roll[0]:		#count dices
			self.dice[0] = int(self.roll[0].split("d")[0])
			self.dice[1] = int(self.roll[0].split("d")[1])
		else:
			self.dice[0] = int(self.roll[0].split("d")[0])

		if self.difficulty > self.dice[1]:
			self.difficulty = self.dice[1]
			
		i = 0
		while i < self.dice[0]:		#count throw
			self.roll_result.append(random.randint(1, int(self.dice[1])))
			i += 1
			if self.roll_result[-1] == self.dice[1] and "e" in self.params: #explosion
				i -= 1
				self.result[3] +=1

		for i in self.roll_result:
			if i >= self.difficulty:	#count >= difficulty
				self.result[0] += 1
			if i == 1:					#count 1
				self.result[1] += 1

		if self.result[0] > self.result[1]:		#success
			self.result[2] = "Success: " + str(self.result[0] - self.result[1])
		elif self.result[0] == 0 and self.result[1] >= 1 and self.crit_fail_check == True:	#crit fail
			self.result[2] = "Crit fail: " + str(self.result[0] - self.result[1])
		elif self.result[0] <= self.result[1]:	#fail
			self.result[2] = "Fail: " + str(self.result[0] - self.result[1])

		output = (self.author + "\n" + self.result[2] + "\n" + str(self.roll_result))

		if self.result[3] >= 1:
			output += ("\n" + "Explodes: " + str(self.result[3]))

		return("```" + output + "```")