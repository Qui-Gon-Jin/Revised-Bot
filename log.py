import datetime
now = datetime.datetime.now()
def log_roll(author, throw_result, success, roll_result, bonus, roll):
	log = open('log.txt', 'a')
	log.write(author + "\t" + throw_result + success + "\t" + "" + roll_result + "\tbonus: " + str(bonus) + "\n")
	log.write("( "+ str(roll) + " )" + "\t" + str(now.strftime("%H:%M - %d.%m")) + "\n\n")
	log.close()
def log_character(author, character_info):
	log = open('log.txt', 'a')
	log.write('User: ' + character_info['player'] + "\nCreated: " + character_info['name'] + "\tClan: " + character_info['clan'] + "\n")
	log.write("At " + str(now.strftime("%H:%M - %d.%m")) + "\n\n")
	log.close()