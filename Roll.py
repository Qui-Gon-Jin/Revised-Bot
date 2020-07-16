import Log
import random
def rolling_function(message, author):
	i = 0
	success = 0
	roll_result = []
	roll_result.clear()
	success = 0
	bonus = 0
	dice = []

	roll = message.split(" ")
	if len(roll) == 3:
		if 'd' in roll[1]:
			dice = roll[1].split("d")
			threshold = int(roll[2])
		else:
			dice.append(int(roll[1]))
			dice.append(10)
			threshold = int(roll[2])
	if len(roll) == 2:
		dice.append(int(roll[1]))
		dice.append(10)
		threshold = 6

	while i < int(dice[0]):
		rolling = random.randint(1, int(dice[1]))
		roll_result.append(rolling)
		if rolling >= threshold:
			success = success + 1
			if rolling == int(dice[1]):
				i = i - 1
				bonus = bonus + 1
		elif rolling == 1:
			success = success - 1
		i = i + 1
		if success >= 1:
			throw_result = "Success: "
		elif success <= -1:
			throw_result = "Crit Fail: "
		else:
			throw_result = "Fail: "
	Log.log_roll(message, throw_result, str(success), str(roll_result), str(bonus), roll)
	return("```" + author + "\n" + throw_result + str(success) + "\n" + str(roll_result) + "\nbonus: " + str(bonus) + "```")