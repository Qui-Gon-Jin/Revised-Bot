import json
class Settings:
	def __init__(self):
		self.explosive_dice = True
		self.do_log = True
		self.dice_mod = True
	def show_settings(self):
		output = ("```Bonus mechanic: " 
					+ str(self.explosive_dice)
					+ "\nLogging: "
					+ str(self.do_log)
					+ "\ndice mod: "
					+ str(self.dice_mod)
					+ "```")
		return(output)
	def change_bonus_state(self, bonus):
		self.explosive_dice = bonus
		return("```" + self.explosive_dice + "```")
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
