import json

bonus_works = True
do_log = True

def show_settings():
	output = "```Is bonus mechanic works: " + str(bonus_works) +"\nIs logging is commiting: " + str(do_log) + "```"
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
