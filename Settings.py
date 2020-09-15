import json
explosive_dice = True;
do_log = True

def show_settings():
	output = "```Bonus mechanic: " + str(explosive_dice) +"\nLogging: " + str(do_log) + "```"
	return(output)
def change_settings(bonus, log):
	bonus_works = bonus
	do_log = log
	print(bonus_works, " ", do_log)
	pass
def serialize():
	with open("Settings.json", "w") as write_file:
		json.dump(data, write_file)
	pass
def deserialize():
	pass
