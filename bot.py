import discord
from datetime import datetime
from discord.ext import commands
import help_call
import roll

client = discord.Client()
characters = dict()

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

	if message.content.startswith('!uptime'):
		current_time = datetime.now()
		diff_time = current_time - startup_time
		startup_time = str(startup_time).split('.')[0]
		diff_time = str(diff_time).split('.')[0]
		await message.channel.send('```Started at: \t' + startup_time + '\nUptime: \t\t' + diff_time + '```')

	if message.content.startswith('!roll') or message.content.startswith('!r'):
		#output = roll.rolling_function(str(message.content), str(message.author))
		roll_rezult = roll.roll(str(message.content), str(message.author))
		output = roll_rezult.rolling()
		await message.channel.send(output)

token = open('test_token.txt', 'r')
client.run(token.read())
token.close()