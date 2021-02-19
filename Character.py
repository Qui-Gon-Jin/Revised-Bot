import log
class character:
	def __init__(self, character, author):
		self.character = character
		self.character_info = dict()
		self.character_info['name'] = character[1]
		self.character_info['clan'] = character[2]
		self.character_info['player'] = author
		log.log_character(author, self.character_info)
	def show_character(self):
		output = ("```User: " + self.character_info['player'] + "\nCharacter: " + self.character_info['name'] + "\nClan: " + self.character_info['clan'] + "```")
		return(output)
		
