import discord
from datetime import datetime
from discord.ext import commands
import help_call
import roll
import settings
client = discord.Client()
startup_time = datetime.now()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	print(str(startup_time))

@client.event
async def on_message(message):
	author = str(message.author).split('#')[0]
	if message.author == client.user:
		return
	if message.content.startswith('!help'):
		await message.channel.send(help_call.help())

	if message.content.startswith('!roll') or message.content.startswith('!r'):
		roll_rezult = roll.roll(str(message.content), str(message.author))
		await message.channel.send(roll_rezult.rolling())

	if message.content.startswith('!settings'):
		settings_object = settings.settings(message.guild.id, message.channel.id)
		await message.channel.send(settings_object.show_settings())

token = open('test_token.txt', 'r')
client.run(token.read())
token.close()