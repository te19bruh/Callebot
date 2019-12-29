import discord
import random
import string
from time import sleep
from discord.ext import commands
import asyncio
import tracemalloc

botid = ''

junior = 'Salanty#4884'
samuel = 'sampaixd#8896'
adams = 'Ugn Värmsson#7650'
adamw = 'Eyy B0ss#9506'
calle = 'Calle#4643'
solaf = 'Solaf#7852'

bot = commands.Bot(command_prefix='.')

#async def istyping():
#	async with message.channel.typing():
#		sleep(random.randint(1, 5))
		
#async def say():
#	await message.channel.send(mymessage)
	
#istypingsay():
#	async with message.channel.typing():
#		sleep(random.randint(1, 5))
#		await message.channel.send(mysessage)



class MyClient(discord.Client):
	
	i=0
	
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		if message.author == self.user:
			return
		
		if message.content == ('Calle, hjälp!'):
			await message.channel.send('+ingenjör')
			await message.channel.send('Calle, ingenjör count')
			await message.channel.send('Calle, vem bestämmer?')
			await message.channel.send('Trim!')
			await message.channel.send('Calle, vad gör en mus bra?')
			await message.channel.send('Calle, vad är vi?')

		if message.content == ('Calle, vad är vi?'):
			for i in range(3):
				
				if(i==1):
					async with message.channel.typing():
						sleep(random.randint(2, 5))
					await message.channel.send('Vi är ingenjörer.')
					sleep(random.randint(1,3))
				if(i==2):
					async with message.channel.typing():
						sleep(random.randint(3, 10))
					await message.channel.send('OCH INGENJÖRER LÖSER PROBLEM!')
				
				
		if message.content == ('Calle, vad gör en mus bra?'):
			for i in range(4):
				
				if(i==1):
					async with message.channel.typing():
						sleep(random.randint(2,5))
					await message.channel.send('Den där, runda...')
					sleep(random.randint(1,3))
				if(i==2):
					async with message.channel.typing():
						sleep(random.randint(2,5))
					await message.channel.send('knappen.')
					sleep(random.randint(1,3))
				if(i==3):
					async with message.channel.typing():
						sleep(random.randint(2,5))
					await message.channel.send('...den ska ha en såndär rund knapp i mitten. :)')
	
		if message.content == ('this is a test'):
			mymessage = "404 text not found"
			async with message.channel.typing():
				sleep(random.randint(1, 5))
			await message.channel.send(mymessage)
			
		if message.content == ('this is a test too'):
			mymessage = "505 text was found"
			istyping()
			say()
			
		if message.content == ('this is a test three'):
			istypingsay()

		if str(message.author) == adamw: 
			if message.content == ('Vad fick jag för betyg?'):
				mymessage = "Du får F!"
				async with message.channel.typing():
					sleep(random.randint(1, 5))
				await message.channel.send(mymessage)
				sleep(1)
				async with message.channel.typing():
					sleep(random.randint(1,5))
				mymessage = "Sorry, fel Adam."
				await message.channel.send(mymessage)
				mymessage = "Du får F!"
				async with message.channel.typing():
					sleep(random.randint(1, 5))
				await message.channel.send(mymessage)
				
		if str(message.author) != solaf:
			if message.content == ('Trim!'):
				async with message.channel.typing():
					sleep(random.randint(1,2))
				await message.channel.send('Ja, trim!')
				
		if message.content == ('+ingenjör'):
			addi(self)
			mymessage = "Ingenjör count: "+str(self.i)
			async with message.channel.typing():
				sleep(random.randint(1, 3))
			await message.channel.send(mymessage)

		if message.content == ('Calle, ingenjör count'):
			mymessage = "Ingenjör count: "+str(self.i)
			async with message.channel.typing():
				sleep(random.randint(1, 3))
			await message.channel.send(mymessage)	

#		if message.content == ('Calle, vem bestämmer?'):
#			mymessage = str('Inte ')  +str(message.author) +str(' iallafall.')
#			async with message.channel.typing():
#				sleep(random.randint(1, 5))
#			await message.channel.send(mymessage)

def addi(self):
	self.i = self.i + 1

async def istyping():
	async with message.channel.typing():
		sleep(random.randint(1, 5))
	
async def say():
	await message.channel.send(mymessage)
			
client = MyClient()
client.run(botid)
