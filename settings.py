import json
class settings:
	def __init__(self, guild, channel):
		self.server_name = guild
		self.chat_name = channel
		self.explosive_dice_by_default = False
		self.do_log = True

	def show_settings(self):
		output = ("```" 
			+ "server_id: " + str(self.server_name)
			+ "\nchat_id: " + str(self.chat_name)
			+ "\nBonus mechanic by default: " 
			+ str(self.explosive_dice_by_default)
			+ "\nLogging: " + str(self.do_log)
			+ "```")
		return(output)

	def change_bonus_state(self, bonus):
		if str(bonus) == "False":
			bonus = False
		elif str(bonus) == "True":
			bonus = True
		self.explosive_dice = bonus
		return("```" + str(self.explosive_dice) + "```")

	def change_log_state(self, log):
		self.do_log = log
		return("```" + self.do_log + "```")
	def change_dice_mod(self, mod):
		self.dice_mod = mod
		return("```" + self.mod + "```")
	def serialize():
		with open("Settings.json", "w") as write_file:
			json.dump(data, write_file)
		pass
	def deserialize():
		pass
