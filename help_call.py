def help():
	guide = ("```Rolls are looking the same as they presented in a corebook:\n\n" +
	"!roll *number_of_dices* *roll_threshold*\n\n" +
	"As bot supports default  **roll_threshold** as 6, you can skip this part and type\n\n" +
	"!roll *number_of_dices*\n\n" +
	"Add -e in the end of comand to roll with explosive option (every 10 on roll will be reroled extra time)\n\n" +
	"If you need some extra of d10 dices, type\n\n" +
	"!roll *number_of_dices*d*dice_type* *roll_threshold*\n\n" +
	"Or skip **roll_threshold**, and it will counted as 6\n\n" +
	"!roll *number_of_dices*d*dice_type*\n\n\n" +
	"Wish you nice time <3```")
	return(guide)