import datetime
def log_roll(author, throw_result, success, roll_result, bonus, roll):
	now = datetime.datetime.now()
	log = open('log.txt', 'a')
	log.write(author + "\t" + throw_result + success + "\t" + "" + roll_result + "\tbonus: " + str(bonus) + "\n")
	log.write("( "+ str(roll[1]) + ", " + str(roll[2]) + " )" + "\t" + str(now.strftime("%H:%M - %d.%m")) + "\n\n")
	log.close()