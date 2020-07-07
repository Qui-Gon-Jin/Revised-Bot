import discord
from discord.ext import commands
import Help
import Roll
import Settings
from Character import Character

client = discord.Client()
roll_result = []
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	global new_character
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
		output = Roll.rolling_function(roll, dice, threshold, roll_result, str(message.author))
		await message.channel.send(output)

	if message.content.startswith('!add_char'):
		character = message.content.split(" ")
		new_character = Character(character, str(message.author))

	if message.content.startswith('!show_char'):
		await message.channel.send(new_character.show_character())
	#if message.content.startswith('!mod_char'):


token = open('token.txt', 'r')
client.run(token.read())
token.close()