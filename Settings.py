import json
explosive_dice = True
do_log = True
dice_mod = True

def choose_set(message):
	set_choose = message.split(" ")
	if len(set_choose) == 1:
		return(show_settings())
	elif set_choose[1] == "bonus":
		change_bonus_state(set_choose[2])
	elif set_choose[1] == "log":
		change_log_state(set_choose[2])
	elif set_choose[1] == "mod":
		change_dice_mod(set_choose[2])


def show_settings():
	output = ("```Bonus mechanic: " 
				+ str(explosive_dice)
				+ "\nLogging: "
				+ str(do_log)
				+ "\ndice mod: "
				+ str(dice_mod)
				+ "```")
	return(output)
def change_bonus_state(bonus):
	bonus_works = bonus
	print(bonus_works)
def change_log_state(log):
	do_log = log
	print(do_log)
def change_dice_mod(mod):
	dice_mod = mod
	print(mod)
def serialize():
	with open("Settings.json", "w") as write_file:
		json.dump(data, write_file)
	pass
def deserialize():
	pass
