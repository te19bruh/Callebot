import discord
import random
import string
from time import sleep
from discord.ext import commands
import asyncio
import tracemalloc
import botlib.info as info


botid = info.getBotId()
botid = botid[0]

ingenjörCount = 0

firstname   = info.setUserFirst()
lastname    = info.setUserLast()
discordTag  = info.setUserDiscord()

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f"\nLogged on as {self.user}\n")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        async def sendMessage(messagelist, istyping=True):
            print(f"{message.author}:\t{message.content}")
            for messages in messagelist:
                if istyping == True:
                    async with message.channel.typing():
                        sleep(random.randint(1,5))
                await message.channel.send(messages)
                print(f"{self.user}:\t{messages}")
    
        def getUser(Userid):
            return 
    
        if message.content == ('Calle, hjälp!'):
            messagelist = [
            'ingenjör',
            'Calle, ingenjör count',
            'Calle, vem bestämmer?',
            'Trim!',
            'Calle, vad gör en mus bra?',
            'Calle, vad är vi?']
            await sendMessage(messagelist, istyping=False)

        if message.content == ('Calle, vad är vi?'):
            messagelist = ['Vi är ingenjörer.', 'OCH INGENJÖRER LÖSER PROBLEM!']    
            await sendMessage(messagelist)
        
        if message.content == ('Calle, vad gör en mus bra?'):
            messagelist = ['Den där, runda...', 'knappen.', '...den ska ha en såndär rund knapp i mitten.',':)']    
            await sendMessage(messagelist)
            
            
        if message.author != discordTag[5] and message.content == ('Trim!'):
            messagelist = ['Ja, trim!']    
            await sendMessage(messagelist)
        
        if message.content == ('Calle, ingenjör count'):
            messagelist = ['Jag har sagt ingenjörer {ingenjörCount} gånger', 'OCH INGENJÖRER LÖSER PROBLEM!']    
            await sendMessages(messagelist)
        
        if message.content == ('Calle, vem bestämmer?'):
            messagelist = [f'Inte {message.author} iallafall']    
            await sendMessage(messagelist)
        
        
client = MyClient()
client.run(botid)
