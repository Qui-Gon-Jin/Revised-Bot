def help():
	help_file = "help.txt"
	with open(help_file) as help:
		content = help.read()
	return(content)
