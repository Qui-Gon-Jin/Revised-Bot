import discord
from datetime import datetime
from discord.ext import commands
import help_call
import roll
import initiative
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
	#Help function call
	if message.content.startswith('!help'):
		await message.channel.send(help_call.help())
	#Roll function call
	if message.content.startswith('!r'):
		roll_rezult = roll.roll(str(message.content), str(message.author))
		await message.channel.send(roll_rezult.rolling())
	#Count initiative call
	if message.content.startswith('!i'):
		initiative_rezult = initiative.initiative(str(message.content), str(message.author))
		await message.channel.send(initiative_rezult.init())
#Choose token for logining in discord API
token = open('token.txt', 'r')
client.run(token.read())
token.close()
