class Character:
	def __init__(self, character, author):
		self.character = character
		self.character_info = dict()
		self.character_info['name'] = character[1]
		self.character_info['clan'] = character[2]
		self.character_info['player'] = author
	def show_character(self):
		output = ("```" + str(self.character_info) + "```")
		return(output)
		
