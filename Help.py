def help():
	intro = "Hey, hey.\nIt's me ~~Mario~~ Revised Bot for playing Vampire the Masquarade using discord.\n"
	guide = "Use !roll **n**d**n** **n** with your: \n```1 - number of dices\n2 - dice max value\n3 - success threshold\n!set - to see current settings\n!re_set - to change settings```"
	conclusion = "```!roll 4d10 6```\nWish you nice time <3"
	output = intro + guide + conclusion
	return(output)