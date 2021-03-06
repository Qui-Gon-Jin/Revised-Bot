import Log
import random
import Settings
def rolling_function(message, author):
	crit_fail_check = True
	i = 0
	bonus_string = ""
	success = 0
	roll_result = []
	roll_result.clear()
	success = 0
	bonus = 0
	dice = []

	roll = message.split(" ")
	if len(roll) == 2:
		if "d" in roll[1]:
			dice.append(int(roll[1].split("d")[0]))
			dice.append(int(roll[1].split("d")[1]))
		else:
			dice.append(int(roll[1]))
			dice.append(10)
		threshold = 6

	elif len(roll) == 3:
		if 'd' in roll[1]:
			dice.append(int(roll[1].split("d")[0]))
			dice.append(int(roll[1].split("d")[1]))
		else:
			dice.append(int(roll[1]))
			dice.append(10)
		threshold = int(roll[2])

	while i < int(dice[0]):
		rolling = random.randint(1, int(dice[1]))
		roll_result.append(rolling)
		if rolling >= threshold:
			success = success + 1
			crit_fail_check = False;
			if rolling == int(dice[1]):
				i = i - 1
				bonus = bonus + 1
		elif rolling == 1:
			success = success - 1
		i = i + 1
		if success >= 1:
			throw_result = "Success: "
		elif success <= -1 and crit_fail_check == True:
			throw_result = "Crit Fail: "
		else:
			throw_result = "Fail: "
	Log.log_roll(message, throw_result, str(success), str(roll_result), str(bonus), roll)
	if bonus >= 1:
		bonus_string = ("\nbonus: " + str(bonus))

	output_string = ("```" 
					+ author + "\n"
					+ throw_result + str(success) + "\n"
					+ str(roll_result)
					+ bonus_string + "```")
	return(output_string)
	#return("```" + author + "\n" + throw_result + str(success) + "\n" + str(roll_result) + "\nbonus: " + str(bonus) + "```")