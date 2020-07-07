import discord
from discord.ext import commands
import Help
import Roll
import Settings
from Charlist import Charlist

client = discord.Client()
roll_result = []
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!help'):
		await message.channel.send(Help.help())
	if message.content.startswith('!set'):
		await message.channel.send(Settings.show_settings())
	if message.content.startswith('!roll'):
		roll = message.content.split(" ")
		dice = roll[1].split("d")
		threshold = int(roll[2])
		await message.channel.send(Roll.rolling_function(roll, dice, threshold, roll_result, str(message.author)))
	if message.content.startswith('!re_set'):
		new_set = message.content.split(" ")
		if len(new_set) == 3:
			await message.channel.send(Settings.change_settings(new_set[1], new_set[2]))
		else:
			await message.channel.send("```You doind it wrong\nTry !re_set value value```")

	#if message.content.startswith('!show_char'):
		#await message.channel.send("```" + new_character.name + "\n" + new_character.character + "```")

	if message.content.startswith('!add_char'):
		character = message.content.split(" ")
		if len(character) == 2:
			new_character = Charlist(str(character[1]), str(message.author))
			await message.channel.send("```Done\nCharacter: " + character[1] + "\nBy user: " + str(message.author) + "\nIs done```")
		else:
			await message.channel.send("```You doind it wrong\nTry !add_char name```")
			
client.run('NzI5NTkzMjA0MTc2OTc3OTcx.XwLPlQ.DjcowfdOWVWq3XQ_1wJz43EQOLs')