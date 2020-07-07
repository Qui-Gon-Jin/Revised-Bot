import Log
import random
def rolling_function(roll, dice, threshold, roll_result, message):
	i = 0
	success = 0
	roll_result.clear()
	success = 0
	bonus = 0

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
	Log.log(message, throw_result, str(success), str(roll_result), str(bonus), roll)
	return("```" + message + "\n" + throw_result + str(success) + "\n" + str(roll_result) + "\nbonus: " + str(bonus) + "```")