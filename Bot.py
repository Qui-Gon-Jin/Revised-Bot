import discord
from datetime import datetime
from discord.ext import commands
import Help
import Roll
import Settings
from Character import Character

client = discord.Client()
characters = dict()

startup_time = datetime.now()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	print(str(startup_time))
@client.event
async def on_message(message):
	global characters
	global new_character
	author = str(message.author).split('#')[0]
	if message.author == client.user:
		return
	if message.content.startswith('!help'):
		await message.channel.send(Help.help())


	if message.content.startswith('!uptime'):
		current_time = datetime.now()
		diff_time = current_time - startup_time
		startup_time = str(startup_time).split('.')[0]
		diff_time = str(diff_time).split('.')[0]
 
		await message.channel.send('```Started at: \t' + startup_time + '\nUptime: \t\t' + diff_time + '```')

	if message.content.startswith('!roll'):
		output = Roll.rolling_function(str(message.content), str(message.author))
		await message.channel.send(output)

	if message.content.startswith('!set'):
		await message.channel.send(Settings.choose_set(str(message.content)))

	if message.content.startswith('!add_char'):
		character = message.content.split(" ")
		characters[author] = Character(character, author)
		
	if message.content.startswith('!mod_char'):
		character = message.content.split(" ")
		characters[author] = Character(character, author)

	if message.content.startswith('!show_char'):
		await message.channel.send(characters[author].show_character())

token = open('Token.txt', 'r')
client.run(token.read())
token.close()