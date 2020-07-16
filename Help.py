def help():
	guide = "```Use !roll **number**d**dice** **threshold**\nIf you will input !roll **number** **threshold**, d10 will be rolled as default\n!roll **number** will roll your number of yours and default d10 with threshold 6" + "\n!set - to see current settings\n!re_set - to change settings"
	conclusion = "\nWish you nice time <3```"
	output = guide + conclusion
	return(output)